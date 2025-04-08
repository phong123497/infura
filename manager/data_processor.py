import pandas as pd
from datetime import datetime
from .logging_config import logger
from util.round_relate import round_and_is_morning_mapping, get_round_times, check_round_update
from util.constants import (
    CATEGORY_DOOR, CATEGORY_UB, CATEGORY_SM, CATEGORY_ANDON, CATEGORY_NDAI,
    DAISU, SHOKUSEI_YOBIDASHI, UB_DOOR_SM_CATEGORIES,
    START_TIME_AM, END_TIME_AM, END_TIME_PM
)
class DataProcessor:
 
    def process_column_names(self, df, category_name):
        new_columns = []
        # df = df.fillna(0)
        if category_name  == CATEGORY_UB:
            end_index = -2
            suffix = "_ub"
        elif category_name  == CATEGORY_DOOR:
            end_index = -2
            suffix = "_door"
        elif category_name == CATEGORY_SM:
            end_index = None
            suffix = "_sm"
        elif category_name == CATEGORY_ANDON:
            end_index = None
            suffix = "_andon"
        elif category_name  == CATEGORY_NDAI:
            end_index = None
            suffix = "_ndai"
        for col in df.columns[1:]:
            new_col_name = col[5:end_index]
            new_col_name += suffix
            new_columns.append(new_col_name)
        df.columns = [df.columns[0]] + new_columns  
        return df
   
    def divide_100_convert_int( self, df_cleaned, category_name):
        try:
            if category_name in UB_DOOR_SM_CATEGORIES: 
                df_cleaned = df_cleaned.fillna(0) 
                for col in df_cleaned.columns[1:]:
                    if DAISU not in col and SHOKUSEI_YOBIDASHI not in col:
                        # df[col] = pd.to_numeric(df[col], errors='coerce')
                        df_cleaned.loc[:, col] = (df_cleaned[col].abs() / 100).round(0).astype(int) 
                    else:
                        df_cleaned.loc[:, col] = df_cleaned[col].astype(int)
            elif category_name == CATEGORY_NDAI:
                string_columns = df_cleaned.columns[-4:]
                df_cleaned[string_columns] = df_cleaned[string_columns].fillna("") 
                df_cleaned = df_cleaned.fillna(0)
            else:
                df_cleaned = df_cleaned.fillna(0) 
        except Exception as e:
            print(f"error at divide_100_convert_int{e}")
        return df_cleaned
    def drop_column_by_time(self,df, col):
        time_now = datetime.now().strftime("%H:%M:%S") 
        if START_TIME_AM <= time_now < END_TIME_AM:
            if "_PM" in col:
                df.drop(columns=[col], inplace=True)  # Drop the column if it contains "_PM_"
            else:
                rename_col = col.replace("_AM", "")  # Rename the column if it contains "_AM_"
                return rename_col

        elif END_TIME_AM <= time_now or time_now < END_TIME_PM:
            if "_AM" in col:
                df.drop(columns=[col], inplace=True)  
            else:
                rename_col = col.replace("_PM", "")  
                return rename_col
        else:
            return col  

    def read_and_process_csv(self, file_path, category_name):
        try:
            df = pd.read_csv(file_path, encoding="shift-jis", skiprows=[1])
            df = self.divide_100_convert_int(df,category_name)
            if category_name in UB_DOOR_SM_CATEGORIES: 
                new_columns = [self.drop_column_by_time(df, col) for col in df.columns]

                new_columns = [col for col in new_columns if col is not None]
                df.columns = new_columns
                df = self.process_column_names(df, category_name)
            else: # for Andon and Ndai
                df = self.process_column_names(df, category_name)
                logger.info(f"Successfully read and processed CSV file: {file_path}")
            return df

        except Exception as e:
            logger.error(f"Error processing {file_path}: {str(e)}", exc_info=True)
            raise 
    
    def get_round_info_for_all_times(self, merged_df):
        round_info = []
        try:
            for time_input in merged_df['hour_minute']:
                round_number, is_morning = round_and_is_morning_mapping(time_input)
                round_update=  check_round_update(time_input)
                result= get_round_times(round_number, is_morning)
                if result is not None:
                    start_time, end_time  = result
                else:
                    start_time , end_time=  '04:00', '05:00'
                round_info.append({
                    'round_number': round_number,
                    'is_morning': is_morning,
                    'hour_minute': time_input,  
                    'start_time': start_time,
                    'end_time': end_time,
                    'round_update': round_update
                })
            logger.debug("Successfully retrieved round information for all times.")
            return pd.DataFrame(round_info)
        except Exception as e:
            logger.error(f"Error retrieving round information: {e}", exc_info=True)
            raise 
