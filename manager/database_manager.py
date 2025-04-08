from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from enties.master import IdMaster
import pandas as pd
from .logging_config import logger
from util.helper import connect_string
from util.constants import DATETIME_FORMAT, DEFAULT_DELETE_FLAG


class DatabaseManager:
    def __init__(self):
        self.connection_string = connect_string()
        self.engine = None
        self.Session = None
        self.processed_created_at = set()

    def connect_to_db(self):
        try:
            if not self.engine:
                self.engine = create_engine(self.connection_string)
                self.Session = sessionmaker(bind=self.engine)
            return self.Session()
        except Exception as e:
            logger.error(f"Database connection error: {e}")
            return None

    def insert_id_master_data(self, session, df):
        try:
            id_master_instances = []
            id_master_ids = []
            id_master_created_at = []

            for idx, row in df.iterrows():
                created_at_value = pd.to_datetime(row['収集日時'], format= DATETIME_FORMAT, errors="coerce")
                if created_at_value in self.processed_created_at:
                    # logger.info(f"Skipping insert for duplicate created_at: {created_at_value}")
                    continue  

                id_master_instance = IdMaster(
                    created_at=created_at_value,
                    delete_flag= DEFAULT_DELETE_FLAG
                )
                id_master_instances.append(id_master_instance)
                
             
                self.processed_created_at.add(created_at_value)

            session.add_all(id_master_instances)
            session.flush()  # Flush to get generated IDs

            for instance in id_master_instances:
                id_master_ids.append(instance.id)
                id_master_created_at.append(instance.created_at)

            logger.info(f"Successfully inserted id_master data for IDs: {id_master_ids}")
            return id_master_ids, id_master_created_at

        except Exception as e:
            session.rollback() 
            logger.error(f"Error inserting id_master data with {id_master_ids}: {e}", exc_info=True)
            raise

    def insert_model_data(self, session, df, table_mapper, id_master_ids, id_master_created_times):
        try:
            def map_to_model_with_id_and_created_at(row, id_master_id, created_time):
                
                if  created_time == row['収集日時']:
                    model_instance = table_mapper().map_to_model(row)
                    model_instance.id = id_master_id 
                return model_instance
            
            model_instances = [map_to_model_with_id_and_created_at(row, id_master_id, created_time) for row, id_master_id ,
                             created_time in zip(df.to_dict('records'), id_master_ids, id_master_created_times)]

            session.add_all(model_instances)
            session.flush()  # Flush to make sure it will affect to DB
            logger.info(f"Successfully inserted model data using {table_mapper.__name__}")

        except Exception as e:
            session.rollback()
            logger.error(f"Error inserting model data using {table_mapper.__name__}: {e}", exc_info=True)
            raise