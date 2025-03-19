# database_manager.py
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from enties.master_no_check import IdMaster
import pandas as pd
from logging_config import logger



class DatabaseManager:
    def __init__(self, db_url='postgresql://postgres:12345@localhost:5432/demo1'):
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

    def map_to_id_master(self, row, table_name='under_body_page_data3'):
        try:
            created_at_value = pd.to_datetime(row['収集日時'], format='%Y/%m/%d %H:%M', errors="coerce")
            id_master_instance = IdMaster(
                # table_name=table_name,
                created_at=created_at_value,
                delete_flag=False
            )
            logger.debug(f"Successfully mapped row to IdMaster for table {table_name}")
            return id_master_instance
        except Exception as e:
            logger.error(f"Error mapping row to IdMaster for table {table_name}: {e}", exc_info=True)
            raise

    def insert_id_master_data(self, session, df, table_name):
        try:
            id_master_instances = df.apply(lambda row: self.map_to_id_master(row, table_name=table_name), axis=1).tolist() # Convert to list
            session.add_all(id_master_instances)
            session.flush()  # Flush to get generated IDs

            # Get the IDs of the inserted IdMaster instances
            id_master_ids = [instance.id for instance in id_master_instances]
            logger.info(f"Successfully inserted id_master data for {table_name}. IDs: {id_master_ids}")
            return id_master_ids

        except Exception as e:
            session.rollback()
            logger.error(f"Error inserting id_master data for {table_name}: {e}", exc_info=True)
            raise

    def insert_model_data(self, session, df, table_mapper, id_master_ids):
        try:
            def map_to_model_with_id(row, id_master_id):
                model_instance = table_mapper().map_to_model(row)
                model_instance.id = id_master_id  # Set the id for the model
                return model_instance

            model_instances = [map_to_model_with_id(row, id_master_id) for row, id_master_id in zip(df.to_dict('records'), id_master_ids)]

            session.add_all(model_instances)
            session.flush()  # Flush to make sure it will affect to DB
            logger.info(f"Successfully inserted model data using {table_mapper.__name__}")

        except Exception as e:
            session.rollback()
            logger.error(f"Error inserting model data using {table_mapper.__name__}: {e}", exc_info=True)
            raise