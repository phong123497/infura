from sqlalchemy import Column, Integer, SmallInteger, Boolean, TIMESTAMP
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class BaseModel(Base):
    __abstract__ = True  # This ensures SQLAlchemy doesn't create a table for this class
    round = Column(SmallInteger)
    round_update = Column(Boolean, default=False, index=True)
    is_morning = Column(SmallInteger)
    year = Column(SmallInteger, index=True)
    month = Column(SmallInteger,index=True)
    day = Column(SmallInteger,index=True)
    hour = Column(SmallInteger, index=True)
    minute = Column(SmallInteger,index=True)
    update_time = Column(TIMESTAMP, nullable=False, default="CURRENT_TIMESTAMP", index=True)
    delete_flag = Column(Boolean, default=False,index=True) 


