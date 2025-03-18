from enties.under_body import UnderBodyPageData1, UnderBodyPageData2, UnderBodyPageData3
from .base_mapper import BaseMapper



class UnderBodyPageData1Mapper(BaseMapper):
    def map_to_model(self, row):
            model_instance = UnderBodyPageData1()
            model_instance = self.map_common_fields(row, model_instance)
            model_instance.frfr_r_daisu=row['frfr_r_daisu'],
            model_instance.frfr_l_daisu=row['frfr_l_daisu'],
            model_instance.apron_r_daisu=row['apron_r_daisu'],
            model_instance.apron_l_daisu=row['apron_l_daisu'],
            model_instance.inner_r_daisu=row['inner_r_daisu'],
            model_instance.inner_l_daisu=row['inner_l_daisu'],
            model_instance.frfr_r_em_time=row['frfr_r_em_time'],
            model_instance.frfr_l_em_time=row['frfr_l_em_time'],
            model_instance.apron_r_em_time=row['apron_r_em_time'],
            model_instance.apron_l_em_time=row['apron_l_em_time'],
            model_instance.inner_r_em_time=row['inner_r_em_time'],
            model_instance.inner_l_em_time=row['inner_l_em_time'],
            model_instance.frfr_r_boman=row['frfr_r_boman'],
            model_instance.frfr_l_boman=row['frfr_l_boman'],
            model_instance.apron_r_boman=row['apron_r_boman'],
            model_instance.apron_l_boman=row['apron_l_boman'],
            model_instance.inner_r_boman=row['inner_r_boman'],
            model_instance.inner_l_boman=row['inner_l_boman'],
            model_instance.frfr_r_boketsu=row['frfr_r_boketsu'],
            model_instance.frfr_l_boketsu=row['frfr_l_boketsu'],
            model_instance.apron_r_boketsu=row['apron_r_boketsu'],
            model_instance.apron_l_boketsu=row['apron_l_boketsu'],
            model_instance.inner_r_boketsu=row['inner_r_boketsu'],
            model_instance.inner_l_boketsu=row['inner_l_boketsu'],
            model_instance.frfr_r_shokusei_yobidashi=row['frfr_r_shokusei_yobidashi'],
            model_instance.frfr_l_shokusei_yobidashi=row['frfr_l_shokusei_yobidashi'],
            model_instance.apron_r_shokusei_yobidashi=row['apron_r_shokusei_yobidashi'],
            model_instance.apron_l_shokusei_yobidashi=row['apron_l_shokusei_yobidashi'],
            model_instance.inner_r_shokusei_yobidashi=row['inner_r_shokusei_yobidashi'],
            model_instance.inner_l_shokusei_yobidashi=row['inner_l_shokusei_yobidashi'],
            model_instance.frfr_r_sei_yobidashi=row['frfr_r_sei_yobidashi'],
            model_instance.frfr_l_sei_yobidashi=row['frfr_l_sei_yobidashi'],
            model_instance.apron_r_sei_yobidashi=row['apron_r_sei_yobidashi'],
            model_instance.apron_l_sei_yobidashi=row['apron_l_sei_yobidashi'],
            model_instance.inner_r_sei_yobidashi=row['inner_r_sei_yobidashi'],
            model_instance.inner_l_sei_yobidashi=row['inner_l_sei_yobidashi']
            return model_instance

class UnderBodyPageData2Mapper(BaseMapper):
    def map_to_model(self, row):
        model_instance = UnderBodyPageData2()
        model_instance = self.map_common_fields(row, model_instance)
        model_instance.fsmr_daisu = row['fsmr_daisu']
        model_instance.fsml_daisu = row['fsml_daisu']
        model_instance.dash_daisu = row['dash_daisu']
        model_instance.locker_daisu = row['locker_daisu']
        model_instance.rfloor_daisu = row['rfloor_daisu']
        model_instance.fsmr_em_time = row['fsmr_em_time']
        model_instance.fsml_em_time = row['fsml_em_time']
        model_instance.dash_em_time = row['dash_em_time']
        model_instance.locker_em_time = row['locker_em_time']
        model_instance.rfloor_em_time = row['rfloor_em_time']
        model_instance.fsmr_boman = row['fsmr_boman']
        model_instance.fsml_boman = row['fsml_boman']
        model_instance.dash_boman = row['dash_boman']
        model_instance.locker_boman = row['locker_boman']
        model_instance.rfloor_boman = row['rfloor_boman']
        model_instance.fsmr_boketsu = row['fsmr_boketsu']
        model_instance.fsml_boketsu = row['fsml_boketsu']
        model_instance.dash_boketsu = row['dash_boketsu']
        model_instance.locker_boketsu = row['locker_boketsu']
        model_instance.rfloor_boketsu = row['rfloor_boketsu']
        model_instance.fsmr_shokusei_yobidashi = row['fsmr_shokusei_yobidashi']
        model_instance.fsml_shokusei_yobidashi = row['fsml_shokusei_yobidashi']
        model_instance.dash_shokusei_yobidashi = row['dash_shokusei_yobidashi']
        model_instance.locker_shokusei_yobidashi = row['locker_shokusei_yobidashi']
        model_instance.rfloor_shokusei_yobidashi = row['rfloor_shokusei_yobidashi']
        model_instance.fsmr_sei_yobidashi = row['fsmr_sei_yobidashi']
        model_instance.fsml_sei_yobidashi = row['fsml_sei_yobidashi']
        model_instance.dash_sei_yobidashi = row['dash_sei_yobidashi']
        model_instance.locker_sei_yobidashi = row['locker_sei_yobidashi']
        model_instance.rfloor_sei_yobidashi = row['rfloor_sei_yobidashi']
        return model_instance

class UnderBodyPageData3Mapper(BaseMapper):
    def map_to_model(self, row):
        model_instance = UnderBodyPageData3()
        model_instance = self.map_common_fields(row, model_instance)
        model_instance.noa_e_c_daisu = row['noa_e_c_daisu']
        model_instance.al_e_c_daisu = row['al_e_c_daisu']
        model_instance.noa_ctr_daisu = row['noa_ctr_daisu']
        model_instance.al_ctr_daisu = row['al_ctr_daisu']
        model_instance.noa_r_u_daisu = row['noa_r_u_daisu']
        model_instance.al_r_u_daisu = row['al_r_u_daisu']
        model_instance.noa_e_c_em_time = row['noa_e_c_em_time']
        model_instance.al_e_c_em_time = row['al_e_c_em_time']
        model_instance.noa_ctr_em_time = row['noa_ctr_em_time']
        model_instance.al_ctr_em_time = row['al_ctr_em_time']
        model_instance.noa_r_u_em_time = row['noa_r_u_em_time']
        model_instance.al_r_u_em_time = row['al_r_u_em_time']
        model_instance.noa_e_c_boman = row['noa_e_c_boman']
        model_instance.al_e_c_boman = row['al_e_c_boman']
        model_instance.noa_ctr_boman = row['noa_ctr_boman']
        model_instance.al_ctr_boman = row['al_ctr_boman']
        model_instance.noa_r_u_boman = row['noa_r_u_boman']
        model_instance.al_r_u_boman = row['al_r_u_boman']
        model_instance.noa_e_c_boketsu = row['noa_e_c_boketsu']
        model_instance.al_e_c_boketsu = row['al_e_c_boketsu']
        model_instance.noa_ctr_boketsu = row['noa_ctr_boketsu']
        model_instance.al_ctr_boketsu = row['al_ctr_boketsu']
        model_instance.noa_r_u_boketsu = row['noa_r_u_boketsu']
        model_instance.al_r_u_boketsu = row['al_r_u_boketsu']
        model_instance.noa_e_c_shokusei_yobidashi = row['noa_e_c_shokusei_yobidashi']
        model_instance.al_e_c_shokusei_yobidashi = row['al_e_c_shokusei_yobidashi']
        model_instance.noa_ctr_shokusei_yobidashi = row['noa_ctr_shokusei_yobidashi']
        model_instance.al_ctr_shokusei_yobidashi = row['al_ctr_shokusei_yobidashi']
        model_instance.noa_r_u_shokusei_yobidashi = row['noa_r_u_shokusei_yobidashi']
        model_instance.al_r_u_shokusei_yobidashi = row['al_r_u_shokusei_yobidashi']
        model_instance.noa_e_c_sei_yobidashi = row['noa_e_c_sei_yobidashi']
        model_instance.al_e_c_sei_yobidashi = row['al_e_c_sei_yobidashi']
        model_instance.noa_ctr_sei_yobidashi = row['noa_ctr_sei_yobidashi']
        model_instance.al_ctr_sei_yobidashi = row['al_ctr_sei_yobidashi']
        model_instance.noa_r_u_sei_yobidashi = row['noa_r_u_sei_yobidashi']
        model_instance.al_r_u_sei_yobidashi = row['al_r_u_sei_yobidashi']
        return model_instance