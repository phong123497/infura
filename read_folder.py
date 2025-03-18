import os
import re  # Import thư viện regular expression
import sys
from functools import reduce
from pathlib import Path
from typing import Any
from datetime import datetime
import pandas as pd
from mapper.door_mapper import DoorPageData1Mapper, DoorPageData2Mapper
from sqlalchemy.orm import sessionmaker
from mapper.under_body_mapper import UnderBodyPageData1Mapper, UnderBodyPageData2Mapper, UnderBodyPageData3Mapper
from enties.master_no_check import  RoundMasterMapperNoCheck ,IdMaster
from sqlalchemy import create_engine
from mapper.rount_mapping import round_and_is_morning_mapping , get_round_times
from mapper.column_mapping import (round_master_columns, door1_columns, door2_columns,
                                   under_body1_columns,under_body2_columns, under_body3_columns,
                                   sm_page_data1_columns, sm_page_data2_columns)       
from mapper.under_body_mapper import UnderBodyPageData1Mapper, UnderBodyPageData2Mapper, UnderBodyPageData3Mapper

# アプリケーションのベースパスを取得
# if getattr(sys, "frozen", False):
#     ROOT_DIR = Path(sys._MEIPASS)
# else:
#     ROOT_DIR = Path(__file__).parent.parent

def check_folder_type(root_dir):
    folder_categories = os.listdir(root_dir)
    expected_categories = ["SM", "ドア", "UB"]
    result_categories = []
    for category in folder_categories:
        if category in expected_categories:
            print("category", category)
            result_categories.append(category)
        else:
            print("must be SM, ドア, or UB")
            return None
    return result_categories

def check_folder_round(root_dir, category_name):
    category_name_path = os.path.join(root_dir, category_name)
    folders = os.listdir(category_name_path)
    result_round = []
    for folder in folders:
        if "ラウンド" in folder:
            result_round.append(folder)
        else:
            print("round not found, check again")
    return result_round

def process_directory(root_dir, category_name):
    """Xử lý một thư mục (SM, Door, under body)."""
    rounds = check_folder_round(root_dir, category_name)
    for round_name in rounds:
        data_category_dir = os.path.join(root_dir, category_name, round_name)
        if os.path.exists(data_category_dir) and os.path.isdir(data_category_dir):
            process_csv_files(data_category_dir, category_name)


def tabel_names_mapper(category_name):
    if category_name == "ドア":
        return DoorPageData1Mapper, DoorPageData2Mapper
    elif category_name == "UB":
        return UnderBodyPageData1Mapper, UnderBodyPageData2Mapper, UnderBodyPageData3Mapper
    # elif category_name == "SM":
    #     return 
    return None


def process_column_names(df):
    new_columns = []
    
    for col in df.columns[1:]:  
        new_col_name = col[5:-2]
        new_columns.append(new_col_name)
    
    # Cập nhật lại tên cột trong DataFrame
    df.columns = [df.columns[0]] + new_columns  # Giữ cột đầu tiên không thay đổi
    return df
def process_csv_files(data_dir, category_name):
    # get data_dit name
    parent_dir = os.path.dirname(data_dir)
    folder_name = os.path.basename(data_dir)
    parent_folder_name = os.path.basename(parent_dir)
    output_file = f'merged_df_for{parent_folder_name}{folder_name}.csv'
    files = list(Path(data_dir).glob("**/*.csv"))
    current_date = datetime.now().strftime('%Y%m%d')
    print("current date", current_date) 
    dataframes = []
    for file_path in files:
        file_name = file_path.name
        if current_date not in file_name:
            df = pd.read_csv(file_path, encoding="shift-jis", skiprows=[1])
            df = process_column_names(df)
            dataframes.append(df)
    if len(dataframes) > 1:
        merged_df = dataframes[0]
        # for df in dataframes[1:]:
        #     merged_df = pd.merge(merged_df, df, on='収集日時', how='inner')
        
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
             
             # check exception at here if round_master_columns is an valid key 
            round_master = merged_df[round_master_columns] 
            round_mst_no_check = RoundMasterMapperNoCheck()   
            round_master =  [round_mst_no_check.map_to_fields(row) for idx, row in round_master.iterrows()]
            session.add_all(round_master)
            
            if category_name == "ドア":
                # Lấy các cột tương ứng
                df_door1 = merged_df[door1_columns]
                df_door2 = merged_df[door2_columns]

                # Tạo các bản ghi id_master và model instance cho door1 và door2
                door1_table_name = 'door_page_data1'
                door2_table_name = 'door_page_data2'

                # insert data to id_master
                id_master_instances = [map_to_id_master(row, table_name=door1_table_name) for index, row in df_door1.iterrows()]
                id_master_instances += [map_to_id_master(row, table_name=door2_table_name) for index, row in df_door2.iterrows()]
                session.add_all(id_master_instances)

                # insrt data to door
                model_instances = [table_mappers[0]().map_to_model(row) for index, row in df_door1.iterrows()]
                model_instances += [table_mappers[1]().map_to_model(row) for index, row in df_door2.iterrows()]
                session.add_all(model_instances)
            elif category_name == "UB":
                df_under_body1 = merged_df[under_body1_columns]
                df_under_body2 = merged_df[under_body2_columns]
                df_under_body3 = merged_df[under_body3_columns]

                under_body_name1 = 'under_body_page_data1'
                under_body_name2 = 'under_body_page_data2'
                under_body_name3 = 'under_body_page_data3'
                id_master_instances = [map_to_id_master(row, table_name=under_body_name1) for index, row in df_under_body1.iterrows()]
                id_master_instances += [map_to_id_master(row, table_name=under_body_name2) for index, row in df_under_body2.iterrows()]
                id_master_instances += [map_to_id_master(row, table_name=under_body_name3) for index, row in df_under_body3.iterrows()]
                session.add_all(id_master_instances)
                # insert to under_body
                model_instances = [table_mappers[0]().map_to_model(row) for index, row in df_under_body1.iterrows()]
                model_instances += [table_mappers[1]().map_to_model(row) for index, row in df_under_body2.iterrows()]
                model_instances += [table_mappers[2]().map_to_model(row) for index, row in df_under_body3.iterrows()]
            elif category_name == "SM":
                df_sm1 = merged_df[sm_page_data1_columns]
                df_sm2 = merged_df[sm_page_data2_columns]

                sm_name1 = 'sm_page_data1'
                sm_name2 = 'sm_page_data2'
                id_master_instances = [map_to_id_master(row, table_name=sm_name1) for index, row in df_sm1.iterrows()]
                id_master_instances += [map_to_id_master(row, table_name=sm_name2) for index, row in df_sm2.iterrows()]
                session.add_all(id_master_instances)

                # insrt data to door
                model_instances = [table_mappers[0]().map_to_model(row) for index, row in df_sm1.iterrows()]
                model_instances += [table_mappers[1]().map_to_model(row) for index, row in df_sm2.iterrows()]
            session.commit()
            session.close()
    else:
        print("file must be more than one")


def connect_to_db():
    try:
        engine = create_engine('postgresql://postgres:12345@localhost:5432/test_db')
        Session = sessionmaker(bind=engine)
        session = Session()
        return session
    except Exception as e:
        print(f"Error connecting to the database: {e}")
    return session

def map_to_id_master(row , table_name='under_body_page_data3'):
    created_at_value = pd.to_datetime(row['収集日時'], format='%Y/%m/%d %H:%M', errors="coerce")
    id_master_instance = IdMaster(
        table_name= table_name,  
        created_at=created_at_value,   
        delete_flag=False              
    )
    return id_master_instance

def get_round_info_for_all_times(merged_df):
    round_info = []

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





