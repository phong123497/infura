import os
import schedule
import time
import sys
import gc
from functools import reduce
from pathlib import Path
from datetime import datetime
import pandas as pd
from logging_config import logger
from folder_manager import FolderManager
from data_processor import DataProcessor
from database_manager import DatabaseManager
from mapper.door_mapper import DoorPageData1Mapper, DoorPageData2Mapper
from mapper.under_body_mapper import UnderBodyPageData1Mapper, UnderBodyPageData2Mapper, UnderBodyPageData3Mapper,UnderBodyPageData4Mapper
from mapper.saimen_mapper import SmPageData1Mapper, SmPageData2Mapper
from mapper.andon_mapper import AndonPageDataMapper
from mapper.ndai_mapper import NdaiPageDataMapper
from enties.master import RoundMasterMapper
from mapper.round_mapping import round_and_is_morning_mapping
from mapper.columns_mapping import (id_master_columns, common_columns, round_master_columns, door1_columns, door2_columns,
                                   under_body1_columns, under_body2_columns, under_body3_columns,under_body4_columns,
                                   sm_page_data1_columns, sm_page_data2_columns, andon_page_data_columns, ndai_page_data_columns)

from constants import (
    CATEGORY_DOOR, CATEGORY_UB, CATEGORY_SM, CATEGORY_ANDON, CATEGORY_NDAI,UB_DOOR_SM_CATEGORIES,
    DATE_FORMAT, TIME_FORMAT
)



def tabel_names_mapper(category_name):
    if category_name == CATEGORY_DOOR:
        return DoorPageData1Mapper, DoorPageData2Mapper
    elif category_name == CATEGORY_UB:
        return UnderBodyPageData1Mapper, UnderBodyPageData2Mapper, UnderBodyPageData3Mapper,UnderBodyPageData4Mapper
    elif category_name == CATEGORY_SM:
        return SmPageData1Mapper, SmPageData2Mapper
    elif category_name == CATEGORY_ANDON:
        return AndonPageDataMapper
    elif category_name == CATEGORY_NDAI:
        return NdaiPageDataMapper
    return None


def get_column_mapping(category_name):
    if category_name == CATEGORY_DOOR:
        return door1_columns, door2_columns
    elif category_name == CATEGORY_UB:
        return under_body1_columns, under_body2_columns, under_body3_columns,under_body4_columns
    elif category_name == CATEGORY_SM:
        return sm_page_data1_columns, sm_page_data2_columns
    elif category_name == CATEGORY_ANDON:
        return andon_page_data_columns,
    elif category_name == CATEGORY_NDAI:
        return ndai_page_data_columns,
    return None


class MainApp:
    def __init__(self, root_dir):
        self.root_dir = root_dir
        self.folder_manager = FolderManager(self.root_dir)
        self.data_processor = DataProcessor()
        self.database_manager = DatabaseManager()
        self.is_running = True
        self.temp_dataframes = []

    def process_category_data(self, merged_df, category_name, table_mappers, session, id_master_ids,
                                  id_master_created_times):
        try:
            logger.info(f"Processing data for category: {category_name}")

            # Get column mapping for the current category
            column_mapping = get_column_mapping(category_name)
            if not column_mapping:
                logger.warning(f"No column mapping found for category {category_name}. Skipping.")
                return

            if len(column_mapping) == 1:
                # Processing logic for ANODN and NDAI
                columns = column_mapping[0]
                missing_columns = [col for col in columns if col not in merged_df.columns]
                if missing_columns:
                    # logger.warning(f"Missing columns in {category_name}: {missing_columns}")
                    df = merged_df[common_columns].copy()
                else:
                    df = merged_df[columns].copy()

                self.database_manager.insert_model_data(session, df, table_mappers, id_master_ids,
                                                         id_master_created_times)
                self.temp_dataframes.append(df)  # Add df to temp list
            elif len(column_mapping) == 2:
                # DOOR, SM, # check len mapper = 2 
                columns1, columns2 = column_mapping

                missing_columns_1 = [col for col in columns1 if col not in merged_df.columns]
                if missing_columns_1:
                    df1 = merged_df[common_columns].copy()
                else:
                    df1 = merged_df[columns1].copy()
                missing_columns_2 = [col for col in columns2 if col not in merged_df.columns]
                if missing_columns_2:
                    df2 = merged_df[common_columns].copy()
                else:
                    df2 = merged_df[columns2].copy()
                    
                self.database_manager.insert_model_data(session, df1, table_mappers[0], id_master_ids, id_master_created_times)
                self.database_manager.insert_model_data(session, df2, table_mappers[1], id_master_ids, id_master_created_times)
                self.temp_dataframes.extend([df1, df2])

            elif len(column_mapping) == 4: 
                # UNDER_BODY processing
                columns1, columns2, columns3, columns4 = column_mapping

                ub1_missing_columns = [col for col in columns1 if col not in merged_df.columns]
                ub2_missing_columns = [col for col in columns2 if col not in merged_df.columns]
                ub3_missing_columns = [col for col in columns3 if col not in merged_df.columns]
                ub4_missing_columns = [col for col in columns4 if col not in merged_df.columns]
                if ub1_missing_columns:
                    df_ub1 = merged_df[common_columns].copy()
                else:
                    df_ub1 = merged_df[columns1].copy()
                if ub2_missing_columns:
                    df_ub2 = merged_df[common_columns].copy()
                else:
                    df_ub2 = merged_df[columns2].copy()
                if ub3_missing_columns:
                    df_ub3 = merged_df[common_columns].copy()
                else:
                    df_ub3 = merged_df[columns3].copy()
                if ub4_missing_columns:
                    df_ub4 = merged_df[common_columns].copy()
                else:
                    df_ub4 = merged_df[columns4].copy()

                self.database_manager.insert_model_data(session, df_ub1, table_mappers[0], id_master_ids,id_master_created_times)
                self.database_manager.insert_model_data(session, df_ub2, table_mappers[1], id_master_ids,id_master_created_times)
                self.database_manager.insert_model_data(session, df_ub3, table_mappers[2], id_master_ids,id_master_created_times)
                self.database_manager.insert_model_data(session, df_ub4, table_mappers[3], id_master_ids,id_master_created_times)
                self.temp_dataframes.extend([df_ub1, df_ub2, df_ub3, df_ub4])

            else:
                logger.warning(f"Unexpected column mapping: {len(column_mapping)}")

            logger.info(f"Successfully processed data for category: {category_name}")
        except Exception as e:
            session.rollback()
            logger.error(f"Error processing category {category_name}: {e}", exc_info=True)
            raise  # Re-raise the exception

    def process_csv_files(self, data_dir, category_name, all_dataframes):
        # Get all CSV files in the directory
        files = list(Path(data_dir).glob("**/*.csv"))
        # current_date = datetime.now().strftime(DATE_FORMAT)
        current_date = "20250325"
        logger.info(f"Processing CSV files in {data_dir} for category {category_name}")

        for file_path in files:
            if current_date not in file_path.name:
                continue
            try:
                # Read and process CSV file
                df = self.data_processor.read_and_process_csv(file_path, category_name)
                if df is not None:
                    # Convert '収集日時' to datetime and then format it to '%H:%M'
                    df['収集日時'] = pd.to_datetime(df['収集日時'], errors='coerce')

                    # Now format '収集日時' to '%Y/%m/%d %H:%M'
                    df['収集日時'] = df['収集日時'].dt.strftime('%Y/%m/%d %H:%M')
                    all_dataframes.append(df)
            except Exception as e:
                logger.error(f"Error processing file {file_path.name}: {e}", exc_info=True)

    def process_directory(self, category_name, all_dataframes):
        """Process directories based on category (e.g. SM, Door, under body, andon, ndai)."""
        round_num = self.folder_manager.get_folder_round_name()
        if category_name in UB_DOOR_SM_CATEGORIES:
            data_category_dir = os.path.join(self.root_dir, category_name, round_num)

            if os.path.exists(data_category_dir) and os.path.isdir(data_category_dir):
                is_files_exist = self.folder_manager.check_files_exist_in_category(self.root_dir, category_name,
                                                                                   round_num)
                if not is_files_exist:
                    logger.error(f"Directory enough nunber files csv")
                    return
                self.process_csv_files(data_category_dir, category_name, all_dataframes)

            else:
                logger.error(f"Directory {data_category_dir} does not exist or is not a directory.")
                   
            time.sleep(1)
            # Andon and ndai don
        else:
            data_category_dir = os.path.join(self.root_dir, category_name)
            is_files_exist = self.folder_manager.check_files_exist_in_category(self.root_dir, category_name,
                                                                               round_num)
            if not is_files_exist:
                return
            self.process_csv_files(data_category_dir, category_name, all_dataframes)
            logger.info(f"Processing directory: {data_category_dir}")

    def cleanup_temporary_dataframes(self):
        """Clean up all temporary DataFrames"""
        try:
            logger.info(f"Cleaning up {len(self.temp_dataframes)} temporary DataFrames...")
            for df in self.temp_dataframes:
                del df
            self.temp_dataframes.clear()
            gc.collect()
            logger.info("Temporary DataFrames cleanup completed")
        except Exception as e:
            logger.error(f"Error during DataFrame cleanup: {e}", exc_info=True)

    def main(self):
        try:
            # check time break before process
            timenow = datetime.now().strftime(TIME_FORMAT)
            # timenow = "07:00"
            round_number, is_morning = round_and_is_morning_mapping(timenow)
            if round_number == 0 and is_morning == 0:
                logger.warning("休暇時間中")
                categories = self.folder_manager.check_folder_type()
                self.database_manager.processed_created_at.clear()
                # delete all file csv in folder because time break
                if categories:
                    for category in categories:
                        data_category_dir = os.path.join(self.root_dir, category)
                        self.folder_manager.delete_csv_files_in_directory(data_category_dir)
                return
            else:
                logger.info(f"Processing data for round: {round_number}, is_morning: {is_morning}")
                # Get categories from folder manager
                categories = self.folder_manager.check_folder_type()

                if not categories:
                    logger.warning("No valid categories found. Exiting.")
                    return
                
                all_dataframes = []
                # Collect dataframes
                for category in categories:
                    self.process_directory(category, all_dataframes)

                # If no valid dataframes are collected, exit
                if not all_dataframes:
                    logger.warning("No valid dataframes found to process. Exiting.")
                    return

                merged_df = reduce(lambda left, right: pd.merge(left, right, on='収集日時', how='inner'), all_dataframes)
                merged_df['収集日時'] = pd.to_datetime(merged_df['収集日時'], format='%Y/%m/%d %H:%M', errors='coerce')

                # Check if merged_df is empty
                if merged_df.empty:
                    logger.warning("Merged DataFrame is empty. Skipping database insertion.")
                    return

                # Extract components from '収集日時'
                merged_df['hour_minute'] = merged_df['収集日時'].dt.strftime('%H:%M')
                merged_df['year'] = merged_df['収集日時'].dt.year
                merged_df['month'] = merged_df['収集日時'].dt.month
                merged_df['day'] = merged_df['収集日時'].dt.day
                merged_df['hour'] = merged_df['収集日時'].dt.hour
                merged_df['minute'] = merged_df['収集日時'].dt.minute

                # Add additional columns
                merged_df['update_time'] = datetime.now()
                merged_df['delete_flag'] = 0
                
                # Assume round_info is processed properly elsewhere
                round_info = self.data_processor.get_round_info_for_all_times(merged_df)
                merged_df = pd.merge(merged_df, round_info, on='hour_minute', how='inner')
                
                # Output to CSV
                # merged_df.to_csv('merged_df_add_ndai.csv', index=False, encoding="shift-jis")
                # logger.info("Merged data saved to 'merged_df.csv'")
                session = self.database_manager.connect_to_db()

                if session is None:
                    logger.error("Failed to connect to the database.")
                    return
                try:
                    session.begin()  # Start explicit transaction
                    logger.info("Starting explicit transaction.")


                    df_id_master =  merged_df[id_master_columns]
                    id_master_ids,id_master_created_times = self.database_manager.insert_id_master_data(session, df_id_master)
                    # only get row in merged_df['収集日時'] has value in id_master_created_times
                    merged_df_filtered = merged_df[merged_df['収集日時'].isin(id_master_created_times)]
                    if merged_df_filtered.empty:
                        logger.warning("No valid data found to process. Exiting.")
                        return
                    round_master = merged_df_filtered[round_master_columns]
                    round_mst_mapper = RoundMasterMapper()
                    round_master = [round_mst_mapper.map_to_fields(row) for idx, row in round_master.iterrows()]
                    session.add_all(round_master)
                    session.flush() 
                    # Now, categorize and process data by category
                    for category_name in categories:
                        table_mappers = tabel_names_mapper(category_name)
                        if table_mappers and id_master_ids and id_master_created_times:
                            # Process data by all category
                            self.process_category_data(merged_df_filtered , category_name, table_mappers, session,id_master_ids,id_master_created_times)
                    session.commit()  # Commit if all successful
                    logger.info("Data processing completed successfully. Committing transaction.")
                    # #  free memory
                    self.cleanup_temporary_dataframes()
                    del merged_df
                    del round_master
                    del round_info
                    del id_master_ids,id_master_created_times
                    del categories
                    gc.collect()

                except Exception as e:
                    session.rollback()  # Rollback if any error occurs
                    logger.error(f"Error processing data, rolling back transaction: {e}", exc_info=True)
                    raise  # Re-raise the exception
                finally:
                    session.close()
                    logger.info("Session closed.")

        except Exception as e:
           logger.error(f"A error: {e}", exc_info=True)
    # Add new method for scheduled execution
    def scheduled_execution(self):
        start_time = time.time()
        logger.info("Starting scheduled execution...")
        self.main()

        execution_time = time.time() - start_time

        logger.info(f"Scheduled execution completed in {execution_time:.2f} seconds")

    def stop(self):
        self.is_running = False
        logger.info("Stopping application...")

    def run_scheduler(self):
        try:
            # Schedule the job to run every 20 seconds
            schedule.every(10).seconds.do(self.scheduled_execution)
            logger.info("Scheduler started - running every 10 seconds")
            
            # Keep running until stop is called
            while self.is_running:
                schedule.run_pending()
                time.sleep(1)

        except KeyboardInterrupt:
            logger.info("Received keyboard interrupt, shutting down...")
            self.stop()
        except Exception as e:
            logger.error(f"Error in scheduler: {e}", exc_info=True)
            self.stop()
        finally:
            logger.info("Scheduler stopped")

if __name__ == "__main__":
    try:
        root_dir = "C:\\Users\\nguyen-duy-phong\\Downloads\\infura_data\\0322andon\\新しいフォルダー"
        # root_dir = "C:\\Users\\nguyen-duy-phong\\Downloads\\infura_data\\0325data\\0325data"
        app = MainApp(root_dir)
        # Start the scheduler
        app.run_scheduler()
        # app.main()

    except Exception as e:
        logger.error(f"Application error: {e}", exc_info=True)
        sys.exit(1)