from sqlalchemy import Column, Integer, BigInteger, String, SmallInteger, Time, TIMESTAMP, select
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

Base = declarative_base()

# id_master define
class IdMaster(Base):
    __tablename__ = 'id_master'
    id = Column(BigInteger, primary_key=True, autoincrement=True)
    created_at = Column(TIMESTAMP, nullable=False, default=datetime.now, index=True)
    delete_flag = Column(SmallInteger, nullable=False, default=0)

#  parameter_maste define
class ParameterMaster(Base):
    __tablename__ = 'parameter_master'
    
    parameter_id = Column(Integer, primary_key=True, autoincrement=True)
    parameter_name = Column(String(255), nullable=False)
    parameter_value = Column(String(255))
    created_at = Column(TIMESTAMP, nullable=False, default=datetime.now)
    delete_flag = Column(SmallInteger, nullable=False, default=0)

# round master define
class RoundMaster(Base):
    __tablename__ = 'round_master'
    
    round_id = Column(Integer, primary_key=True, autoincrement=True)
    round_number = Column(SmallInteger, nullable=False)
    start_time = Column(Time, nullable=False)
    end_time = Column(Time, nullable=False)
    is_morning = Column(SmallInteger)
    delete_flag = Column(SmallInteger, nullable=False, default=0)
    update_time = Column(TIMESTAMP, nullable=False, default=datetime.now)


class RoundMasterMapper:
    def map_to_fields(seld, row):
        return RoundMaster(
            round_number=row.get('round_number'),
            start_time=row.get('start_time'),
            end_time=row.get('end_time'),
            is_morning=row.get('is_morning'),
            delete_flag=row.get('delete_flag'),
            update_time=row.get('update_time'),
        )
