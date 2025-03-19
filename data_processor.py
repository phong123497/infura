import pandas as pd
from mapper.round_mapping import round_and_is_morning_mapping, get_round_times
from logging_config import logger



class DataProcessor:
    def process_column_names(self, df):
        new_columns = []
        df = df.dropna()
        for col in df.columns[1:]:
            new_col_name = col[5:-2]
            new_columns.append(new_col_name)
        df.columns = [df.columns[0]] + new_columns  
        return df
    # def check_text_value(self, df):
    #     try:
    #         for col in df.columns[:1]:
    #             df[col] = pd.to_numeric(df[col], errors='coerce')
    #         df = df.dropna()
    #     except Exception as e:
    #         logger.error(f"Error processing {file_path}: {str(e)}", exc_info=True)
        
    def divide_100_convert_int( self, df):
        df_cleaned = df.dropna() #  drop row has nan value
        # df_cleaned = df_cleaned.copy()  
        try:
            for col in df_cleaned.columns[1:]:
                if 'daisu' not in col:
                    # df[col] = pd.to_numeric(df[col], errors='coerce')
                    df_cleaned.loc[:, col] = (df_cleaned[col] / 100).round(0).astype(int) 
        except Exception as e:
            print(f"error{e}")
        
        return df_cleaned
    def read_and_process_csv(self, file_path):
        try:
            df = pd.read_csv(file_path, encoding="shift-jis", skiprows=[1])
            df = self.process_column_names(df)
            df = self.divide_100_convert_int(df)
            logger.info(f"Successfully read and processed CSV file: {file_path}")
            return df
        except Exception as e:
            logger.error(f"Error processing {file_path}: {str(e)}", exc_info=True)
            raise  # Re-raise the exception

    def get_round_info_for_all_times(self, merged_df):
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
            logger.debug("Successfully retrieved round information for all times.")
            return pd.DataFrame(round_info)
        except Exception as e:
            logger.error(f"Error retrieving round information: {e}", exc_info=True)
            raise 