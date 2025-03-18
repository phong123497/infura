import os
import csv
import threading
import datetime
import pandas as pd

class DataProcee:
    def __init__(self, root_dir, db_config):
        """
        Khởi tạo DataProcee.

        Args:
            root_dir (str): Đường dẫn đến thư mục gốc chứa dữ liệu (root/).
            db_config (dict): Thông tin cấu hình kết nối cơ sở dữ liệu.
        """
        self.root_dir = root_dir
        self.db_config = db_config
        self.lock = threading.Lock() # Khóa để đảm bảo an toàn luồng khi ghi vào DB

    def connect_to_db(self):
        """
        Kết nối đến cơ sở dữ liệu.
        """
        try:
            conn = mariadb.connect(**self.db_config)
            return conn
        except mariadb.Error as e:
            print(f"Error connecting to database: {e}")
            return None

    def close_db_connection(self, conn):
      """Đóng kết nối cơ sở dữ liệu an toàn."""
      if conn:
          conn.close()

   

    def process_csv_files(self, data_dir, category_name, data_type, data_category):
        """
        Đọc và xử lý các file CSV trong một thư mục.

        Args:
            data_dir (str): Đường dẫn đến thư mục chứa file CSV (daisu/, entime/, ...).
            category_name (str): Tên thư mục cha (SM, Door, under body).
            data_type (str): Loại dữ liệu (daisu, entime, boman, boketsu, shokusei, sei).
            data_category (str) : data sub dir
        """
        for filename in os.listdir(data_dir):
            if filename.endswith(".csv"):
                file_path = os.path.join(data_dir, filename)
                self.process_csv_file(file_path, category_name, data_type, data_category)

    def process_csv_file(self, file_path, category_name, data_type, data_category):
      
        try:
            with open(file_path, 'r', encoding='utf-8') as csvfile:
                reader = csv.reader(csvfile)
                header = next(reader)  # Đọc header

                # Lấy các chỉ số cột quan trọng từ header (ví dụ: 'round', 'is_morning')
                # Bạn cần điều chỉnh dựa trên cấu trúc file CSV của bạn
                try:
                  round_index = header.index('round')
                  is_morning_index = header.index('is_morning')
                except ValueError as e:
                  print(f"Error: Required column not found in CSV file {file_path}: {e}")
                  return  # Bỏ qua file này nếu thiếu cột quan trọng

                for row in reader:
                    # Lấy dữ liệu từ các cột
                    try:
                      round_value = row[round_index]
                      is_morning_value = row[is_morning_index]
                      # Chuyển đổi kiểu dữ liệu nếu cần
                      round_value = int(round_value)
                      is_morning_value = int(is_morning_value) # Hoặc boolean nếu phù hợp
                    except (ValueError, IndexError) as e:
                      print(f"Error processing row in {file_path}: {e}")
                      continue # Bỏ qua hàng này nếu có lỗi
                    
                    # Tạo câu lệnh SQL INSERT dựa trên category_name, data_type và data từ CSV
                    # Ví dụ:
                    # - category_name: 'SM', 'Door', 'under body' -> Xác định bảng (sm_page_data1, door_page_data1, ...)
                    # - data_type: 'daisu', 'entime', 'boman', ... -> Xác định cột nào cần update
                    # Điều này đòi hỏi bạn phải mapping tên thư mục với tên bảng và tên cột tương ứng
                    table_name = self.map_category_to_table(category_name)
                    column_name = self.map_data_type_to_column(data_category, data_type) # daisu, entime, boman, ...


                    # Lấy các giá trị data tương ứng

                    # Connect to the database
                    conn = self.connect_to_db()
                    if conn:
                        cursor = conn.cursor()
                        try:
                            # Prepare the SQL query
                            # Ví dụ:  query = f"INSERT INTO {table_name} (round, is_morning, {column_name}) VALUES (%s, %s, %s)"
                            # query = self.generate_insert_query(table_name, round_value, is_morning_value, column_name, value)
                            query, values = self.generate_insert_query(table_name, round_value, is_morning_value, data_dir, row) # data_dir để map thêm các cột
                            cursor.execute(query, values)
                            conn.commit()
                            print(f"Inserted row into {table_name} from {file_path}")

                        except mariadb.Error as e:
                            print(f"Error inserting into database: {e}")
                            conn.rollback() # Rollback nếu có lỗi

                        finally:
                            cursor.close()
                            self.close_db_connection(conn)

        except FileNotFoundError:
            print(f"File not found: {file_path}")
        except Exception as e:
            print(f"Error processing file {file_path}: {e}")

    def map_category_to_table(self, category_name):
   
        if category_name == "SM":
            return "sm_page_data1" # 
        elif category_name == "Door":
            return "door_page_data1" # Hoặc door_page_data2
        elif category_name == "under body":
            return "under_body_page_data1" # Hoặc under_body_page_data2, under_body_page_data3
        else:
            return None  # Xử lý trường hợp không hợp lệ

    
    def run(self):
        """
        Bắt đầu quá trình xử lý dữ liệu.
        """
        categories = ["SM", "Door", "under body"]
        threads = []

        for category in categories:
            category_dir = os.path.join(self.root_dir, category)
            if os.path.exists(category_dir) and os.path.isdir(category_dir):
                # Tạo thread cho từng category (SM, Door, under body)
                thread = threading.Thread(target=self.process_directory, args=(category_dir, category, category))
                threads.append(thread)
                thread.start()

        # Chờ tất cả các thread hoàn thành
        for thread in threads:
            thread.join()

        print("Finished processing all data.")

# Cấu hình DB (thay đổi theo thông tin DB của bạn)
db_config = {
    'user': 'your_user',
    'password': 'your_password',
    'host': 'your_host',
    'port': 3306,
    'database': 'your_database'
}

# Sử dụng class
root_dir = "path/to/your/root/directory"  # Thay đổi đường dẫn này
processor = DataProcee(root_dir, db_config)
processor.run()

