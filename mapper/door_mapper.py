from enties.door import DoorPageData1, DoorPageData2
from .base_mapper import BaseMapper


class DoorPageData1Mapper(BaseMapper):
    def map_to_model(self, row):
        door_ins = DoorPageData1()
        door_ins = self.map_common_fields(row, door_ins)
        door_ins.f_dr_daisu=row['f_dr_daisu'],
        door_ins.f_dl_daisu=row['f_dl_daisu'],
        door_ins.s_dr_daisu=row['s_dr_daisu'],
        door_ins.s_dl_daisu=row['s_dl_daisu'],
        door_ins.food_daisu=row['food_daisu'],
        door_ins.b_d_daisu=row['b_d_daisu'],
        door_ins.f_dr_em_time=row['f_dr_em_time'],
        door_ins.f_dl_em_time=row['f_dl_em_time'],
        door_ins.s_dr_em_time=row['s_dr_em_time'],
        door_ins.s_dl_em_time=row['s_dl_em_time'],
        door_ins.food_em_time=row['food_em_time'],
        door_ins.b_d_em_time=row['b_d_em_time'],
        door_ins.f_dr_boman=row['f_dr_boman'],
        door_ins.f_dl_boman=row['f_dl_boman'],
        door_ins.s_dr_boman=row['s_dr_boman'],
        door_ins.s_dl_boman=row['s_dl_boman'],
        door_ins.food_boman=row['food_boman'],
        door_ins.b_d_boman=row['b_d_boman'],
        door_ins.f_dr_boketsu=row['f_dr_boketsu'],
        door_ins.f_dl_boketsu=row['f_dl_boketsu'],
        door_ins.s_dr_boketsu=row['s_dr_boketsu'],
        door_ins.s_dl_boketsu=row['s_dl_boketsu'],
        door_ins.food_boketsu=row['food_boketsu'],
        door_ins.b_d_boketsu=row['b_d_boketsu'],
        door_ins.f_dr_shokusei_yobidashi=row['f_dr_shokusei_yobidashi'],
        door_ins.f_dl_shokusei_yobidashi=row['f_dl_shokusei_yobidashi'],
        door_ins.s_dr_shokusei_yobidashi=row['s_dr_shokusei_yobidashi'],
        door_ins.s_dl_shokusei_yobidashi=row['s_dl_shokusei_yobidashi'],
        door_ins.food_shokusei_yobidashi=row['food_shokusei_yobidashi'],
        door_ins.b_d_shokusei_yobidashi=row['b_d_shokusei_yobidashi'],
        door_ins.f_dr_sei_yobidashi=row['f_dr_sei_yobidashi'],
        door_ins.f_dl_sei_yobidashi=row['f_dl_sei_yobidashi'],
        door_ins.s_dr_sei_yobidashi=row['s_dr_sei_yobidashi'],
        door_ins.s_dl_sei_yobidashi=row['s_dl_sei_yobidashi'],
        door_ins.food_sei_yobidashi=row['food_sei_yobidashi'],
        door_ins.b_d_sei_yobidashi=row['b_d_sei_yobidashi']
        return door_ins

class DoorPageData2Mapper(BaseMapper):
    def map_to_model(self, row):
        model_instance = DoorPageData2()
        model_instance = self.map_common_fields(row, model_instance)
        model_instance.fender_daisu = row['fender_daisu']
        model_instance.sps_daisu = row['sps_daisu']
        model_instance.fender_em_time = row['fender_em_time']
        model_instance.sps_em_time = row['sps_em_time']
        model_instance.fender_boman = row['fender_boman']
        model_instance.sps_boman = row['sps_boman']
        model_instance.fender_boketsu = row['fender_boketsu']
        model_instance.sps_boketsu = row['sps_boketsu']
        model_instance.fender_shokusei_yobidashi = row['fender_shokusei_yobidashi']
        model_instance.sps_shokusei_yobidashi = row['sps_shokusei_yobidashi']
        model_instance.fender_sei_yobidashi = row['fender_sei_yobidashi']
        model_instance.sps_sei_yobidashi = row['sps_sei_yobidashi']
        return model_instance

