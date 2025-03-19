from enties.saimen import  SmPageData1, SmPageData2
from .base_mapper import BaseMapper


class SmPageData1Mapper(BaseMapper):
   def map_to_model(self, row):
        model_instance = SmPageData1()
        model_instance = self.map_common_fields(row, model_instance)
        model_instance.smr_daisu = row['smr_daisu']
        model_instance.sml_daisu = row['sml_daisu']
        model_instance.roof_daisu = row['roof_daisu']
        model_instance.header_daisu = row['header_daisu']
        model_instance.outer_r_daisu = row['outer_r_daisu']
        model_instance.outer_l_daisu = row['outer_l_daisu']
        model_instance.smr_em_time = row['smr_em_time']
        model_instance.sml_em_time = row['sml_em_time']
        model_instance.roof_em_time = row['roof_em_time']
        model_instance.header_em_time = row['header_em_time']
        model_instance.outer_r_em_time = row['outer_r_em_time']
        model_instance.outer_l_em_time = row['outer_l_em_time']
        model_instance.smr_boman = row['smr_boman']
        model_instance.sml_boman = row['sml_boman']
        model_instance.roof_boman = row['roof_boman']
        model_instance.header_boman = row['header_boman']
        model_instance.outer_r_boman = row['outer_r_boman']
        model_instance.outer_l_boman = row['outer_l_boman']
        model_instance.smr_boketsu = row['smr_boketsu']
        model_instance.sml_boketsu = row['sml_boketsu']
        model_instance.roof_boketsu = row['roof_boketsu']
        model_instance.header_boketsu = row['header_boketsu']
        model_instance.outer_r_boketsu = row['outer_r_boketsu']
        model_instance.outer_l_boketsu = row['outer_l_boketsu']
        model_instance.smr_shokusei_yobidashi = row['smr_shokusei_yobidashi']
        model_instance.sml_shokusei_yobidashi = row['sml_shokusei_yobidashi']
        model_instance.roof_shokusei_yobidashi = row['roof_shokusei_yobidashi']
        model_instance.header_shokusei_yobidashi = row['header_shokusei_yobidashi']
        model_instance.outer_r_shokusei_yobidashi = row['outer_r_shokusei_yobidashi']
        model_instance.outer_l_shokusei_yobidashi = row['outer_l_shokusei_yobidashi']
        model_instance.smr_sei_yobidashi = row['smr_sei_yobidashi']
        model_instance.sml_sei_yobidashi = row['sml_sei_yobidashi']
        model_instance.roof_sei_yobidashi = row['roof_sei_yobidashi']
        model_instance.header_sei_yobidashi = row['header_sei_yobidashi']
        model_instance.outer_r_sei_yobidashi = row['outer_r_sei_yobidashi']
        model_instance.outer_l_sei_yobidashi = row['outer_l_sei_yobidashi']
        return model_instance

class SmPageData2Mapper(BaseMapper):
   def map_to_model(self, row):
        model_instance = SmPageData2()
        model_instance = self.map_common_fields(row, model_instance)
        model_instance.inner_r_daisu = row['inner_r_daisu']
        model_instance.inner_l_daisu = row['inner_l_daisu']
        model_instance.cprfr_daisu = row['cprfr_daisu']
        model_instance.cprfl_daisu = row['cprfl_daisu']
        model_instance.transport_daisu = row['transport_daisu']
        model_instance.inner_r_em_time = row['inner_r_em_time']
        model_instance.inner_l_em_time = row['inner_l_em_time']
        model_instance.cprfr_em_time = row['cprfr_em_time']
        model_instance.cprfl_em_time = row['cprfl_em_time']
        model_instance.transport_em_time = row['transport_em_time']
        model_instance.inner_r_boman = row['inner_r_boman']
        model_instance.inner_l_boman = row['inner_l_boman']
        model_instance.cprfr_boman = row['cprfr_boman']
        model_instance.cprfl_boman = row['cprfl_boman']
        model_instance.transport_boman = row['transport_boman']
        model_instance.inner_r_boketsu = row['inner_r_boketsu']
        model_instance.inner_l_boketsu = row['inner_l_boketsu']
        model_instance.cprfr_boketsu = row['cprfr_boketsu']
        model_instance.cprfl_boketsu = row['cprfl_boketsu']
        model_instance.transport_boketsu = row['transport_boketsu']
        model_instance.inner_r_shokusei_yobidashi = row['inner_r_shokusei_yobidashi']
        model_instance.inner_l_shokusei_yobidashi = row['inner_l_shokusei_yobidashi']
        model_instance.cprfr_shokusei_yobidashi = row['cprfr_shokusei_yobidashi']
        model_instance.cprfl_shokusei_yobidashi = row['cprfl_shokusei_yobidashi']
        model_instance.transport_shokusei_yobidashi = row['transport_shokusei_yobidashi']
        model_instance.inner_r_sei_yobidashi = row['inner_r_sei_yobidashi']
        model_instance.inner_l_sei_yobidashi = row['inner_l_sei_yobidashi']
        model_instance.cprfr_sei_yobidashi = row['cprfr_sei_yobidashi']
        model_instance.cprfl_sei_yobidashi = row['cprfl_sei_yobidashi']
        model_instance.transport_sei_yobidashi = row['transport_sei_yobidashi']
        return model_instance



