from sqlalchemy import Column, Integer, SmallInteger, String
from .base_model import BaseModel

from datetime import datetime


class NdaiPageData(BaseModel):
    __tablename__ = 'ndai_page_data'

    id = Column(Integer, primary_key=True, autoincrement=True)
    sample_kotei_ryuju_no = Column(Integer, nullable=True)
    sample_kotei_renban = Column(Integer, nullable=True)
    sample_kotei_shashu = Column(Integer, nullable=True)
    mbm_kotei_ryuju_no = Column(Integer, nullable=True)
    mbm_kotei_renban = Column(Integer, nullable=True)
    mbm_kotei_shashu = Column(Integer, nullable=True)
    mbk1kotei_ub_paretto_no = Column(Integer, nullable=True)
    mbk1kotei_shashu = Column(Integer, nullable=True)
    mbk1kotei_renban = Column(Integer, nullable=True)
    mbk2kotei_dl_matehanshashu = Column(Integer, nullable=True)
    mbk2kotei_renban = Column(Integer, nullable=True)
    sm_outer_l1kotei_670_sukitto_no = Column(Integer, nullable=True)
    sm_outer_l1kotei_shashu = Column(Integer, nullable=True)
    sm_outer_l1kotei_renban = Column(Integer, nullable=True)
    sm_outer_l1kotei_670_shashu = Column(Integer, nullable=True)
    sm_outer_l1kotei_970_shashu = Column(Integer, nullable=True)
    sm_outer_r1kotei_670_sukitto_no = Column(Integer, nullable=True)
    sm_outer_r1kotei_shashu = Column(Integer, nullable=True)
    sm_outer_r1kotei_renban = Column(Integer, nullable=True)
    sm_outer_r1kotei_670_shashu = Column(Integer, nullable=True)
    sm_outer_r1kotei_970_shashu = Column(Integer, nullable=True)
    sm_sukiba_l_kotei_shashu = Column(Integer, nullable=True)
    sm_sukiba_l_kotei_renban = Column(Integer, nullable=True)
    sm_sukiba_l_kotei_sukitto_no = Column(Integer, nullable=True)
    sm_sukiba_r_kotei_shashu = Column(Integer, nullable=True)
    sm_sukiba_r_kotei_renban = Column(Integer, nullable=True)
    sm_sukiba_r_kotei_sukitto_no = Column(Integer, nullable=True)
    s_dl_kotei_shashu = Column(Integer, nullable=True)
    s_dl_kotei_renban = Column(Integer, nullable=True)
    s_dl_kotei_kaiten_jigu_no = Column(Integer, nullable=True)
    s_dr_kotei_shashu = Column(Integer, nullable=True)
    s_dr_kotei_renban = Column(Integer, nullable=True)
    s_dr_kotei_kaiten_jigu_no = Column(Integer, nullable=True)
    b_d_kotei_shashu = Column(Integer, nullable=True)
    b_d_kotei_renban = Column(Integer, nullable=True)
    b_d_kotei_kaiten_jigu_no = Column(Integer, nullable=True)
    e_c_kotei_shashu = Column(Integer, nullable=True)
    e_c_kotei_renban = Column(Integer, nullable=True)
    e_c_kotei_sukitto_no = Column(Integer, nullable=True)
    rr_u_kotei_shashu = Column(Integer, nullable=True)
    rr_u_kotei_renban = Column(Integer, nullable=True)
    rr_u_kotei_sukitto_no = Column(Integer, nullable=True)
    ctrr_kotei_shashu = Column(Integer, nullable=True)
    ctrr_kotei_renban = Column(Integer, nullable=True)
    ctrr_kotei_sukitto_no = Column(Integer, nullable=True)
    A_ukekoma_data= Column(String(10), nullable=True)
    B_ukekoma_data= Column(String(10), nullable=True)
    C_ukekoma_data= Column(String(10), nullable=True)
    D_ukekoma_data= Column(String(10), nullable=True)
    
    

    