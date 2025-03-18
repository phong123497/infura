import pandas as pd
from sqlalchemy import create_engine, Column, Integer, BigInteger, String, Boolean, SmallInteger, Time, TIMESTAMP, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from datetime import datetime
from sqlalchemy import select
from sqlalchemy.orm import Session

Base = declarative_base()

# Định nghĩa bảng `id_master`
class IdMaster(Base):
    __tablename__ = 'id_master'
    
    id = Column(BigInteger, primary_key=True, autoincrement=True)
    table_name = Column(String(255), nullable=False)
    created_at = Column(TIMESTAMP, nullable=False, default="CURRENT_TIMESTAMP")
    delete_flag = Column(Boolean, default=False)

# Định nghĩa bảng `parameter_master`
class ParameterMaster(Base):
    __tablename__ = 'parameter_master'
    
    parameter_id = Column(Integer, primary_key=True, autoincrement=True)
    parameter_name = Column(String(255), nullable=False)
    parameter_value = Column(String(255))
    created_at = Column(TIMESTAMP, nullable=False, default="CURRENT_TIMESTAMP")
    delete_flag = Column(Boolean, default=False)
    id_master_id = Column(BigInteger)
# Định nghĩa bảng `round_master`
class RoundMaster(Base):
    __tablename__ = 'round_master'
    
    round_id = Column(Integer, primary_key=True, autoincrement=True)
    round_number = Column(SmallInteger, nullable=False)
    start_time = Column(Time, nullable=False)
    end_time = Column(Time, nullable=False)
    is_morning = Column(SmallInteger)
    delete_flag = Column(Boolean, default=False)
    update_time = Column(TIMESTAMP, nullable=False, default="CURRENT_TIMESTAMP")
    id_master_id = Column(BigInteger)
    parameter_master_id = Column(Integer)
    

class IdMasterMapper:
    def __init__(self, session):
        self.session = session

    def get_or_create(self, create_at: TIMESTAMP, table_name: str) -> IdMaster:
        """
        Get existing IdMaster record or create a new one
        """
        # Check if record exists
        stmt = select(IdMaster).where(
            IdMaster.create_at == create_at,
            IdMaster.delete_flag == False
        )
        id_master = self.session.execute(stmt).scalar_one_or_none()
        
        if not id_master:
            # Create new record
            id_master = IdMaster(
                table_name=table_name,
                created_at=create_at,
                delete_flag=False
            )
            self.session.add(id_master)
            self.session.flush()  # Assign ID immediately
        
        return id_master
            
class RoundMasterMapper:
    def __init__(self, session):
        self.session = session

    def map_to_model(self, round_number: int, is_morning: int, table_name: str) -> RoundMaster:
      
        # Get the corresponding times for the round
        start_time, end_time = self.get_round_times(round_number, is_morning)
        
        # Get or create IdMaster record
        id_master = self.get_or_create_id_master(table_name)
        
        # Create RoundMaster instance
        round_master = RoundMaster(
            round_number=round_number,
            start_time=start_time,
            end_time=end_time,
            is_morning=is_morning,
            delete_flag=False,
            update_time=datetime.now(),
            id_master_id=id_master.id,
            parameter_master_id=None  # Set this if needed
        )
        
        return round_master

    def get_or_create(self, round_number: int, is_morning: int, table_name: str) -> RoundMaster:
        """
        Get or create RoundMaster record with proper relationships
        """
        # Get start and end times
        start_time, end_time = self.get_round_times(round_number, is_morning)
        
        # Get or create IdMaster record
        id_master = self.id_master_mapper.get_or_create(table_name)
        
        # Check if RoundMaster record exists
        stmt = select(RoundMaster).where(
            RoundMaster.round_number == round_number,
            RoundMaster.is_morning == is_morning,
            RoundMaster.delete_flag == False
        )
        round_master = self.session.execute(stmt).scalar_one_or_none()
        
        if not round_master:
            # Create new RoundMaster record
            round_master = RoundMaster(
                round_number=round_number,
                start_time=start_time,
                end_time=end_time,
                is_morning=is_morning,
                delete_flag=False,
                update_time=datetime.now(),
                id_master_id=id_master.id
            )
            self.session.add(round_master)
            self.session.flush()
        
        return round_master

    def get_round_times(self, round_number: int, is_morning: int) -> tuple:
        """
        Returns start and end times for a given round and shift
        """
        round_times = {
            (1, 0): ('06:30', '07:30'),
            (1, 1): ('17:10', '18:10'),
            (2, 0): ('07:30', '08:30'),
            (2, 1): ('18:10', '19:10'),
            (3, 0): ('08:40', '09:40'),
            (3, 1): ('19:20', '20:20'),
            (4, 0): ('09:40', '10:40'),
            (4, 1): ('20:20', '21:20'),
            (5, 0): ('11:30', '12:30'),
            (5, 1): ('22:10', '23:10'),
            (6, 0): ('12:30', '13:30'),
            (6, 1): ('23:10', '24:10'),
            (7, 0): ('13:40', '14:40'),
            (7, 1): ('00:20', '01:20'),
            (8, 0): ('14:40', '15:10'),
            (8, 1): ('01:20', '01:50'),
            (9, 0): ('15:20', '16:20'),
            (9, 1): ('02:00', '03:00'),
            (10, 0): ('16:20', '17:00'),
            (10, 1): ('03:10', '06:10'),
        }
        
        return round_times.get((round_number, is_morning))

# Khởi tạo engine và tạo các bảng trong cơ sở dữ liệu
engine = create_engine('postgresql://postgres:12345@localhost:5432/test_db')

# Tạo các bảng trong cơ sở dữ liệu nếu chưa tồn tại
Base.metadata.create_all(engine)

# Tạo session để tương tác với cơ sở dữ liệu
Session = sessionmaker(bind=engine)
session = Session()

# Đóng session khi không sử dụng nữa
session.close()
