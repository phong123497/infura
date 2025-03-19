from sqlalchemy import Column, Integer, SmallInteger, TIMESTAMP, Boolean
from datetime import datetime
from enties.base_model import BaseModel


class NdaiPageData(BaseModel):
    __tablename__ = 'ndai_page_data'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    mbm_kotei_ryuju_no = Column(Integer)
    mbm_kotei_renban = Column(Integer)
    mbm_kotei_shashu = Column(Integer)
    mbk1kotei_ub_paretto_no = Column(Integer)
    mbk1kotei_shashu = Column(Integer)
    mbk1kotei_renban = Column(Integer)
    mbk1kotei_uke_koma_no = Column(Integer)
    mbk2kotei_dl_matehanshashu = Column(Integer)
    mbk2kotei_renban = Column(Integer)
    sm_auta_rl1kotei_670_sukitto_no = Column(Integer)
    sm_auta_rl1kotei_shashu = Column(Integer)
    sm_auta_rl1kotei_renban = Column(Integer)
    sm_auta_rl1kotei_670_shashu = Column(Integer)
    sm_auta_rl1kotei_970_shashu = Column(Integer)
    sm_sukiba_rl_kotei_shushu_jikan = Column(Integer)
    sm_sukiba_rl_kotei_shashu = Column(Integer)
    sm_sukiba_rl_kotei_renban = Column(Integer)
    sm_sukiba_rl_kotei_sukitto_no = Column(Integer)
    s_drl_kotei_shashu = Column(Integer)
    s_drl_kotei_renban = Column(Integer)
    s_drl_kotei_kaiten_jigu_no = Column(Integer)
    b_d_kotei_shashu = Column(Integer)
    b_d_kotei_renban = Column(Integer)
    b_d_kotei_kaiten_jigu_no = Column(Integer)
    e_c_kotei_shashu = Column(Integer)
    e_c_kotei_renban = Column(Integer)
    e_c_kotei_sukitto_no = Column(Integer)
    rr_u_kotei_shashu = Column(Integer)
    rr_u_kotei_renban = Column(Integer)
    rr_u_kotei_sukitto_no = Column(Integer)
    ctrr_kotei_shashu = Column(Integer)
    ctrr_kotei_renban = Column(Integer)
    ctrr_kotei_sukitto_no = Column(Integer)

    