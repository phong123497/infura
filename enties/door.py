from sqlalchemy import  Column, Integer
from .base_model import BaseModel

class DoorPageData1(BaseModel):
    __tablename__ = 'door_page_data1'
    id = Column(Integer, primary_key=True)
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

# Define the `door_page_data2` table
class DoorPageData2(BaseModel):
    __tablename__ = 'door_page_data2'
    id = Column(Integer, primary_key=True)
    fender_daisu = Column(Integer)
    sps_daisu = Column(Integer)
    fender_em_time = Column(Integer)
    sps_em_time = Column(Integer)
    fender_boman = Column(Integer)
    sps_boman = Column(Integer)
    fender_boketsu = Column(Integer)
    sps_boketsu = Column(Integer)
    fender_shokusei_yobidashi = Column(Integer)
    sps_shokusei_yobidashi = Column(Integer)
    fender_sei_yobidashi = Column(Integer)
    sps_sei_yobidashi = Column(Integer)




