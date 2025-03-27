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
from mapper.andon_mapper import AndonPageDataMapper
from mapper.ndai_mapper import NdaiPageDataMapper
from enties.master_no_check import RoundMasterMapperNoCheck
from mapper.round_mapping import round_and_is_morning_mapping
from mapper.columns_mapping import (id_master_columns, common_columns, round_master_columns, door1_columns, door2_columns,
                                   under_body1_columns, under_body2_columns, under_body3_columns,
                                   sm_page_data1_columns, sm_page_data2_columns, andon_page_data_columns, ndai_page_data_columns)
import schedule
import time
import sys



def tabel_names_mapper(category_name):
    if category_name == "ドア":
        return DoorPageData1Mapper, DoorPageData2Mapper
    elif category_name == "UB":
        return UnderBodyPageData1Mapper, UnderBodyPageData2Mapper, UnderBodyPageData3Mapper
    elif category_name == "SM": 
        return SmPageData1Mapper, SmPageData2Mapper
    elif category_name == "Andon": 
        return AndonPageDataMapper # 
    elif category_name == "Ndai": 
        return NdaiPageDataMapper 
    return None

class MainApp:
    def __init__(self, root_dir):
        self.root_dir = root_dir
        self.folder_manager = FolderManager(self.root_dir)
        self.data_processor = DataProcessor()
        self.database_manager = DatabaseManager()
        self.is_running = True

    def process_andon_data(self, merged_df, table_mappers, session, id_master_ids,id_master_created_times):
        try:
            missing_columns_andon = [col for col in andon_page_data_columns if col not in merged_df.columns]
            if missing_columns_andon:
                andon_df = merged_df[common_columns]
                # logger.warning(f"Columns missing in door1_columns: {', '.join(missing_columns_door1)}. Using common_columns instead.")
            else:
                andon_df = merged_df[andon_page_data_columns]
            
            self.database_manager.insert_model_data(session, andon_df, table_mappers, id_master_ids, id_master_created_times)
            logger.info("Successfully processed andon data .")

        except Exception as e:
            session.rollback()
            logger.error(f"Error processing ndai data: {e}", exc_info=True)
            raise
    def process_ndai_data(self, merged_df, table_mappers, session, id_master_ids,id_master_created_times):
        try:
            missing_columns_ndai = [col for col in ndai_page_data_columns if col not in merged_df.columns]
            if missing_columns_ndai:
                ndai_df = merged_df[common_columns]
                # logger.warning(f"Columns missing in door1_columns: {', '.join(missing_columns_door1)}. Using common_columns instead.")
            else:
                ndai_df = merged_df[ndai_page_data_columns]
            self.database_manager.insert_model_data(session, ndai_df, table_mappers, id_master_ids, id_master_created_times)
            logger.info("Successfully processed ndai data .")

        except Exception as e:
            session.rollback()
            logger.error(f"Error processing ndai data: {e}", exc_info=True)
            raise
        
        
    def process_door_data(self, merged_df, table_mappers, session, id_master_ids, id_master_created_times):
        try:
            missing_columns_door1 = [col for col in door1_columns if col not in merged_df.columns]
            # columns_door1_in_mergedf = [col for col in door1_columns if col in merged_df.columns]
            if missing_columns_door1:
                df_door1 = merged_df[common_columns ]
                # logger.warning(f"Columns missing in door1_columns: {', '.join(missing_columns_door1)}. Using common_columns instead.")
            else:
                df_door1 = merged_df[door1_columns]

            missing_columns_door2 = [col for col in door2_columns if col not in merged_df.columns]
            
            if missing_columns_door2:
                df_door2 = merged_df[common_columns]
                # logger.warning(f"Columns missing in door2_columns: {', '.join(missing_columns_door2)}. Using common_columns instead.")
            else:
                df_door2 = merged_df[door2_columns]

            self.database_manager.insert_model_data(session, df_door1, table_mappers[0], id_master_ids, id_master_created_times)
            self.database_manager.insert_model_data(session, df_door2, table_mappers[1], id_master_ids, id_master_created_times) # slice to adjust index
            
            logger.info("Successfully processed door data.")

        except Exception as e:
            session.rollback()
            logger.error(f"Error processing door data: {e}", exc_info=True)
            raise
        
    def process_under_body_data(self, merged_df, table_mappers, session,id_master_ids,id_master_created_times):
        try:
            missing_columns_ub1 = [col for col in under_body1_columns if col not in merged_df.columns]
            if missing_columns_ub1:
                df_under_body1 = merged_df[common_columns]
                # logger.warning(f"Columns missing in ub1_columns: {', '.join(missing_columns_ub1)}. Using common_columns instead.")
            else:
                df_under_body1 = merged_df[under_body1_columns]
                
            missing_columns_ub2 = [col for col in under_body2_columns if col not in merged_df.columns]
            if missing_columns_ub2:
                df_under_body2 = merged_df[common_columns]
                # logger.warning(f"Columns missing in ub2_columns: {', '.join(missing_columns_ub2)}. Using common_columns instead.")
            else:
                df_under_body2 = merged_df[under_body2_columns]
                
            missing_columns_ub3 = [col for col in under_body3_columns if col not in merged_df.columns]
                
            if missing_columns_ub3:
                df_under_body3 = merged_df[common_columns]
                # logger.warning(f"Columns missing in ub3_columns: {', '.join(missing_columns_ub3)}. Using common_columns instead.")
            else:
                df_under_body3 = merged_df[under_body2_columns]

            
            self.database_manager.insert_model_data(session, df_under_body1, table_mappers[0], id_master_ids,id_master_created_times)
            self.database_manager.insert_model_data(session, df_under_body2, table_mappers[1], id_master_ids,id_master_created_times)
            self.database_manager.insert_model_data(session, df_under_body3, table_mappers[2], id_master_ids,id_master_created_times)
            logger.info("Successfully processed under body data.")

        except Exception as e:
            session.rollback()
            logger.error(f"Error processing under body data: {e}", exc_info=True)
            raise

    def process_sm_data(self, merged_df, table_mappers, session,id_master_ids,id_master_created_times):
        try:
            if table_mappers is None:
                logger.warning("No table mappers available for SM data.")
                return  
            
            missing_columns_sm1 = [col for col in sm_page_data1_columns if col not in merged_df.columns]
            if missing_columns_sm1:
                df_sm1 = merged_df[common_columns]
                # logger.warning(f"Columns missing in sm1_columns: {', '.join(missing_columns_sm1)}. Using common_columns instead.")
            else:
                df_sm1 = merged_df[sm_page_data1_columns]
                
            missing_columns_sm2 = [col for col in sm_page_data2_columns if col not in merged_df.columns]
            if missing_columns_sm2:
                df_sm2 = merged_df[common_columns]
                # logger.warning(f"Columns missing in sm2_columns: {', '.join(missing_columns_sm2)}. Using common_columns instead.")
            else:
                df_sm2 = merged_df[sm_page_data2_columns]
           
            self.database_manager.insert_model_data(session, df_sm1, table_mappers[0], id_master_ids ,id_master_created_times)
            self.database_manager.insert_model_data(session, df_sm2, table_mappers[1], id_master_ids, id_master_created_times)
            logger.info("Successfully processed SM data.")

        except Exception as e:
            session.rollback()
            logger.error(f"Error processing SM data: {e}", exc_info=True)
            raise

    def process_csv_files(self, data_dir, category_name, all_dataframes):
        # Get all CSV files in the directory
        files = list(Path(data_dir).glob("**/*.csv"))
        # current_date = datetime.now().strftime('%Y%m%d')
        current_date = "20250322"
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
        round_num  = self.folder_manager.get_folder_round_name(root_dir, category_name)
        if category_name in ["SM", "UB", "ドア"]: 
            data_category_dir = os.path.join(self.root_dir, category_name, round_num)
            
            if os.path.exists(data_category_dir) and os.path.isdir(data_category_dir):
                is_files_exist = self.folder_manager.check_files_exist_in_category(self.root_dir, category_name,round_num)
                if not is_files_exist:
                    logger.error(f"Directory enough nunber files csv")
                    time.sleep(1)
                    return
                self.process_csv_files(data_category_dir, category_name, all_dataframes)
                
            else:
                logger.error(f"Directory {data_category_dir} does not exist or is not a directory.")
        
            # Andon and ndai don
        else: 
            data_category_dir = os.path.join(self.root_dir, category_name)
            is_files_exist = self.folder_manager.check_files_exist_in_category(self.root_dir, category_name,round_num)
            if not is_files_exist:
                return
            self.process_csv_files(data_category_dir, category_name, all_dataframes)
            logger.info(f"Processing directory: {data_category_dir}")
        

    def main(self):
        try:
            # check time break before process
            timenow = datetime.now().strftime("%H:%M")
            # timenow = "19:21"
            round_number, is_morning=  round_and_is_morning_mapping(timenow)
            if round_number == 0 and is_morning == 0:
                logger.warning("休暇時間中")
                categories = self.folder_manager.check_folder_type()
                # delete all file csv in folder because time break  
                if categories:
                    for category in categories:
                        data_category_dir = os.path.join(self.root_dir, category)
                        self.folder_manager.delete_csv_files_in_directory(data_category_dir)

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
                
                # Merge with round_info if necessary
                merged_df = pd.merge(merged_df, round_info, on='hour_minute', how='inner')
                
                # Output to CSV
                # merged_df.to_csv('merged_df_add_ndai.csv', index=False, encoding="shift-jis")
                # # logger.info("Merged data saved to 'merged_df.csv'")
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

                    id_master =  merged_df[id_master_columns]
                    
                    id_master_ids,id_master_created_times = self.database_manager.insert_id_master_data(session, id_master)
                    
                    # Now, categorize and process data by category
                    for category_name in  categories:
                        table_mappers = tabel_names_mapper(category_name)
                        if table_mappers:
                            # Get only the Ids related to the number of rows for this category
                            if category_name == "ドア":
                                self.process_door_data(merged_df, table_mappers, session, id_master_ids, id_master_created_times )
                            elif category_name == "UB":
                                self.process_under_body_data(merged_df, table_mappers, session, id_master_ids, id_master_created_times)
                            elif category_name == "SM":
                                self.process_sm_data(merged_df, table_mappers, session, id_master_ids, id_master_created_times)
                            if category_name == "Andon":
                                self.process_andon_data(merged_df, table_mappers, session, id_master_ids, id_master_created_times)
                            if category_name == "Ndai":
                                self.process_ndai_data(merged_df, table_mappers, session, id_master_ids, id_master_created_times)
                            
                    session.commit()  # Commit if all successful
                    logger.info("Data processing completed successfully. Committing transaction.")
                    for category in categories:
                        data_category_dir = os.path.join(self.root_dir, category)
                        self.folder_manager.delete_csv_files_in_directory(data_category_dir)
                        logger.info(f"Successfully deleted CSV files in {data_category_dir} after successful insertion.")
                except Exception as e:
                    session.rollback()  # Rollback if any error occurs
                    logger.error(f"Error processing data, rolling back transaction: {e}", exc_info=True)
                    raise # Re-raise the exception
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
        # root_dir = "C:\\Users\\nguyen-duy-phong\\Downloads\\infura_data\\0322andon\\test_deletefiles"
        root_dir = "C:\\Users\\nguyen-duy-phong\\Downloads\\infura_data\\0325data\\0325data"
        app = MainApp(root_dir)
        # Start the scheduler
        app.run_scheduler()

    except Exception as e:
        logger.error(f"Application error: {e}", exc_info=True)
        sys.exit(1)