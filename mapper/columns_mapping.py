id_master_columns = ['収集日時']
round_master_columns = ['round_number','start_time','end_time','is_morning','delete_flag', 'update_time']

# Common columns shared by all tables
common_columns = [
    'round_number', 'round_update', 'is_morning', 'year', 'month', 'day', 'hour', 'minute',
    'update_time', 'delete_flag', '収集日時', "hour_minute"
]

# Specific columns for each table
door1_columns = common_columns + [
    'f_dr_daisu_door', 'f_dl_daisu_door', 's_dr_daisu_door', 's_dl_daisu_door', 'food_daisu_door', 'b_d_daisu_door',
    'f_dr_em_time_door', 'f_dl_em_time_door', 's_dr_em_time_door', 's_dl_em_time_door', 'food_em_time_door', 'b_d_em_time_door',
    'f_dr_boman_door', 'f_dl_boman_door', 's_dr_boman_door', 's_dl_boman_door', 'food_boman_door', 'b_d_boman_door',
    'f_dr_boketsu_door', 'f_dl_boketsu_door', 's_dr_boketsu_door', 's_dl_boketsu_door', 'food_boketsu_door', 'b_d_boketsu_door',
    'f_dr_shokusei_yobidashi_door', 'f_dl_shokusei_yobidashi_door', 's_dr_shokusei_yobidashi_door', 's_dl_shokusei_yobidashi_door', 'food_shokusei_yobidashi_door', 'b_d_shokusei_yobidashi_door',
    'f_dr_sei_yobidashi_door', 'f_dl_sei_yobidashi_door', 's_dr_sei_yobidashi_door', 's_dl_sei_yobidashi_door', 'food_sei_yobidashi_door', 'b_d_sei_yobidashi_door'
]

door2_columns = common_columns + [
    'fender_daisu_door', 'sps_daisu_door',
    'fender_em_time_door', 'sps_em_time_door',
    'fender_boman_door', 'sps_boman_door',
    'fender_boketsu_door', 'sps_boketsu_door',
    'fender_shokusei_yobidashi_door', 'sps_shokusei_yobidashi_door',
    'fender_sei_yobidashi_door', 'sps_sei_yobidashi_door'
]

under_body1_columns = common_columns + [
    'frfr_r_daisu_ub', 'frfr_l_daisu_ub', 'apron_r_daisu_ub', 'apron_l_daisu_ub', 'inner_r_daisu_ub', 'inner_l_daisu_ub',
    'frfr_r_em_time_ub', 'frfr_l_em_time_ub', 'apron_r_em_time_ub', 'apron_l_em_time_ub', 'inner_r_em_time_ub', 'inner_l_em_time_ub',
    'frfr_r_boman_ub', 'frfr_l_boman_ub', 'apron_r_boman_ub', 'apron_l_boman_ub', 'inner_r_boman_ub', 'inner_l_boman_ub',
    'frfr_r_boketsu_ub', 'frfr_l_boketsu_ub', 'apron_r_boketsu_ub', 'apron_l_boketsu_ub', 'inner_r_boketsu_ub', 'inner_l_boketsu_ub',
    'frfr_r_shokusei_yobidashi_ub', 'frfr_l_shokusei_yobidashi_ub', 'apron_r_shokusei_yobidashi_ub', 'apron_l_shokusei_yobidashi_ub', 'inner_r_shokusei_yobidashi_ub', 'inner_l_shokusei_yobidashi_ub',
    'frfr_r_sei_yobidashi_ub', 'frfr_l_sei_yobidashi_ub', 'apron_r_sei_yobidashi_ub', 'apron_l_sei_yobidashi_ub', 'inner_r_sei_yobidashi_ub', 'inner_l_sei_yobidashi_ub'
]

under_body2_columns = common_columns + [
    'fsmr_daisu_ub', 'fsml_daisu_ub', 'dash_daisu_ub', 'locker_daisu_ub', 'rfloor_daisu_ub',
    'fsmr_em_time_ub', 'fsml_em_time_ub', 'dash_em_time_ub', 'locker_em_time_ub', 'rfloor_em_time_ub',
    'fsmr_boman_ub', 'fsml_boman_ub', 'dash_boman_ub', 'locker_boman_ub', 'rfloor_boman_ub',
    'fsmr_boketsu_ub', 'fsml_boketsu_ub', 'dash_boketsu_ub', 'locker_boketsu_ub', 'rfloor_boketsu_ub',
    'fsmr_shokusei_yobidashi_ub', 'fsml_shokusei_yobidashi_ub', 'dash_shokusei_yobidashi_ub', 'locker_shokusei_yobidashi_ub', 'rfloor_shokusei_yobidashi_ub',
    'fsmr_sei_yobidashi_ub', 'fsml_sei_yobidashi_ub', 'dash_sei_yobidashi_ub', 'locker_sei_yobidashi_ub', 'rfloor_sei_yobidashi_ub'
]

under_body3_columns = common_columns + [
    'noa_e_c_daisu_ub', 'al_e_c_daisu_ub', 'noa_ctr_daisu_ub', 'al_ctr_daisu_ub', 'noa_r_u_daisu_ub', 'al_r_u_daisu_ub',
    'noa_e_c_em_time_ub', 'al_e_c_em_time_ub', 'noa_ctr_em_time_ub', 'al_ctr_em_time_ub', 'noa_r_u_em_time_ub', 'al_r_u_em_time_ub',
    'noa_e_c_boman_ub', 'al_e_c_boman_ub', 'noa_ctr_boman_ub', 'al_ctr_boman_ub', 'noa_r_u_boman_ub', 'al_r_u_boman_ub',
    'noa_e_c_boketsu_ub', 'al_e_c_boketsu_ub', 'noa_ctr_boketsu_ub', 'al_ctr_boketsu_ub', 'noa_r_u_boketsu_ub', 'al_r_u_boketsu_ub',
    'noa_e_c_shokusei_yobidashi_ub', 'al_e_c_shokusei_yobidashi_ub', 'noa_ctr_shokusei_yobidashi_ub', 'al_ctr_shokusei_yobidashi_ub', 'noa_r_u_shokusei_yobidashi_ub', 'al_r_u_shokusei_yobidashi_ub',
    'noa_e_c_sei_yobidashi_ub', 'al_e_c_sei_yobidashi_ub', 'noa_ctr_sei_yobidashi_ub', 'al_ctr_sei_yobidashi_ub', 'noa_r_u_sei_yobidashi_ub', 'al_r_u_sei_yobidashi_ub'
]
under_body4_columns = common_columns+ [
    'e_c_joku_daisu_ub','ctr_joku_daisu_ub','r_u_joku_daisu_ub','motomachi_daisu_ub',
    'e_c_joku_em_time_ub','ctr_joku_em_time_ub','r_u_joku_em_time_ub','motomachi_em_time_ub',
    'e_c_joku_boman_ub','ctr_joku_boman_ub','r_u_joku_boman_ub','motomachi_boman_ub',
    'e_c_joku_boketsu_ub','ctr_joku_boketsu_ub','r_u_joku_boketsu_ub','motomachi_boketsu_ub',
    'e_c_joku_shokusei_yobidashi_ub','ctr_joku_shokusei_yobidashi_ub','r_u_joku_shokusei_yobidashi_ub','motomachi_shokusei_yobidashi_ub',
    'e_c_joku_sei_yobidashi_ub','ctr_joku_sei_yobidashi_ub','r_u_joku_sei_yobidashi_ub','motomachi_sei_yobidashi_ub'
]

sm_page_data1_columns = common_columns + [
    'smr_daisu_sm', 'sml_daisu_sm', 'roof_daisu_sm', 'header_daisu_sm', 'outer_r_daisu_sm', 'outer_l_daisu_sm',
    'smr_em_time_sm', 'sml_em_time_sm', 'roof_em_time_sm', 'header_em_time_sm', 'outer_r_em_time_sm', 'outer_l_em_time_sm',
    'smr_boman_sm', 'sml_boman_sm', 'roof_boman_sm', 'header_boman_sm', 'outer_r_boman_sm', 'outer_l_boman_sm',
    'smr_boketsu_sm', 'sml_boketsu_sm', 'roof_boketsu_sm', 'header_boketsu_sm', 'outer_r_boketsu_sm', 'outer_l_boketsu_sm',
    'smr_shokusei_yobidashi_sm', 'sml_shokusei_yobidashi_sm', 'roof_shokusei_yobidashi_sm', 'header_shokusei_yobidashi_sm', 'outer_r_shokusei_yobidashi_sm', 'outer_l_shokusei_yobidashi_sm',
    'smr_sei_yobidashi_sm', 'sml_sei_yobidashi_sm', 'roof_sei_yobidashi_sm', 'header_sei_yobidashi_sm', 'outer_r_sei_yobidashi_sm', 'outer_l_sei_yobidashi_sm'
]

sm_page_data2_columns = common_columns + [
    'inner_r_daisu_sm', 'inner_l_daisu_sm', 'cprfr_daisu_sm', 'cprfl_daisu_sm', 'transport_daisu_sm',
    'inner_r_em_time_sm', 'inner_l_em_time_sm', 'cprfr_em_time_sm', 'cprfl_em_time_sm', 'transport_em_time_sm',
    'inner_r_boman_sm', 'inner_l_boman_sm', 'cprfr_boman_sm', 'cprfl_boman_sm', 'transport_boman_sm',
    'inner_r_boketsu_sm', 'inner_l_boketsu_sm', 'cprfr_boketsu_sm', 'cprfl_boketsu_sm', 'transport_boketsu_sm',
    'inner_r_shokusei_yobidashi_sm', 'inner_l_shokusei_yobidashi_sm', 'cprfr_shokusei_yobidashi_sm', 'cprfl_shokusei_yobidashi_sm', 'transport_shokusei_yobidashi_sm',
    'inner_r_sei_yobidashi_sm', 'inner_l_sei_yobidashi_sm', 'cprfr_sei_yobidashi_sm', 'cprfl_sei_yobidashi_sm', 'transport_sei_yobidashi_sm'
]

ndai_page_data_columns = common_columns +[
    'sample_kotei_ryuju_no_ndai', 'sample_kotei_renban_ndai', 'sample_kotei_shashu_ndai', 'mbm_kotei_ryuju_no_ndai', 'mbm_kotei_renban_ndai', 'mbm_kotei_shashu_ndai', 'mbk1kotei_ub_paretto_no_ndai',
    'mbk1kotei_shashu_ndai', 'mbk1kotei_renban_ndai', 'mbk2kotei_dl_matehanshashu_ndai', 'mbk2kotei_renban_ndai', 'sm_outer_l1kotei_670_sukitto_no_ndai', 'sm_outer_l1kotei_shashu_ndai', 'sm_outer_l1kotei_renban_ndai', 
    'sm_outer_l1kotei_670_shashu_ndai', 'sm_outer_l1kotei_970_shashu_ndai', 'sm_outer_r1kotei_670_sukitto_no_ndai', 'sm_outer_r1kotei_shashu_ndai', 'sm_outer_r1kotei_renban_ndai', 'sm_outer_r1kotei_670_shashu_ndai', 
    'sm_outer_r1kotei_970_shashu_ndai', 'sm_sukiba_l_kotei_shashu_ndai', 'sm_sukiba_l_kotei_renban_ndai', 'sm_sukiba_l_kotei_sukitto_no_ndai', 'sm_sukiba_r_kotei_shashu_ndai', 'sm_sukiba_r_kotei_renban_ndai', 
    'sm_sukiba_r_kotei_sukitto_no_ndai', 's_dl_kotei_shashu_ndai', 's_dl_kotei_renban_ndai', 's_dl_kotei_kaiten_jigu_no_ndai', 's_dr_kotei_shashu_ndai', 's_dr_kotei_renban_ndai', 's_dr_kotei_kaiten_jigu_no_ndai', 
    'b_d_kotei_shashu_ndai', 'b_d_kotei_renban_ndai', 'b_d_kotei_kaiten_jigu_no_ndai', 'e_c_kotei_shashu_ndai', 'e_c_kotei_renban_ndai', 'e_c_kotei_sukitto_no_ndai', 'rr_u_kotei_shashu_ndai', 'rr_u_kotei_renban_ndai', 
    'rr_u_kotei_sukitto_no_ndai', 'ctrr_kotei_shashu_ndai', 'ctrr_kotei_renban_ndai', 'ctrr_kotei_sukitto_no_ndai', 'A_ukekoma_data_ndai', 'B_ukekoma_data_ndai', 'C_ukekoma_data_ndai', 'D_ukekoma_data_ndai',
    
]

andon_page_data_columns = common_columns + [
    'chika_andon','p_f_ow_andon',
    'p_f_ot_andon',
    'toso_andon',
    '_3_kai_andon',
    'fsm_l_andon',
    'fsm_r_andon',
    'ctr_rada_andon',
    'dash_andon',
    'ec_cv_andon',
    'cl_cv_andon',
    'ru_cv_andon',
    'r_f_andon',
    'floor_andon',
    '_5f_670kai_andon',
    'r_u_andon',
    'noa_floor_andon',
    'u_b_kari_zo_andon',
    's_m_hanso_andon',
    'm_b_kari_tsuki_andon',
    'm_b_zoda_andon',
    'sps_andon',
    '_4ten_agv_andon',
    'roof_andon',
    'inner_l_andon',
    'outer_l_andon',
    's_m_l_andon',
    's_m_r_andon',
    'outer_r_andon',
    'inner_r_andon',
    '_2line_keikaku_daisu_andon',
    '_2line_shindo_daisu_andon',
    '_2line_jisseki_daisu_andon',
    '_2line_zangyo_jikan_andon',
    '_1line_keikaku_daisu_andon',
    '_1line_shindo_daisu_andon',
    '_1line_jisseki_daisu_andon',
    '_1line_zangyo_jikan_andon',
    'chika_status_andon',
    'sheru_nai_status_andon',
    '_3kai_nishi_status_andon',
    '_3kai_higashi_status_andon',
    'fsm_l_status_andon',
    'fsm_r_status_andon',
    'r_f_status_andon',
    'e_c_status_andon',
    '_67cr_rada_status_andon',
    '_67_r_u_status_andon',
    'ec_oroshi_status_andon',
    's_m_hanso_status_andon',
    's_m_cv_status_andon',
    's_m_l_status_andon',
    's_m_r_status_andon',
    'inner_l_status_andon',
    'outer_l_status_andon',
    'outer_r_status_andon',
    'inner_r_status_andon',
    'noa_roof_status_andon',
    'u_b_kari_zo_status_andon',
    'm_b_kari_tsuki_status_andon',
    'm_b_zoda_status_andon',
    'S_B_storage_CV_status_andon',
    'dai1sheru_status_andon',
    'dai2sheru_status_andon',
    'p_f_ow_status_andon',
    'p_f_ot_status_andon',
    '_4ten_hanso_status_andon',
    'roof_agv_status_andon',
    'agv_status_andon',
    '_3f_shikake_status_andon',
    '_4f_shikake_status_andon',
    's_m3_l_status_andon',
    's_m3_r_status_andon',
    's_d_l_status_andon',
    'food_status_andon',
    'rsm_status_andon',
    'u_b3_l_status_andon',
    'u_b3_r_status_andon',
    '_5f_670kai_status_andon',
    'dash_status_andon',
    'rajisapo_status_andon',
    'rokkamenba_status_andon',
    'f_d_l_status_andon',
    'f_d_r_status_andon',
    's_d_r_status_andon',
    'b_d_status_andon',
    'sps_status_andon',
    '_2sheru_status_andon',
    '_1sheru_status_andon',
    'chu2kai_goguchi_status_andon',
    'chu2kai_retsugai_status_andon',
    'retsugaito_nyujo_status_andon',
    '_3kai_toso_status_andon',
    'Fender_status_andon',
    '_3_reikyaku_mizu_ponpu_status_andon',
    '_4_reikyaku_mizu_ponpu_status_andon',
    'Gas_atsu_status_andon',
    'Choko_kanri_status_andon',
    'floor_status_andon',
    'ec_cv_status_andon',
    'cl_cv_status_andon',
    'ru_cv_status_andon',
    'E_C_hanso_status_andon',
    'CTR_hanso_status_andon',
    'R_U_hanso_status_andon',
    '_5f_97kai_status_andon',
    '_970fsm_r_status_andon',
    '_970_ap_fsm_status_andon',
    '_970fsm_l_status_andon',
    '_970rajisapo_status_andon',
    '_970dash_status_andon',
    '_970ctr_rada_status_andon',
    '_970_ru_status_andon',
    '_970_ec_status_andon',
    'Trigger_andon'
]


