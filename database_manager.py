# database_manager.py
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from enties.master_no_check import IdMaster
import pandas as pd
from logging_config import logger



class DatabaseManager:
    def __init__(self, db_url='postgresql://postgres:12345@localhost:5432/test_db'):
        self.engine = create_engine(db_url)
        self.Session = sessionmaker(bind=self.engine)

    def connect_to_db(self):
        try:
            session = self.Session()
            logger.info("Successfully connected to the database.")
            return session
        except Exception as e:
            logger.error(f"Error connecting to the database: {e}", exc_info=True)
            return None  # Or raise an exception if it's critical

    def map_to_id_master(self, row):
        try:
            created_at_value = pd.to_datetime(row['収集日時'], format='%Y/%m/%d %H:%M', errors="coerce")
            id_master_instance = IdMaster(
                created_at = created_at_value,
                delete_flag = 0
            )
            return id_master_instance
        except Exception as e:
            logger.error(f"Error mapping row to IdMaster{e}", exc_info=True)
            raise
    
    
    def insert_id_master_data(self, session, df):
        try:
            id_master_instances = df.apply(lambda row: self.map_to_id_master(row), axis=1).tolist() # Convert to list
            session.add_all(id_master_instances)
            session.flush()  # Flush to get generated IDs
            id_master_ids = []
            id_master_created_at = []
            # Get the IDs of the inserted IdMaster instances
            for instance in id_master_instances:
                id_master_ids.append(instance.id)
                id_master_created_at.append(instance.created_at)
            logger.info(f"Successfully inserted id_master data for  IDs: {id_master_ids}")
        
            return id_master_ids ,id_master_created_at

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