from enties.door import DoorPageData1, DoorPageData2
from .base_mapper import BaseMapper


class DoorPageData1Mapper(BaseMapper):
    def map_to_model(self, row):
        door_ins = DoorPageData1()
        door_ins = self.map_common_fields(row, door_ins)
        door_ins.f_dr_daisu = row.get('f_dr_daisu_door', 0)
        door_ins.f_dl_daisu = row.get('f_dl_daisu_door', 0)
        door_ins.s_dr_daisu = row.get('s_dr_daisu_door', 0)
        door_ins.s_dl_daisu = row.get('s_dl_daisu_door', 0)
        door_ins.food_daisu = row.get('food_daisu_door', 0)
        door_ins.b_d_daisu = row.get('b_d_daisu_door', 0)
        door_ins.f_dr_em_time = row.get('f_dr_em_time_door', 0)
        door_ins.f_dl_em_time = row.get('f_dl_em_time_door', 0)
        door_ins.s_dr_em_time = row.get('s_dr_em_time_door', 0)
        door_ins.s_dl_em_time = row.get('s_dl_em_time_door', 0)
        door_ins.food_em_time = row.get('food_em_time_door', 0)
        door_ins.b_d_em_time = row.get('b_d_em_time_door', 0)
        door_ins.f_dr_boman = row.get('f_dr_boman_door', 0)
        door_ins.f_dl_boman = row.get('f_dl_boman_door', 0)
        door_ins.s_dr_boman = row.get('s_dr_boman_door', 0)
        door_ins.s_dl_boman = row.get('s_dl_boman_door', 0)
        door_ins.food_boman = row.get('food_boman_door', 0)
        door_ins.b_d_boman = row.get('b_d_boman_door', 0)
        door_ins.f_dr_boketsu = row.get('f_dr_boketsu_door', 0)
        door_ins.f_dl_boketsu = row.get('f_dl_boketsu_door', 0)
        door_ins.s_dr_boketsu = row.get('s_dr_boketsu_door', 0)
        door_ins.s_dl_boketsu = row.get('s_dl_boketsu_door', 0)
        door_ins.food_boketsu = row.get('food_boketsu_door', 0)
        door_ins.b_d_boketsu = row.get('b_d_boketsu_door', 0)
        door_ins.f_dr_shokusei_yobidashi = row.get('f_dr_shokusei_yobidashi_door', 0)
        door_ins.f_dl_shokusei_yobidashi = row.get('f_dl_shokusei_yobidashi_door', 0)
        door_ins.s_dr_shokusei_yobidashi = row.get('s_dr_shokusei_yobidashi_door', 0)
        door_ins.s_dl_shokusei_yobidashi = row.get('s_dl_shokusei_yobidashi_door', 0)
        door_ins.food_shokusei_yobidashi = row.get('food_shokusei_yobidashi_door', 0)
        door_ins.b_d_shokusei_yobidashi = row.get('b_d_shokusei_yobidashi_door', 0)
        door_ins.f_dr_sei_yobidashi = row.get('f_dr_sei_yobidashi_door', 0)
        door_ins.f_dl_sei_yobidashi = row.get('f_dl_sei_yobidashi_door', 0)
        door_ins.s_dr_sei_yobidashi = row.get('s_dr_sei_yobidashi_door', 0)
        door_ins.s_dl_sei_yobidashi = row.get('s_dl_sei_yobidashi_door', 0)
        door_ins.food_sei_yobidashi = row.get('food_sei_yobidashi_door', 0)
        door_ins.b_d_sei_yobidashi = row.get('b_d_sei_yobidashi_door', 0)

        return door_ins

class DoorPageData2Mapper(BaseMapper):
    def map_to_model(self, row):
        model_instance = DoorPageData2()
        model_instance = self.map_common_fields(row, model_instance)
        model_instance.fender_daisu = row.get('fender_daisu_door', 0)
        model_instance.sps_daisu = row.get('sps_daisu_door', 0)
        model_instance.fender_em_time = row.get('fender_em_time_door', 0)
        model_instance.sps_em_time = row.get('sps_em_time_door', 0)
        model_instance.fender_boman = row.get('fender_boman_door', 0)
        model_instance.sps_boman = row.get('sps_boman_door', 0)
        model_instance.fender_boketsu = row.get('fender_boketsu_door', 0)
        model_instance.sps_boketsu = row.get('sps_boketsu_door', 0)
        model_instance.fender_shokusei_yobidashi = row.get('fender_shokusei_yobidashi_door', 0)
        model_instance.sps_shokusei_yobidashi = row.get('sps_shokusei_yobidashi_door', 0)
        model_instance.fender_sei_yobidashi = row.get('fender_sei_yobidashi_door', 0)
        model_instance.sps_sei_yobidashi = row.get('sps_sei_yobidashi_door', 0)
        return model_instance
