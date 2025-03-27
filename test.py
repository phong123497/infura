# import pandas as pd

# class DataProcessor:
    
#     def process_column_names(self, df):
#         """
#         Chỉnh sửa tên cột của DataFrame bằng cách cắt bỏ phần đầu và phần cuối của tên cột (trừ cột đầu tiên).
#         """
#         new_columns = []

#         for col in df.columns[1:]:
#             # Cắt bỏ 5 ký tự đầu và 2 ký tự cuối từ tên cột
#             new_col_name = col[5:-2]
#             new_columns.append(new_col_name)

#         # Cập nhật lại tên cột trong DataFrame
#         df.columns = [df.columns[0]] + new_columns  # Giữ cột đầu tiên không thay đổi
#         return df
    
#     def divie_by_100_get_integer(self, df):
#         for col in df.columns[1:]:
#             if 'daisu' not in col:
#                 df[col] = (df[col] / 100).round(0).astype(int)
        
#         return df
#     def check_text_value(self, df):
#         try:
#             for col in df.columns:
#                 df[col] = pd.to_numeric(df[col], errors='coerce')
#             df = df.dropna()
#         except Exception as e:
#             # logger.error(f"Error processing {file_path}: {str(e)}", exc_info=True)
#             print(f"Error processing {file_path}: {str(e)}")
        

#         return df
# # Giả sử bạn có một DataFrame df
# df = pd.DataFrame({
#     'id': [1, 2, 3],
#     'data_01': ['100', '200', 'abc'],  # 'abc' không phải là số
#     'data_02': [1000, 'xyz', 3000],  # 'xyz' không phải là số
# })
# # file_path = "C:\\Users\\nguyen-duy-phong\\Downloads\\infura_data\\0314\\UB\\ラウンド01\\職制呼出回数\\2025\\03\\ub_r01_shokusei_yobidashi_20250313.csv"
# file_path = "C:\\Users\\nguyen-duy-phong\\Downloads\\infura_data\\0314\\UB\\ラウンド01\\職制呼出回数\\2025\\03\\ub_r01_shokusei_yobidashi_20250313.csv"
# # file_path = "C:\\Users\\nguyen-duy-phong\\Downloads\\infura_data\\0314\\UB\\ラウンド01\異常停止時間\\2025\\03\\ub_r01_em_time_20250313.csv"
# # Tạo đối tượng DataProcessor và áp dụng các phương thức
# processor = DataProcessor()
# df = pd.read_csv(file_path, encoding="shift-jis", skiprows=[1])
# print(f"Before dropping NaN: {df.shape}")

# # Loại bỏ hàng chứa NaN
# df_cleaned = df.dropna()

# # In ra số dòng và cột sau khi loại bỏ NaN
# print(f"After dropping NaN: {df_cleaned.shape}")

# # Hiển thị DataFrame sau khi loại bỏ NaN
# print(df_cleaned)
# # df = processor.check_text_value(df)
# # df = processor.divie_by_100_get_integer(df)

# # # Hiển thị DataFrame kết quả
# # print(df)
# # print(df.dtypes)


import pandas as pd
from datetime import datetime


# import pandas as pd
# from datetime import datetime

path_file = "C:\\Users\\nguyen-duy-phong\\Downloads\\0326_ndai_adon\\0326_ndai_adon\\Ndai_20250326.csv"
df = pd.read_csv(path_file, encoding="shift-jis", skiprows=[1])


# Điền giá trị mặc định là "" cho 4 cột cuối, giả sử 4 cột cuối là string
def process_column_names_ndai( df):
    string_columns = df.columns[-4:]
    df[string_columns] = df[string_columns].fillna("") 
    
    df = df.fillna(0) 

    # Duyệt qua các cột, bỏ qua 4 cột cuối và chỉ thực hiện tính toán cho cột số (integer)
    for col in df.columns[1:-4]:  # Bỏ qua 4 cột cuối
        df.loc[:, col] = (df[col].abs() / 100).round(0).astype(int)
    return df
df = process_column_names_ndai(df)
df.to_csv("teet2.csv", index=False, encoding="shift-jis")
# # Định nghĩa hàm để xóa hoặc đổi tên cột theo thời gian
# def drop_column_by_time(col):
#     global df
#     if "063000" <= time_now < "171000":  # Từ 06:30 đến 17:10
#         if "_PM_" in col:
#             df.drop(columns=[col], inplace=True)  # Xóa cột nếu có "_PM_"
#         else:
#             rename_col = col.replace("_AM_", "")  # Đổi tên cột nếu có "_AM_8"
#             return rename_col
        
#     elif "171000" <= time_now  or time_now < "031000": 
#         if "_AM_" in col:
#             df.drop(columns=[col], inplace=True) 
#         else:
#             rename_col = col.replace("_PM_", "")  
#             return rename_col
    
#     else:
#         return col  

# # Áp dụng hàm để thay đổi tên cột và xóa các cột không cần thiết
# new_columns = [drop_column_by_time(col) for col in df.columns]

# new_columns = [col for col in new_columns if col is not None] 
# df.columns = new_columns 
# # Lưu DataFrame vào file CSV mới
# df.to_csv("test.csv", index=False, encoding="shift-jis")

# # In ra tên các cột đã được thay đổi để kiểm tra
# print(df.columns)


# from datetime import datetime
# import os

# from mapper.round_mapping import round_times

# def check_folder_round_and_time(category_name_path):
#     # timenow = datetime.now().strftime("%H%M%S")
#     timenow = "220000"
    
#     current_round_number = None
#     for round_time in round_times:
#         if round_time['start'] <= timenow <= round_time['end']:
#             current_round_number = round_time['round']
#             print(f"Current round: {current_round_number:02d}") 
#             break
#         else:
#             print("kiuke")
    
#     # Tạo đường dẫn thư mục cho vòng
#     current_round_number_formatted = f"{current_round_number:02d}"  
#     curren_path = os.path.join(category_name_path, f"ラウンド{current_round_number_formatted}")
#     print(f"ラウンド{current_round_number_formatted}")
    
#     return current_round_number_formatted

# category_name_path = "C:\\Users\\nguyen-duy-phong\\Downloads\\0322andon\\0322all\\UB"
# check_folder_round_and_time(category_name_path)

column_names = [
    'OPC1_sample_kotei_ryuju_no', 'OPC1_sample_kotei_renban', 'OPC1_sample_kotei_shashu', 'OPC1_mbm_kotei_ryuju_no', 'OPC1_mbm_kotei_renban', 'OPC1_mbm_kotei_shashu', 'OPC1_mbk1kotei_ub_paretto_no', 'OPC1_mbk1kotei_shashu', 'OPC1_mbk1kotei_renban', 'OPC1_mbk2kotei_dl_matehanshashu', 'OPC1_mbk2kotei_renban', 'OPC1_sm_outer_l1kotei_670_sukitto_no', 'OPC1_sm_outer_l1kotei_shashu', 'OPC1_sm_outer_l1kotei_renban', 'OPC1_sm_outer_l1kotei_670_shashu', 'OPC1_sm_outer_l1kotei_970_shashu', 'OPC1_sm_outer_r1kotei_670_sukitto_no', 'OPC1_sm_outer_r1kotei_shashu', 'OPC1_sm_outer_r1kotei_renban', 'OPC1_sm_outer_r1kotei_670_shashu', 'OPC1_sm_outer_r1kotei_970_shashu', 'OPC1_sm_sukiba_l_kotei_shashu', 'OPC1_sm_sukiba_l_kotei_renban', 'OPC1_sm_sukiba_l_kotei_sukitto_no', 'OPC1_sm_sukiba_r_kotei_shashu', 'OPC1_sm_sukiba_r_kotei_renban', 'OPC1_sm_sukiba_r_kotei_sukitto_no', 'OPC1_s_dl_kotei_shashu', 'OPC1_s_dl_kotei_renban', 'OPC1_s_dl_kotei_kaiten_jigu_no', 'OPC1_s_dr_kotei_shashu', 'OPC1_s_dr_kotei_renban', 'OPC1_s_dr_kotei_kaiten_jigu_no', 'OPC1_b_d_kotei_shashu', 'OPC1_b_d_kotei_renban', 'OPC1_b_d_kotei_kaiten_jigu_no', 'OPC1_e_c_kotei_shashu', 'OPC1_e_c_kotei_renban', 'OPC1_e_c_kotei_sukitto_no', 'OPC1_rr_u_kotei_shashu', 'OPC1_rr_u_kotei_renban', 'OPC1_rr_u_kotei_sukitto_no', 'OPC1_ctrr_kotei_shashu', 'OPC1_ctrr_kotei_renban', 'OPC1_ctrr_kotei_sukitto_no', 'OPC1_A_ukekoma_data_0_0', 'OPC1_A_ukekoma_data_0_1', 'OPC1_A_ukekoma_data_0_2', 'OPC1_A_ukekoma_data_0_3', 'OPC1_A_ukekoma_data_1_0', 'OPC1_A_ukekoma_data_1_1', 'OPC1_A_ukekoma_data_1_2', 'OPC1_A_ukekoma_data_1_3', 'OPC1_A_ukekoma_data_2_0', 'OPC1_A_ukekoma_data_2_1', 'OPC1_A_ukekoma_data_2_2', 'OPC1_A_ukekoma_data_2_3', 'OPC1_A_ukekoma_data_3_0', 'OPC1_A_ukekoma_data_3_1', 'OPC1_A_ukekoma_data_3_2', 'OPC1_A_ukekoma_data_3_3', 'OPC1_B_ukekoma_data_0_0', 'OPC1_B_ukekoma_data_0_1', 'OPC1_B_ukekoma_data_0_2', 'OPC1_B_ukekoma_data_0_3', 'OPC1_B_ukekoma_data_1_0', 'OPC1_B_ukekoma_data_1_1', 'OPC1_B_ukekoma_data_1_2', 'OPC1_B_ukekoma_data_1_3', 'OPC1_B_ukekoma_data_2_0', 'OPC1_B_ukekoma_data_2_1', 'OPC1_B_ukekoma_data_2_2', 'OPC1_B_ukekoma_data_2_3', 'OPC1_B_ukekoma_data_3_0', 'OPC1_B_ukekoma_data_3_1', 'OPC1_B_ukekoma_data_3_2', 'OPC1_B_ukekoma_data_3_3', 'OPC1_C_ukekoma_data_0_0', 'OPC1_C_ukekoma_data_0_1', 'OPC1_C_ukekoma_data_0_2', 'OPC1_C_ukekoma_data_0_3', 'OPC1_C_ukekoma_data_1_0', 'OPC1_C_ukekoma_data_1_1', 'OPC1_C_ukekoma_data_1_2', 'OPC1_C_ukekoma_data_1_3', 'OPC1_C_ukekoma_data_2_0', 'OPC1_C_ukekoma_data_2_1', 'OPC1_C_ukekoma_data_2_2', 'OPC1_C_ukekoma_data_2_3', 'OPC1_C_ukekoma_data_3_0', 'OPC1_C_ukekoma_data_3_1', 'OPC1_C_ukekoma_data_3_2', 'OPC1_C_ukekoma_data_3_3', 'OPC1_D_ukekoma_data_0_0', 'OPC1_D_ukekoma_data_0_1', 'OPC1_D_ukekoma_data_0_2', 'OPC1_D_ukekoma_data_0_3', 'OPC1_D_ukekoma_data_1_0', 'OPC1_D_ukekoma_data_1_1', 'OPC1_D_ukekoma_data_1_2', 'OPC1_D_ukekoma_data_1_3', 'OPC1_D_ukekoma_data_2_0', 'OPC1_D_ukekoma_data_2_1', 'OPC1_D_ukekoma_data_2_2', 'OPC1_D_ukekoma_data_2_3', 'OPC1_D_ukekoma_data_3_0',
    'OPC1_D_ukekoma_data_3_1', 'OPC1_D_ukekoma_data_3_2', 'OPC1_D_ukekoma_data_3_3'
]
csv = [
    "sample_kotei_ryuju_no", "sample_kotei_renban", "sample_kotei_shashu", "mbm_kotei_ryuju_no",
    "mbm_kotei_renban", "mbm_kotei_shashu", "mbk1kotei_ub_paretto_no", "mbk1kotei_shashu",
    "mbk1kotei_renban", "mbk1kotei_uke_koma_no", "mbk2kotei_dl_matehanshashu", "mbk2kotei_renban",
    "sm_outer_l1kotei_670_sukitto_no", "sm_outer_l1kotei_shashu", "sm_outer_l1kotei_renban",
    "sm_outer_l1kotei_670_shashu", "sm_outer_l1kotei_970_shashu", "sm_outer_r1kotei_670_sukitto_no",
    "sm_outer_r1kotei_shashu", "sm_outer_r1kotei_renban", "sm_outer_r1kotei_670_shashu", "sm_outer_r1kotei_970_shashu",
    "sm_sukiba_l_kotei_shashu", "sm_sukiba_l_kotei_renban", "sm_sukiba_l_kotei_sukitto_no", "sm_sukiba_r_kotei_shashu",
    "sm_sukiba_r_kotei_renban", "sm_sukiba_r_kotei_sukitto_no", "s/dl_kotei_shashu", "s/dl_kotei_renban",
    "s/dl_kotei_kaiten_jigu_no", "s/dr_kotei_shashu", "s/dr_kotei_renban", "s/dr_kotei_kaiten_jigu_no",
    "b/d_kotei_shashu", "b/d_kotei_renban", "b/d_kotei_kaiten_jigu_no", "e/c_kotei_shashu", "e/c_kotei_renban",
    "e/c_kotei_sukitto_no", "rr/u_kotei_shashu", "rr/u_kotei_renban", "rr/u_kotei_sukitto_no", "ctrr_kotei_shashu",
    "ctrr_kotei_renban", "ctrr_kotei_sukitto_no", "A_ukekoma_data_0_0", "A_ukekoma_data_0_1", "A_ukekoma_data_0_2",
    "A_ukekoma_data_0_3", "A_ukekoma_data_1_0", "A_ukekoma_data_1_1", "A_ukekoma_data_1_2", "A_ukekoma_data_1_3",
    "A_ukekoma_data_2_0", "A_ukekoma_data_2_1", "A_ukekoma_data_2_2", "A_ukekoma_data_2_3", "A_ukekoma_data_3_0",
    "A_ukekoma_data_3_1", "A_ukekoma_data_3_2", "A_ukekoma_data_3_3", "B_ukekoma_data_0_0", "B_ukekoma_data_0_1",
    "B_ukekoma_data_0_2", "B_ukekoma_data_0_3", "B_ukekoma_data_1_0", "B_ukekoma_data_1_1", "B_ukekoma_data_1_2",
    "B_ukekoma_data_1_3", "B_ukekoma_data_2_0", "B_ukekoma_data_2_1", "B_ukekoma_data_2_2", "B_ukekoma_data_2_3",
    "B_ukekoma_data_3_0", "B_ukekoma_data_3_1", "B_ukekoma_data_3_2", "B_ukekoma_data_3_3", "C_ukekoma_data_0_1",
    "C_ukekoma_data_0_2", "C_ukekoma_data_0_3", "C_ukekoma_data_1_0", "C_ukekoma_data_1_1", "C_ukekoma_data_1_2",
    "C_ukekoma_data_1_3", "C_ukekoma_data_2_0", "C_ukekoma_data_2_1", "C_ukekoma_data_2_2", "C_ukekoma_data_2_3",
    "C_ukekoma_data_3_0", "C_ukekoma_data_3_1", "C_ukekoma_data_3_2", "C_ukekoma_data_3_3", "D_ukekoma_data_0_0",
    "D_ukekoma_data_0_1", "D_ukekoma_data_0_2", "D_ukekoma_data_0_3", "D_ukekoma_data_1_0", "D_ukekoma_data_1_1",
    "D_ukekoma_data_1_2", "D_ukekoma_data_1_3", "D_ukekoma_data_2_0", "D_ukekoma_data_2_1", "D_ukekoma_data_2_2",
    "D_ukekoma_data_2_3", "D_ukekoma_data_3_0", "D_ukekoma_data_3_1", "D_ukekoma_data_3_2", "D_ukekoma_data_3_3"
]

excel = [
    "sample_kotei_ryuju_no", "sample_kotei_renban", "sample_kotei_shashu", "mbm_kotei_ryuju_no",
    "mbm_kotei_renban", "mbm_kotei_shashu", "mbk1kotei_ub_paretto_no", "mbk1kotei_shashu",
    "mbk1kotei_renban", "mbk1kotei_uke_koma_no", "mbk2kotei_dl_matehanshashu", "mbk2kotei_renban",
    "sm_outer_l1kotei_670_sukitto_no", "sm_outer_l1kotei_shashu", "sm_outer_l1kotei_renban",
    "sm_outer_l1kotei_670_shashu", "sm_outer_l1kotei_970_shashu", "sm_outer_r1kotei_670_sukitto_no",
    "sm_outer_r1kotei_shashu", "sm_outer_r1kotei_renban", "sm_outer_r1kotei_670_shashu", "sm_outer_r1kotei_970_shashu",
    "sm_sukiba_l_kotei_shashu", "sm_sukiba_l_kotei_renban", "sm_sukiba_l_kotei_sukitto_no", "sm_sukiba_r_kotei_shashu",
    "sm_sukiba_r_kotei_renban", "sm_sukiba_r_kotei_sukitto_no", "s/dl_kotei_shashu", "s/dl_kotei_renban",
    "s/dl_kotei_kaiten_jigu_no", "s/dr_kotei_shashu", "s/dr_kotei_renban", "s/dr_kotei_kaiten_jigu_no",
    "b/d_kotei_shashu", "b/d_kotei_renban", "b/d_kotei_kaiten_jigu_no", "e/c_kotei_shashu", "e/c_kotei_renban",
    "e/c_kotei_sukitto_no", "rr/u_kotei_shashu", "rr/u_kotei_renban", "rr/u_kotei_sukitto_no", "ctrr_kotei_shashu",
    "ctrr_kotei_renban", "ctrr_kotei_sukitto_no", "A_ukekoma_data_0_0", "A_ukekoma_data_0_1", "A_ukekoma_data_0_2",
    "A_ukekoma_data_0_3", "A_ukekoma_data_1_0", "A_ukekoma_data_1_1", "A_ukekoma_data_1_2", "A_ukekoma_data_1_3",
    "A_ukekoma_data_2_0", "A_ukekoma_data_2_1", "A_ukekoma_data_2_2", "A_ukekoma_data_2_3", "A_ukekoma_data_3_0",
    "A_ukekoma_data_3_1", "A_ukekoma_data_3_2", "A_ukekoma_data_3_3", "B_ukekoma_data_0_0", "B_ukekoma_data_0_1",
    "B_ukekoma_data_0_2", "B_ukekoma_data_0_3", "B_ukekoma_data_1_0", "B_ukekoma_data_1_1", "B_ukekoma_data_1_2",
    "B_ukekoma_data_1_3", "B_ukekoma_data_2_0", "B_ukekoma_data_2_1", "B_ukekoma_data_2_2", "B_ukekoma_data_2_3",
    "B_ukekoma_data_3_0", "B_ukekoma_data_3_1", "B_ukekoma_data_3_2", "B_ukekoma_data_3_3", "C_ukekoma_data_0_1",
    "C_ukekoma_data_0_2", "C_ukekoma_data_0_3", "C_ukekoma_data_1_0", "C_ukekoma_data_1_1", "C_ukekoma_data_1_2",
    "C_ukekoma_data_1_3", "C_ukekoma_data_2_0", "C_ukekoma_data_2_1", "C_ukekoma_data_2_2", "C_ukekoma_data_2_3",
    "C_ukekoma_data_3_0", "C_ukekoma_data_3_1", "C_ukekoma_data_3_2", "C_ukekoma_data_3_3", "D_ukekoma_data_0_0",
    "D_ukekoma_data_0_1", "D_ukekoma_data_0_2", "D_ukekoma_data_0_3", "D_ukekoma_data_1_0", "D_ukekoma_data_1_1",
    "D_ukekoma_data_1_2", "D_ukekoma_data_1_3", "D_ukekoma_data_2_0", "D_ukekoma_data_2_1", "D_ukekoma_data_2_2",
    "D_ukekoma_data_2_3", "D_ukekoma_data_3_0", "D_ukekoma_data_3_1", "D_ukekoma_data_3_2", "D_ukekoma_data_3_3"
]

# Extract the last few characters of each word after removing the first 9
# ndai = [word[5:] for word in column_names]
# print(len(ndai))
# print(ndai)
# set_list_1 = set(csv)
# set_list_2 = set(excel)
# print("lengset", len(set_list_1))
# print("lengset", len(set_list_2))

# # Các mục có trong list_1 nhưng không có trong list_2
# only_in_list_1 = set_list_1 - set_list_2
# print("Các mục có trong list_1 nhưng không có trong list_2:", only_in_list_1)

# # Các mục có trong list_2 nhưng không có trong list_1
# only_in_list_2 = set_list_2 - set_list_1
# print("Các mục có trong list_2 nhưng không có trong list_1:", only_in_list_2)

# # Các mục chung giữa list_1 và list_2
# common_items = set_list_1 & set_list_2

# print("Các mục chung giữa list_1 và list_2:", common_items)
# print("leng", len(common_items))
