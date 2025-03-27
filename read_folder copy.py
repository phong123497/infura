import os
from functools import reduce
from pathlib import Path
from typing import Any
from datetime import datetime
import pandas as pd
from sqlalchemy.orm import sessionmaker, Session
from mapper.door_mapper import DoorPageData1Mapper, DoorPageData2Mapper
from mapper.under_body_mapper import UnderBodyPageData1Mapper, UnderBodyPageData2Mapper, UnderBodyPageData3Mapper
from enties.master_no_check import RoundMasterMapperNoCheck, IdMaster
from sqlalchemy import create_engine
from SQL.mapper.round_mapping import round_and_is_morning_mapping, get_round_times
from SQL.mapper.columns_mapping import (round_master_columns, door1_columns, door2_columns,
                                   under_body1_columns, under_body2_columns, under_body3_columns,
                                   sm_page_data1_columns, sm_page_data2_columns)
import logging

# Cấu hình logging
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

def check_folder_type(root_dir):
    folder_categories = os.listdir(root_dir)
    expected_categories = ["SM", "ドア", "UB", "Andon", "Ndai"]
    result_categories = []
    for category in folder_categories:
        if category in expected_categories:
            logging.info(f"Found category: {category}")
            result_categories.append(category)
        else:
            logging.warning(f"Unexpected category found: {category}. Skipping.")
            return None
    return result_categories


def check_folder_round(root_dir, category_name):
    category_name_path = os.path.join(root_dir, category_name)
    folders = os.listdir(category_name_path)
    result_round = []
    for folder in folders:
        if "ラウンド" in folder:
            logging.info(f"Found round: {folder} in category {category_name}")
            result_round.append(folder)
        else:
            logging.warning(f"Unexpected folder found: {folder} in category {category_name}. Skipping.")
    return result_round


def process_directory(root_dir, category_name):
    """ (SM, Door, under body)."""
    rounds = check_folder_round(root_dir, category_name)
    if rounds:
        for round_name in rounds:
            data_category_dir = os.path.join(root_dir, category_name, round_name)
            if os.path.exists(data_category_dir) and os.path.isdir(data_category_dir):
                process_csv_files(data_category_dir, category_name)
            else:
                logging.error(f"Directory {data_category_dir} does not exist or is not a directory.")
 
    

def tabel_names_mapper(category_name):
    if category_name == "ドア":
        return DoorPageData1Mapper, DoorPageData2Mapper
    elif category_name == "UB":
        return UnderBodyPageData1Mapper, UnderBodyPageData2Mapper, UnderBodyPageData3Mapper
    elif category_name == "SM":  # Added for SM
        return None  # Replace with SM mappers if available
    return None


def process_column_names(df):
    new_columns = []

    for col in df.columns[1:]:
        new_col_name = col[5:-2]
        new_columns.append(new_col_name)

    # rename col in DataFrame 
    df.columns = [df.columns[0]] + new_columns  # first column doesn't change
    return df


def read_and_process_csv(file_path):
    try:
        df = pd.read_csv(file_path, encoding="shift-jis", skiprows=[1])
        df = process_column_names(df)
        logging.info(f"Successfully read and processed CSV file: {file_path}")
        return df
    except Exception as e:
        logging.error(f"Error processing {file_path}: {str(e)}", exc_info=True)
        return None  # Handle error properly


def process_csv_files(data_dir, category_name):
    # get data_dit name
    parent_dir = os.path.dirname(data_dir)
    folder_name = os.path.basename(data_dir)
    parent_folder_name = os.path.basename(parent_dir)
    output_file = f'merged_df_for{parent_folder_name}{folder_name}.csv'
    files = list(Path(data_dir).glob("**/*.csv"))
    current_date = datetime.now().strftime('%Y%m%d')
    logging.info(f"Processing CSV files in {data_dir} for category {category_name}")
    dataframes = []
    for file_path in files:
        file_name = file_path.name
        if current_date not in file_name:
            df = read_and_process_csv(file_path)
            if df is not None:
                dataframes.append(df)

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

            # Thêm các cột cố định
            merged_df['update_time'] = datetime.now()
            merged_df['delete_flag'] = False
            merged_df['round_update'] = False
            round_info = get_round_info_for_all_times(merged_df)

            merged_df = pd.merge(merged_df, round_info, on='hour_minute', how='inner')
            round_master = merged_df[round_master_columns]
            # merged_df.to_csv(output_file,  encoding="shift-jis",index=False)
            table_mappers = tabel_names_mapper(category_name)
            if table_mappers:
                session = connect_to_db()

                try:
                    session.begin()  # Start explicit transaction
                    logging.info("Starting explicit transaction.")

                    round_master = merged_df[round_master_columns]
                    round_mst_no_check = RoundMasterMapperNoCheck()
                    round_master = [round_mst_no_check.map_to_fields(row) for idx, row in round_master.iterrows()]
                    session.add_all(round_master)
                    session.flush()  # Flush to get generated IDs

                    if category_name == "ドア":
                        process_door_data(merged_df, table_mappers, session)
                    elif category_name == "UB":
                        process_under_body_data(merged_df, table_mappers, session)
                    elif category_name == "SM":
                        process_sm_data(merged_df, table_mappers, session)

                    session.commit()  # Commit if all successful
                    logging.info("Data processing completed successfully. Committing transaction.")

                except Exception as e:
                    session.rollback()  # Rollback if any error occurs
                    logging.error(f"Error processing data, rolling back transaction: {e}", exc_info=True)

                finally:
                    session.close()
                    logging.info("Session closed.")
        except Exception as e:
             logging.error(f"Failed to process dataframe: {e}", exc_info=True)
    else:
        logging.warning("File must be more than one, skipping")


def insert_model_data(session, df, table_mapper):
    try:
        model_instances = df.apply(lambda row: table_mapper().map_to_model(row), axis=1)
        session.add_all(model_instances)
        session.flush()  # Flush to make sure it will affect to DB
        logging.info(f"Successfully inserted model data using {table_mapper.__name__}")

    except Exception as e:
        session.rollback()
        logging.error(f"Error inserting model data using {table_mapper.__name__}: {e}", exc_info=True)
        raise e


def insert_id_master_data(session, df, table_name):
    try:
        id_master_instances = df.apply(lambda row: map_to_id_master(row, table_name=table_name), axis=1)
        session.add_all(id_master_instances)
        session.flush()  # Flush to make sure it will affect to DB
        logging.info(f"Successfully inserted id_master data for {table_name}")

    except Exception as e:
        session.rollback()
        logging.error(f"Error inserting id_master data for {table_name}: {e}", exc_info=True)
        raise e


def process_door_data(merged_df, table_mappers, session):
    try:
        df_door1 = merged_df[door1_columns]
        df_door2 = merged_df[door2_columns]
        door1_table_name = 'door_page_data1'
        door2_table_name = 'door_page_data2'

        insert_id_master_data(session, df_door1, door1_table_name)
        insert_id_master_data(session, df_door2, door2_table_name)

        insert_model_data(session, df_door1, table_mappers[0])
        insert_model_data(session, df_door2, table_mappers[1])
        logging.info("Successfully processed door data.")

    except Exception as e:
        session.rollback()
        logging.error(f"Error processing door data: {e}", exc_info=True)
        raise e


def process_under_body_data(merged_df, table_mappers, session):
    try:
        df_under_body1 = merged_df[under_body1_columns]
        df_under_body2 = merged_df[under_body2_columns]
        df_under_body3 = merged_df[under_body3_columns]

        insert_id_master_data(session, df_under_body1, 'under_body_page_data1')
        insert_id_master_data(session, df_under_body2, 'under_body_page_data2')
        insert_id_master_data(session, df_under_body3, 'under_body_page_data3')

        insert_model_data(session, df_under_body1, table_mappers[0])
        insert_model_data(session, df_under_body2, table_mappers[1])
        insert_model_data(session, df_under_body3, table_mappers[2])
        logging.info("Successfully processed under body data.")

    except Exception as e:
        session.rollback()
        logging.error(f"Error processing under body data: {e}", exc_info=True)
        raise e


def process_sm_data(merged_df, table_mappers, session):
    try:
        if table_mappers is None:
            logging.warning("No table mappers available for SM data.")
            return

        df_sm1 = merged_df[sm_page_data1_columns]
        df_sm2 = merged_df[sm_page_data2_columns]
        sm_name1 = 'sm_page_data1'
        sm_name2 = 'sm_page_data2'

        insert_id_master_data(session, df_sm1, sm_name1)
        insert_id_master_data(session, df_sm2, sm_name2)

        insert_model_data(session, df_sm1, table_mappers[0])
        insert_model_data(session, df_sm2, table_mappers[1])
        logging.info("Successfully processed SM data.")

    except Exception as e:
        session.rollback()
        logging.error(f"Error processing SM data: {e}", exc_info=True)
        raise e


def connect_to_db():
    try:
        engine = create_engine('postgresql://postgres:12345@localhost:5432/test_db')
        Session = sessionmaker(bind=engine)
        session = Session()
        logging.info("Successfully connected to the database.")
        return session
    except Exception as e:
        logging.error(f"Error connecting to the database: {e}", exc_info=True)
        return None  # Return None if the session cannot be created


def map_to_id_master(row, table_name='under_body_page_data3'):
    try:
        created_at_value = pd.to_datetime(row['収集日時'], format='%Y/%m/%d %H:%M', errors="coerce")
        id_master_instance = IdMaster(
            table_name=table_name,
            created_at=created_at_value,
            delete_flag=False
        )
        logging.debug(f"Successfully mapped row to IdMaster for table {table_name}")
        return id_master_instance

    except Exception as e:
        logging.error(f"Error mapping row to IdMaster for table {table_name}: {e}", exc_info=True)
        raise e


def get_round_info_for_all_times(merged_df):
    round_info = []
    try:
        for time_input in merged_df['hour_minute']:
            round_number, is_morning = round_and_is_morning_mapping(time_input)
            start_time, end_time = get_round_times(round_number, is_morning)
            round_info.append({
                'round_number': round_number,
                'is_morning': is_morning,
                'hour_minute': time_input,
                'start_time': start_time,
                'end_time': end_time
            })
        logging.debug("Successfully retrieved round information for all times.")
    except Exception as e:
        logging.error(f"Error retrieving round information: {e}", exc_info=True)
        raise e
    result_df = pd.DataFrame(round_info)
    return result_df


def main():
    root_dir = "C:\\Users\\nguyen-duy-phong\\Downloads\\infura_data\\0314"
    categories = check_folder_type(root_dir)
    if categories:
        for category in categories:
            process_directory(root_dir, category)


if __name__ == "__main__":
    main()