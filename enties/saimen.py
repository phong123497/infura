from sqlalchemy import create_engine, Column, Integer
from enties.base_model import BaseModel

class SmPageData1(BaseModel):
    __tablename__ = 'sm_page_data1'
    
    id = Column(Integer, primary_key=True)
    smr_daisu = Column(Integer)
    sml_daisu = Column(Integer)
    roof_daisu = Column(Integer)
    header_daisu = Column(Integer)
    outer_r_daisu = Column(Integer)
    outer_l_daisu = Column(Integer)
    smr_em_time = Column(Integer)
    sml_em_time = Column(Integer)
    roof_em_time = Column(Integer)
    header_em_time = Column(Integer)
    outer_r_em_time = Column(Integer)
    outer_l_em_time = Column(Integer)
    smr_boman = Column(Integer)
    sml_boman = Column(Integer)
    roof_boman = Column(Integer)
    header_boman = Column(Integer)
    outer_r_boman = Column(Integer)
    outer_l_boman = Column(Integer)
    smr_boketsu = Column(Integer)
    sml_boketsu = Column(Integer)
    roof_boketsu = Column(Integer)
    header_boketsu = Column(Integer)
    outer_r_boketsu = Column(Integer)
    outer_l_boketsu = Column(Integer)
    smr_shokusei_yobidashi = Column(Integer)
    sml_shokusei_yobidashi = Column(Integer)
    roof_shokusei_yobidashi = Column(Integer)
    header_shokusei_yobidashi = Column(Integer)
    outer_r_shokusei_yobidashi = Column(Integer)
    outer_l_shokusei_yobidashi = Column(Integer)
    smr_sei_yobidashi = Column(Integer)
    sml_sei_yobidashi = Column(Integer)
    roof_sei_yobidashi = Column(Integer)
    header_sei_yobidashi = Column(Integer)
    outer_r_sei_yobidashi = Column(Integer)
    outer_l_sei_yobidashi = Column(Integer)
    
# Define the `sm_page_data2` table
class SmPageData2(BaseModel):
    __tablename__ = 'sm_page_data2'
    
    id = Column(Integer, primary_key=True)
    inner_r_daisu = Column(Integer)
    inner_l_daisu = Column(Integer)
    cprfr_daisu = Column(Integer)
    cprfl_daisu = Column(Integer)
    transport_daisu = Column(Integer)
    inner_r_em_time = Column(Integer)
    inner_l_em_time = Column(Integer)
    cprfr_em_time = Column(Integer)
    cprfl_em_time = Column(Integer)
    transport_em_time = Column(Integer)
    inner_r_boman = Column(Integer)
    inner_l_boman = Column(Integer)
    cprfr_boman = Column(Integer)
    cprfl_boman = Column(Integer)
    transport_boman = Column(Integer)
    inner_r_boketsu = Column(Integer)
    inner_l_boketsu = Column(Integer)
    cprfr_boketsu = Column(Integer)
    cprfl_boketsu = Column(Integer)
    transport_boketsu = Column(Integer)
    inner_r_shokusei_yobidashi = Column(Integer)
    inner_l_shokusei_yobidashi = Column(Integer)
    cprfr_shokusei_yobidashi = Column(Integer)
    cprfl_shokusei_yobidashi = Column(Integer)
    transport_shokusei_yobidashi = Column(Integer)
    inner_r_sei_yobidashi = Column(Integer)
    inner_l_sei_yobidashi = Column(Integer)
    cprfr_sei_yobidashi = Column(Integer)
    cprfl_sei_yobidashi = Column(Integer)
    transport_sei_yobidashi = Column(Integer)
   
class SmPageData1Mapper:
    def map_to_model(self, row):
        return SmPageData1(
            round=row['round'],
            round_update=row['round_update'],
            is_morning=row['is_morning'],
            year=row['year'],
            month=row['month'],
            day=row['day'],
            hour=row['hour'],
            minute=row['minute'],
            smr_daisu=row['smr_daisu'],
            sml_daisu=row['sml_daisu'],
            roof_daisu=row['roof_daisu'],
            header_daisu=row['header_daisu'],
            outer_r_daisu=row['outer_r_daisu'],
            outer_l_daisu=row['outer_l_daisu'],
            smr_em_time=row['smr_em_time'],
            sml_em_time=row['sml_em_time'],
            roof_em_time=row['roof_em_time'],
            header_em_time=row['header_em_time'],
            outer_r_em_time=row['outer_r_em_time'],
            outer_l_em_time=row['outer_l_em_time'],
            smr_boman=row['smr_boman'],
            sml_boman=row['sml_boman'],
            roof_boman=row['roof_boman'],
            header_boman=row['header_boman'],
            outer_r_boman=row['outer_r_boman'],
            outer_l_boman=row['outer_l_boman'],
            smr_boketsu=row['smr_boketsu'],
            sml_boketsu=row['sml_boketsu'],
            roof_boketsu=row['roof_boketsu'],
            header_boketsu=row['header_boketsu'],
            outer_r_boketsu=row['outer_r_boketsu'],
            outer_l_boketsu=row['outer_l_boketsu'],
            smr_shokusei_yobidashi=row['smr_shokusei_yobidashi'],
            sml_shokusei_yobidashi=row['sml_shokusei_yobidashi'],
            roof_shokusei_yobidashi=row['roof_shokusei_yobidashi'],
            header_shokusei_yobidashi=row['header_shokusei_yobidashi'],
            outer_r_shokusei_yobidashi=row['outer_r_shokusei_yobidashi'],
            outer_l_shokusei_yobidashi=row['outer_l_shokusei_yobidashi'],
            smr_sei_yobidashi=row['smr_sei_yobidashi'],
            sml_sei_yobidashi=row['sml_sei_yobidashi'],
            roof_sei_yobidashi=row['roof_sei_yobidashi'],
            header_sei_yobidashi=row['header_sei_yobidashi'],
            outer_r_sei_yobidashi=row['outer_r_sei_yobidashi'],
            outer_l_sei_yobidashi=row['outer_l_sei_yobidashi']
        )

class SmPageData2Mapper:
    def map_to_model(self, row):
        return SmPageData2(
            # Add the appropriate fields here
        )