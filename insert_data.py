from sqlalchemy import create_engine, Column, Integer, BigInteger, String, Boolean, SmallInteger, Time, TIMESTAMP, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from datetime import datetime
import pandas as pd
Base = declarative_base()
# Kết nối tới PostgreSQL
DATABASE_URI = 'postgresql://postgres:12345@localhost:5432/test_db'  # Thay bằng URI của bạn
engine = create_engine(DATABASE_URI)
Session = sessionmaker(bind=engine)
session = Session()
# Định nghĩa các cột từ bảng PostgreSQL (Class DoorPageData1)


class DoorPageData1(Base):
    __tablename__ = 'door_page_data1'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    f_dr_daisu = Column(Integer)
    f_dl_daisu = Column(Integer)
    s_dr_daisu = Column(Integer)
    s_dl_daisu = Column(Integer)
    food_daisu = Column(Integer)
    b_d_daisu = Column(Integer)
    f_dr_em_time = Column(Integer)
    f_dl_em_time = Column(Integer)
    s_dr_em_time = Column(Integer)
    s_dl_em_time = Column(Integer)
    food_em_time = Column(Integer)
    b_d_em_time = Column(Integer)
    f_dr_boman = Column(Integer)
    f_dl_boman = Column(Integer)
    s_dr_boman = Column(Integer)
    s_dl_boman = Column(Integer)
    food_boman = Column(Integer)
    b_d_boman = Column(Integer)
    f_dr_boketsu = Column(Integer)
    f_dl_boketsu = Column(Integer)
    s_dr_boketsu = Column(Integer)
    s_dl_boketsu = Column(Integer)
    food_boketsu = Column(Integer)
    b_d_boketsu = Column(Integer)
    f_dr_shokusei_yobidashi = Column(Integer)
    f_dl_shokusei_yobidashi = Column(Integer)
    s_dr_shokusei_yobidashi = Column(Integer)
    s_dl_shokusei_yobidashi = Column(Integer)
    food_shokusei_yobidashi = Column(Integer)
    b_d_shokusei_yobidashi = Column(Integer)
    f_dr_sei_yobidashi = Column(Integer)
    f_dl_sei_yobidashi = Column(Integer)
    s_dr_sei_yobidashi = Column(Integer)
    s_dl_sei_yobidashi = Column(Integer)
    food_sei_yobidashi = Column(Integer)
    b_d_sei_yobidashi = Column(Integer)

class DoorPageDataMapper:
    # Đây là một ánh xạ giữa các cột CSV và các trường của model DoorPageData1
    def map_to_model(self, row):
        # Tạo đối tượng DoorPageData1 từ một hàng (row) của DataFrame
        return DoorPageData1(
            f_dr_daisu=row['f_dr_daisu'],
            f_dl_daisu=row['f_dl_daisu'],
            s_dr_daisu=row['s_dr_daisu'],
            s_dl_daisu=row['s_dl_daisu'],
            food_daisu=row['food_daisu'],
            b_d_daisu=row['b_d_daisu'],
            f_dr_em_time=row['f_dr_em_time'],
            f_dl_em_time=row['f_dl_em_time'],
            s_dr_em_time=row['s_dr_em_time'],
            s_dl_em_time=row['s_dl_em_time'],
            food_em_time=row['food_em_time'],
            b_d_em_time=row['b_d_em_time'],
            f_dr_boman=row['f_dr_boman'],
            f_dl_boman=row['f_dl_boman'],
            s_dr_boman=row['s_dr_boman'],
            s_dl_boman=row['s_dl_boman'],
            food_boman=row['food_boman'],
            b_d_boman=row['b_d_boman'],
            f_dr_boketsu=row['f_dr_boketsu'],
            f_dl_boketsu=row['f_dl_boketsu'],
            s_dr_boketsu=row['s_dr_boketsu'],
            s_dl_boketsu=row['s_dl_boketsu'],
            food_boketsu=row['food_boketsu'],
            b_d_boketsu=row['b_d_boketsu'],
            f_dr_shokusei_yobidashi=row['f_dr_shokusei_yobidashi'],
            f_dl_shokusei_yobidashi=row['f_dl_shokusei_yobidashi'],
            s_dr_shokusei_yobidashi=row['s_dr_shokusei_yobidashi'],
            s_dl_shokusei_yobidashi=row['s_dl_shokusei_yobidashi'],
            food_shokusei_yobidashi=row['food_shokusei_yobidashi'],
            b_d_shokusei_yobidashi=row['b_d_shokusei_yobidashi'],
            f_dr_sei_yobidashi=row['f_dr_sei_yobidashi'],
            f_dl_sei_yobidashi=row['f_dl_sei_yobidashi'],
            s_dr_sei_yobidashi=row['s_dr_sei_yobidashi'],
            s_dl_sei_yobidashi=row['s_dl_sei_yobidashi'],
            food_sei_yobidashi=row['food_sei_yobidashi'],
            b_d_sei_yobidashi=row['b_d_sei_yobidashi']
        )
path_file = "C:\\Users\\nguyen-duy-phong\\Documents\\inabe_lstm_app\\merge1.csv"
# Đọc file CSV
df = pd.read_csv(path_file, encoding="shift-jis")


df.columns = df.columns.str.strip()  #

# Tạo dictionary mapping cột CSV với cột bảng PostgreSQL
column_mapping = {
    'b_d_boketsu': 'b_d_boketsu',
    'f_dl_boketsu': 'f_dl_boketsu',
    'f_dr_boketsu': 'f_dr_boketsu',
    'food_boketsu': 'food_boketsu',
    's_dl_boketsu': 's_dl_boketsu',
    's_dr_boketsu': 's_dr_boketsu',
    'b_d_boman': 'b_d_boman',
    'f_dl_boman': 'f_dl_boman',
    'f_dr_boman': 'f_dr_boman',
    'food_boman': 'food_boman',
    's_dl_boman': 's_dl_boman',
    's_dr_boman': 's_dr_boman',
    'b_d_daisu': 'b_d_daisu',
    'f_dl_daisu': 'f_dl_daisu',
    'f_dr_daisu': 'f_dr_daisu',
    'food_daisu': 'food_daisu',
    's_dl_daisu': 's_dl_daisu',
    's_dr_daisu': 's_dr_daisu',
    'b_d_em_time': 'b_d_em_time',
    'f_dl_em_time': 'f_dl_em_time',
    'f_dr_em_time': 'f_dr_em_time',
    'food_em_time': 'food_em_time',
    's_dl_em_time': 's_dl_em_time',
    's_dr_em_time': 's_dr_em_time',
    'b_d_shokusei_yobidashi': 'b_d_shokusei_yobidashi',
    'f_dl_shokusei_yobidashi': 'f_dl_shokusei_yobidashi',
    'f_dr_shokusei_yobidashi': 'f_dr_shokusei_yobidashi',
    'food_shokusei_yobidashi': 'food_shokusei_yobidashi',
    's_dl_shokusei_yobidashi': 's_dl_shokusei_yobidashi',
    's_dr_shokusei_yobidashi': 's_dr_shokusei_yobidashi',
    'b_d_sei_yobidashi': 'b_d_sei_yobidashi',
    'f_dl_sei_yobidashi': 'f_dl_sei_yobidashi',
    'f_dr_sei_yobidashi': 'f_dr_sei_yobidashi',
    'food_sei_yobidashi': 'food_sei_yobidashi',
    's_dl_sei_yobidashi': 's_dl_sei_yobidashi',
    's_dr_sei_yobidashi': 's_dr_sei_yobidashi'
}

df = df.rename(columns=column_mapping)
mapper = DoorPageDataMapper()
# Chuyển đổi DataFrame sang đối tượng tương ứng với database (mapping vào bảng PostgreSQL)
for index, row in df.iterrows():
    door_page_data = mapper.map_to_model(row)
    
    session.add(door_page_data)

session.commit()

session.close()

print("Dữ liệu đã được thêm vào bảng database.")
