


def get_existing_time(engine, table_name='under_body_page_data3'):
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
        existing_times_set = []
        for row in result:
            existing_times_set.append((row[0], row[1], row[2], row[3], row[4]))
    
    return existing_times_set


def tabel_names(category_name):
  
    if category_name == "ドア":
        return "door_page_data1", "door_page_data2"
    elif category_name == "UB":
        return  "under_body_page_data1", "under_body_page_data2", "under_body_page_data3"
    elif category_name == "SM":
        return "sm_page_data1", "sm_page_data2", "sm_page_data3"
    return None
