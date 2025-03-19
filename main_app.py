import os
from functools import reduce
from pathlib import Path
from datetime import datetime
import pandas as pd
from logging_config import logger
from folder_manager import FolderManager
from data_processor import DataProcessor
from database_manager import DatabaseManager
from mapper.door_mapper import DoorPageData1Mapper, DoorPageData2Mapper
from mapper.under_body_mapper import UnderBodyPageData1Mapper, UnderBodyPageData2Mapper, UnderBodyPageData3Mapper
from mapper.saimen_mapper import SmPageData1Mapper, SmPageData2Mapper
from enties.master_no_check import RoundMasterMapperNoCheck
from mapper.columns_mapping import (round_master_columns, door1_columns, door2_columns,
                                   under_body1_columns, under_body2_columns, under_body3_columns,
                                   sm_page_data1_columns, sm_page_data2_columns)



def tabel_names_mapper(category_name):
    if category_name == "ドア":
        return DoorPageData1Mapper, DoorPageData2Mapper
    elif category_name == "UB":
        return UnderBodyPageData1Mapper, UnderBodyPageData2Mapper, UnderBodyPageData3Mapper
    elif category_name == "SM":  # Added for SM
        return SmPageData1Mapper, SmPageData2Mapper
    return None

class MainApp:
    def __init__(self, root_dir):
        self.root_dir = root_dir
        self.folder_manager = FolderManager(self.root_dir)
        self.data_processor = DataProcessor()
        self.database_manager = DatabaseManager()

    def process_door_data(self, merged_df, table_mappers, session):
        try:
            df_door1 = merged_df[door1_columns]
            df_door2 = merged_df[door2_columns]
            door1_table_name = 'door_page_data1'
            door2_table_name = 'door_page_data2'

            id_master_ids_door1 = self.database_manager.insert_id_master_data(session, df_door1, door1_table_name)
            id_master_ids_door2 = self.database_manager.insert_id_master_data(session, df_door2, door2_table_name)

            self.database_manager.insert_model_data(session, df_door1, table_mappers[0], id_master_ids_door1)
            self.database_manager.insert_model_data(session, df_door2, table_mappers[1], id_master_ids_door2)
            logger.info("Successfully processed door data.")

        except Exception as e:
            session.rollback()
            logger.error(f"Error processing door data: {e}", exc_info=True)
            raise

    def process_under_body_data(self, merged_df, table_mappers, session):
        try:
            df_under_body1 = merged_df[under_body1_columns]
            df_under_body2 = merged_df[under_body2_columns]
            df_under_body3 = merged_df[under_body3_columns]

            id_master_ids_under_body1 = self.database_manager.insert_id_master_data(session, df_under_body1, 'under_body_page_data1')
            id_master_ids_under_body2 = self.database_manager.insert_id_master_data(session, df_under_body2, 'under_body_page_data2')
            id_master_ids_under_body3 = self.database_manager.insert_id_master_data(session, df_under_body3, 'under_body_page_data3')

            self.database_manager.insert_model_data(session, df_under_body1, table_mappers[0],id_master_ids_under_body1)
            self.database_manager.insert_model_data(session, df_under_body2, table_mappers[1],id_master_ids_under_body2)
            self.database_manager.insert_model_data(session, df_under_body3, table_mappers[2],id_master_ids_under_body3)
            logger.info("Successfully processed under body data.")

        except Exception as e:
            session.rollback()
            logger.error(f"Error processing under body data: {e}", exc_info=True)
            raise

    def process_sm_data(self, merged_df, table_mappers, session):
        try:
            if table_mappers is None:
                logger.warning("No table mappers available for SM data.")
                return

            df_sm1 = merged_df[sm_page_data1_columns]
            df_sm2 = merged_df[sm_page_data2_columns]
            sm_name1 = 'sm_page_data1'
            sm_name2 = 'sm_page_data2'

            id_master_ids_sm1 = self.database_manager.insert_id_master_data(session, df_sm1, sm_name1)
            id_master_ids_sm2 = self.database_manager.insert_id_master_data(session, df_sm2, sm_name2)

            self.database_manager.insert_model_data(session, df_sm1, table_mappers[0],id_master_ids_sm1)
            self.database_manager.insert_model_data(session, df_sm2, table_mappers[1],id_master_ids_sm2)
            logger.info("Successfully processed SM data.")

        except Exception as e:
            session.rollback()
            logger.error(f"Error processing SM data: {e}", exc_info=True)
            raise

    def process_csv_files(self, data_dir, category_name):
        # get data_dit name
        parent_dir = os.path.dirname(data_dir)
        folder_name = os.path.basename(data_dir)
        parent_folder_name = os.path.basename(parent_dir)
        output_file = f'merged_df_for{parent_folder_name}{folder_name}.csv'
        files = list(Path(data_dir).glob("**/*.csv"))
        current_date = datetime.now().strftime('%Y%m%d')
        logger.info(f"Processing CSV files in {data_dir} for category {category_name}")
        dataframes = []
        for file_path in files:
            file_name = file_path.name
            if current_date not in file_name:
                try:
                    df = self.data_processor.read_and_process_csv(file_path)
                    if df is not None:
                        dataframes.append(df)
                except Exception as e:
                     logger.error(f"A error: {e}", exc_info=True)
                     return

        if len(dataframes) > 1:
            try:
                merged_df = reduce(lambda left, right: pd.merge(left, right, on='収集日時', how='inner'), dataframes)

                merged_df['収集日時'] = pd.to_datetime(merged_df['収集日時'], format='%Y/%m/%d %H:%M', errors="coerce")
                merged_df['hour_minute'] = merged_df['収集日時'].dt.strftime('%H:%M')
                merged_df['year'] = merged_df['収集日時'].dt.year
                merged_df['month'] = merged_df['収集日時'].dt.month
                merged_df['day'] = merged_df['収集日時'].dt.day
                merged_df['hour'] = merged_df['収集日時'].dt.hour
                merged_df['minute'] = merged_df['収集日時'].dt.minute

                # 
                merged_df['update_time'] = datetime.now()
                merged_df['delete_flag'] = False
                merged_df['round_update'] = False
                round_info = self.data_processor.get_round_info_for_all_times(merged_df)

                merged_df = pd.merge(merged_df, round_info, on='hour_minute', how='inner')
                merged_df.to_csv(output_file,  encoding="shift-jis",index=False)
                table_mappers = tabel_names_mapper(category_name)
                if table_mappers:
                    session = self.database_manager.connect_to_db()

                    if session is None:
                        logger.error("Failed to connect to the database.")
                        return

                    try:
                        session.begin()  # Start explicit transaction
                        logger.info("Starting explicit transaction.")

                        round_master = merged_df[round_master_columns]
                        round_mst_no_check = RoundMasterMapperNoCheck()
                        round_master = [round_mst_no_check.map_to_fields(row) for idx, row in round_master.iterrows()]
                        session.add_all(round_master)
                        session.flush()  # Flush to get generated IDs
                        
                        if category_name == "ドア":
                            self.process_door_data(merged_df, table_mappers, session)
                        elif category_name == "UB":
                            self.process_under_body_data(merged_df, table_mappers, session)
                        elif category_name == "SM":
                            self.process_sm_data(merged_df, table_mappers, session)

                        session.commit()  # Commit if all successful
                        logger.info("Data processing completed successfully. Committing transaction.")

                    except Exception as e:
                        session.rollback()  # Rollback if any error occurs
                        logger.error(f"Error processing data, rolling back transaction: {e}", exc_info=True)
                        raise # Re-raise the exception

                    finally:
                        session.close()
                        logger.info("Session closed.")
            except Exception as e:
               logger.error(f"Failed to process dataframe: {e}", exc_info=True)
        else:
            logger.warning("File must be more than one, skipping")

    def process_directory(self, category_name):
        """ (SM, Door, under body)."""
        rounds = self.folder_manager.check_folder_round(category_name)
        if rounds:
            for round_name in rounds:
                data_category_dir = os.path.join(self.root_dir, category_name, round_name)
                if os.path.exists(data_category_dir) and os.path.isdir(data_category_dir):
                    self.process_csv_files(data_category_dir, category_name)
                else:
                    logger.error(f"Directory {data_category_dir} does not exist or is not a directory.")

    def main(self):
        try:
            categories = self.folder_manager.check_folder_type()
            if categories:
                for category in categories:
                    self.process_directory(category)
        except Exception as e:
           logger.error(f"A error: {e}", exc_info=True)

if __name__ == "__main__":
    root_dir = "C:\\Users\\nguyen-duy-phong\\Downloads\\infura_data\\0314"
    app = MainApp(root_dir)
    app.main()