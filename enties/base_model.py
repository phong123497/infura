from sqlalchemy import Column, Integer, SmallInteger, Boolean, TIMESTAMP
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class BaseModel(Base):
    __abstract__ = True  # This ensures SQLAlchemy doesn't create a table for this class
    round = Column(SmallInteger)
    round_update = Column(Boolean, default=False)
    is_morning = Column(SmallInteger)
    year = Column(SmallInteger)
    month = Column(SmallInteger)
    day = Column(SmallInteger)
    hour = Column(SmallInteger)
    minute = Column(SmallInteger)
    update_time = Column(TIMESTAMP, nullable=False, default="CURRENT_TIMESTAMP")
    delete_flag = Column(Boolean, default=False) 


