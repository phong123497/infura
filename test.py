import pandas as pd

class DataProcessor:
    
    def process_column_names(self, df):
        """
        Chỉnh sửa tên cột của DataFrame bằng cách cắt bỏ phần đầu và phần cuối của tên cột (trừ cột đầu tiên).
        """
        new_columns = []

        for col in df.columns[1:]:
            # Cắt bỏ 5 ký tự đầu và 2 ký tự cuối từ tên cột
            new_col_name = col[5:-2]
            new_columns.append(new_col_name)

        # Cập nhật lại tên cột trong DataFrame
        df.columns = [df.columns[0]] + new_columns  # Giữ cột đầu tiên không thay đổi
        return df
    
    def divie_by_100_get_integer(self, df):
        for col in df.columns[1:]:
            if 'daisu' not in col:
                df[col] = (df[col] / 100).round(0).astype(int)
        
        return df
    def check_text_value(self, df):
        try:
            for col in df.columns:
                df[col] = pd.to_numeric(df[col], errors='coerce')
            df = df.dropna()
        except Exception as e:
            # logger.error(f"Error processing {file_path}: {str(e)}", exc_info=True)
            print(f"Error processing {file_path}: {str(e)}")
        

        return df
# Giả sử bạn có một DataFrame df
df = pd.DataFrame({
    'id': [1, 2, 3],
    'data_01': ['100', '200', 'abc'],  # 'abc' không phải là số
    'data_02': [1000, 'xyz', 3000],  # 'xyz' không phải là số
})
# file_path = "C:\\Users\\nguyen-duy-phong\\Downloads\\infura_data\\0314\\UB\\ラウンド01\\職制呼出回数\\2025\\03\\ub_r01_shokusei_yobidashi_20250313.csv"
file_path = "C:\\Users\\nguyen-duy-phong\\Downloads\\infura_data\\0314\\UB\\ラウンド01\\職制呼出回数\\2025\\03\\ub_r01_shokusei_yobidashi_20250313.csv"
# file_path = "C:\\Users\\nguyen-duy-phong\\Downloads\\infura_data\\0314\\UB\\ラウンド01\異常停止時間\\2025\\03\\ub_r01_em_time_20250313.csv"
# Tạo đối tượng DataProcessor và áp dụng các phương thức
processor = DataProcessor()
df = pd.read_csv(file_path, encoding="shift-jis", skiprows=[1])
print(f"Before dropping NaN: {df.shape}")

# Loại bỏ hàng chứa NaN
df_cleaned = df.dropna()

# In ra số dòng và cột sau khi loại bỏ NaN
print(f"After dropping NaN: {df_cleaned.shape}")

# Hiển thị DataFrame sau khi loại bỏ NaN
print(df_cleaned)
# df = processor.check_text_value(df)
# df = processor.divie_by_100_get_integer(df)

# # Hiển thị DataFrame kết quả
# print(df)
# print(df.dtypes)