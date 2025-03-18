import pandas as pd
from datetime import datetime
from sqlalchemy import create_engine, text
from enties.door import DoorPageData1, DoorPageData2
from enties.under_body import UnderBodyPageData1, UnderBodyPageData2, UnderBodyPageData3
def process_csv_file(file_path, existing_times_set):
    # Đọc file CSV, bỏ qua chỉ dòng 2 (index bắt đầu từ 0, nên bỏ dòng 1)
    df = pd.read_csv(file_path, encoding='utf-8', skiprows=[1])
    
    # Chuyển đổi cột '収集日時' thành datetime và tách ra năm, tháng, ngày, giờ, phút
    df['収集日時'] = pd.to_datetime(df['収集日時'], format='%Y/%m/%d %H:%M:%S')

    df['year'] = df['収集日時'].dt.year
    df['month'] = df['収集日時'].dt.month
    df['day'] = df['収集日時'].dt.day
    df['hour'] = df['収集日時'].dt.hour
    df['minute'] = df['収集日時'].dt.minute

    df['round'] = 1  # Ví dụ round là 1
    df['is_morning'] = 0  # Ví dụ is_morning là 0

    df['fender_boketsu'] = df['OPC1_fender_boketsu_1']
    df['sps_boketsu'] = df['OPC1_sps_boketsu_1']
    
    # Tạo kết nối tới cơ sở dữ liệu (ví dụ PostgreSQL)
    engine = create_engine('postgresql://username:password@localhost:5432/your_database')

    # Lọc dữ liệu để chỉ lưu dữ liệu mới (chưa có trong cơ sở dữ liệu)
    new_data = []

    for index, row in df.iterrows():
        time_key = (row['year'], row['month'], row['day'], row['hour'], row['minute'])
        
        if time_key not in existing_times_set:
           
            new_data.append({
                'round': row['round'],
                'is_morning': row['is_morning'],
                'year': row['year'],
                'month': row['month'],
                'day': row['day'],
                'hour': row['hour'],
                'minute': row['minute'],
                'fender_boketsu': row['fender_boketsu'],
                'sps_boketsu': row['sps_boketsu'],
                'round_update': False,
                'delete_flag': False,
                'update_time': datetime.now()
            })
            existing_times_set.add(time_key)  # Thêm thời gian vào bộ nhớ
   
    # Nếu có dữ liệu mới, thực hiện insert
    if new_data:
        insert_df = pd.DataFrame(new_data)
        insert_df.to_sql('door_page_data2', engine, if_exists='append', index=False)
        print(f"Inserted {len(new_data)} new rows into door_page_data2.")
    else:
        print("No new data to insert.")

# Tạo kết nối tới cơ sở dữ liệu để lấy thông tin thời gian đã có
def get_existing_times(engine, table_name='under_body_page_data3'):
    # Tạo kết nối từ engine
    with engine.connect() as connection:
        # Truy vấn lấy thời gian mới nhất (thời gian lớn nhất)
        query = text("""
            SELECT year, month, day, hour, minute 
            FROM {table_name}
            ORDER BY year DESC, month DESC, day DESC, hour DESC, minute DESC
            LIMIT 1
        """.format(table_name=table_name))  # Chú ý sử dụng .format để chèn tên bảng

        # Thực thi câu truy vấn
        result = connection.execute(query)
        print("result", result)
        # Lưu trữ thời gian mới nhất vào một set (mặc dù chỉ có một record duy nhất)
        existing_times_set = set()
        for row in result:
            existing_times_set.add((row[0], row[1], row[2], row[3], row[4]))
    
    return existing_times_set

def tabel_names(category_name):
  
    if category_name == "ドア":
        return DoorPageData1, DoorPageData2
    elif category_name == "UB":
        return  UnderBodyPageData1, UnderBodyPageData2, UnderBodyPageData3
    # elif category_name == "SM":
    #     return 
    return None

def get_existing_times(engine, category_name):
    
    table_models = tabel_names(category_name)

    if not table_models:
        raise ValueError(f"No table models found for category: {category_name}")
    
    table_model = table_models[0]  # Bạn có thể thay đổi điều này nếu muốn lấy bảng khác
    
    # Tạo session từ engine
    Session = sessionmaker(bind=engine)
    session = Session()
    
    # Truy vấn lấy thời gian mới nhất từ bảng tương ứng
    latest_time = session.query(table_model.year, table_model.month, table_model.day,
                                table_model.hour, table_model.minute). \
                    order_by(table_model.year.desc(), table_model.month.desc(),
                             table_model.day.desc(), table_model.hour.desc(),
                             table_model.minute.desc()). \
                    first()  

    session.close()

    # Nếu có kết quả, trả về kết quả dưới dạng tuple
    if latest_time:
        existing_times_set = {(latest_time[0], latest_time[1], latest_time[2], 
                               latest_time[3], latest_time[4])}
        return existing_times_set
    else:
        # Nếu không có dữ liệu trong bảng, trả về set rỗng
        return set()
# Gọi hàm để lấy các thời gian đã tồn tại và xử lý file CSV
engine = create_engine('postgresql://postgres:12345@localhost:5432/test_db')
existing_times_set = get_existing_times(engine)
print("existing_times_set", existing_times_set)
# process_csv_file('path_to_your_file.csv', existing_times_set)
