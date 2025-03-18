import pandas as pd
from sqlalchemy import create_engine, Column, Integer, BigInteger, String, Boolean, SmallInteger, Time, TIMESTAMP, ForeignKey, select
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker, Session
from datetime import datetime

Base = declarative_base()

# Định nghĩa bảng `id_master`
class IdMaster(Base):
    __tablename__ = 'id_master'
    
    id = Column(BigInteger, primary_key=True, autoincrement=True)
    table_name = Column(String(255), nullable=False)
    created_at = Column(TIMESTAMP, nullable=False, default=datetime.now)
    delete_flag = Column(Boolean, default=False)

# Định nghĩa bảng `parameter_master`
class ParameterMaster(Base):
    __tablename__ = 'parameter_master'
    
    parameter_id = Column(Integer, primary_key=True, autoincrement=True)
    parameter_name = Column(String(255), nullable=False)
    parameter_value = Column(String(255))
    created_at = Column(TIMESTAMP, nullable=False, default=datetime.now)
    delete_flag = Column(Boolean, default=False)

# Định nghĩa bảng `round_master`
class RoundMaster(Base):
    __tablename__ = 'round_master'
    
    round_id = Column(Integer, primary_key=True, autoincrement=True)
    round_number = Column(SmallInteger, nullable=False)
    start_time = Column(Time, nullable=False)
    end_time = Column(Time, nullable=False)
    is_morning = Column(SmallInteger)
    delete_flag = Column(Boolean, default=False)
    update_time = Column(TIMESTAMP, nullable=False, default=datetime.now)


# engine = create_engine('postgresql://postgres:12345@localhost:5432/test_db')

# Tạo các bảng trong cơ sở dữ liệu nếu chưa tồn tại
# Base.metadata.create_all(engine)

# # Tạo session để tương tác với cơ sở dữ liệu
# Session = sessionmaker(bind=engine)
# session = Session()

# # Đóng session khi không sử dụng nữa
# session.close()


class RoundMasterMapperNoCheck:
    def map_to_fields(seld, row):
        return RoundMaster(
            round_number=row['round_number'],
            start_time=row['start_time'],
            end_time=row['end_time'],
            is_morning=row['is_morning'],
            delete_flag=row['delete_flag'],
            update_time=row['update_time']
        )
