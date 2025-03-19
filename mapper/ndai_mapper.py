from enties.ndai import NdaiPageData
from .base_mapper import BaseMapper


class NdaiPageDataMapper(BaseMapper):
    def map_to_model(self, row):
        model_instance = NdaiPageData()
        model_instance = self.map_common_fields(row, model_instance)
        model_instance.mbm_kotei_ryuju_no = row['mbm_kotei_ryuju_no']
        model_instance.mbm_kotei_renban = row['mbm_kotei_renban']
        model_instance.mbm_kotei_shashu = row['mbm_kotei_shashu']
        model_instance.mbk1kotei_ub_paretto_no = row['mbk1kotei_ub_paretto_no']
        model_instance.mbk1kotei_shashu = row['mbk1kotei_shashu']
        model_instance.mbk1kotei_renban = row['mbk1kotei_renban']
        model_instance.mbk1kotei_uke_koma_no = row['mbk1kotei_uke_koma_no']
        model_instance.mbk2kotei_dl_matehanshashu = row['mbk2kotei_dl_matehanshashu']
        model_instance.mbk2kotei_renban = row['mbk2kotei_renban']
        model_instance.sm_auta_rl1kotei_670_sukitto_no = row['sm_auta_rl1kotei_670_sukitto_no']
        model_instance.sm_auta_rl1kotei_shashu = row['sm_auta_rl1kotei_shashu']
        model_instance.sm_auta_rl1kotei_renban = row['sm_auta_rl1kotei_renban']
        model_instance.sm_auta_rl1kotei_670_shashu = row['sm_auta_rl1kotei_670_shashu']
        model_instance.sm_auta_rl1kotei_970_shashu = row['sm_auta_rl1kotei_970_shashu']
        model_instance.sm_sukiba_rl_kotei_shushu_jikan = row['sm_sukiba_rl_kotei_shushu_jikan']
        model_instance.sm_sukiba_rl_kotei_shashu = row['sm_sukiba_rl_kotei_shashu']
        model_instance.sm_sukiba_rl_kotei_renban = row['sm_sukiba_rl_kotei_renban']
        model_instance.sm_sukiba_rl_kotei_sukitto_no = row['sm_sukiba_rl_kotei_sukitto_no']
        model_instance.s_drl_kotei_shashu = row['s_drl_kotei_shashu']
        model_instance.s_drl_kotei_renban = row['s_drl_kotei_renban']
        model_instance.s_drl_kotei_kaiten_jigu_no = row['s_drl_kotei_kaiten_jigu_no']
        model_instance.b_d_kotei_shashu = row['b_d_kotei_shashu']
        model_instance.b_d_kotei_renban = row['b_d_kotei_renban']
        model_instance.b_d_kotei_kaiten_jigu_no = row['b_d_kotei_kaiten_jigu_no']
        model_instance.e_c_kotei_shashu = row['e_c_kotei_shashu']
        model_instance.e_c_kotei_renban = row['e_c_kotei_renban']
        model_instance.e_c_kotei_sukitto_no = row['e_c_kotei_sukitto_no']
        model_instance.rr_u_kotei_shashu = row['rr_u_kotei_shashu']
        model_instance.rr_u_kotei_renban = row['rr_u_kotei_renban']
        model_instance.rr_u_kotei_sukitto_no = row['rr_u_kotei_sukitto_no']
        model_instance.ctrr_kotei_shashu = row['ctrr_kotei_shashu']
        model_instance.ctrr_kotei_renban = row['ctrr_kotei_renban']
        model_instance.ctrr_kotei_sukitto_no = row['ctrr_kotei_sukitto_no']
        return model_instance
