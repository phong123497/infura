

round_master_columns = ['round_number','start_time','end_time','is_morning','delete_flag', 'update_time']

# Common columns shared by all tables
common_columns = [
    'round_number', 'round_update', 'is_morning', 'year', 'month', 'day', 'hour', 'minute',
    'update_time', 'delete_flag', "収集日時", "hour_minute"
]

# Specific columns for each table
door1_columns = common_columns + [
    'f_dr_daisu', 'f_dl_daisu', 's_dr_daisu', 's_dl_daisu', 'food_daisu', 'b_d_daisu',
    'f_dr_em_time', 'f_dl_em_time', 's_dr_em_time', 's_dl_em_time', 'food_em_time', 'b_d_em_time',
    'f_dr_boman', 'f_dl_boman', 's_dr_boman', 's_dl_boman', 'food_boman', 'b_d_boman',
    'f_dr_boketsu', 'f_dl_boketsu', 's_dr_boketsu', 's_dl_boketsu', 'food_boketsu', 'b_d_boketsu',
    'f_dr_shokusei_yobidashi', 'f_dl_shokusei_yobidashi', 's_dr_shokusei_yobidashi', 's_dl_shokusei_yobidashi', 'food_shokusei_yobidashi', 'b_d_shokusei_yobidashi',
    'f_dr_sei_yobidashi', 'f_dl_sei_yobidashi', 's_dr_sei_yobidashi', 's_dl_sei_yobidashi', 'food_sei_yobidashi', 'b_d_sei_yobidashi'
]

door2_columns = common_columns + [
    'fender_daisu', 'sps_daisu',
    'fender_em_time', 'sps_em_time',
    'fender_boman', 'sps_boman',
    'fender_boketsu', 'sps_boketsu',
    'fender_shokusei_yobidashi', 'sps_shokusei_yobidashi', 
    'fender_sei_yobidashi', 'sps_sei_yobidashi'
]

under_body1_columns = common_columns + [
    'frfr_r_daisu', 'frfr_l_daisu', 'apron_r_daisu', 'apron_l_daisu', 'inner_r_daisu', 'inner_l_daisu',
    'frfr_r_em_time', 'frfr_l_em_time', 'apron_r_em_time', 'apron_l_em_time', 'inner_r_em_time', 'inner_l_em_time',
    'frfr_r_boman', 'frfr_l_boman', 'apron_r_boman', 'apron_l_boman', 'inner_r_boman', 'inner_l_boman',
    'frfr_r_boketsu', 'frfr_l_boketsu', 'apron_r_boketsu', 'apron_l_boketsu', 'inner_r_boketsu', 'inner_l_boketsu',
    'frfr_r_shokusei_yobidashi', 'frfr_l_shokusei_yobidashi', 'apron_r_shokusei_yobidashi', 'apron_l_shokusei_yobidashi', 'inner_r_shokusei_yobidashi', 'inner_l_shokusei_yobidashi',
    'frfr_r_sei_yobidashi', 'frfr_l_sei_yobidashi', 'apron_r_sei_yobidashi', 'apron_l_sei_yobidashi', 'inner_r_sei_yobidashi', 'inner_l_sei_yobidashi'
]

under_body2_columns = common_columns + [
    'fsmr_daisu', 'fsml_daisu', 'dash_daisu', 'locker_daisu', 'rfloor_daisu',
    'fsmr_em_time', 'fsml_em_time', 'dash_em_time', 'locker_em_time', 'rfloor_em_time',
    'fsmr_boman', 'fsml_boman', 'dash_boman', 'locker_boman', 'rfloor_boman',
    'fsmr_boketsu', 'fsml_boketsu', 'dash_boketsu', 'locker_boketsu', 'rfloor_boketsu',
    'fsmr_shokusei_yobidashi', 'fsml_shokusei_yobidashi', 'dash_shokusei_yobidashi', 'locker_shokusei_yobidashi', 'rfloor_shokusei_yobidashi',
    'fsmr_sei_yobidashi', 'fsml_sei_yobidashi', 'dash_sei_yobidashi', 'locker_sei_yobidashi', 'rfloor_sei_yobidashi'
]

under_body3_columns = common_columns + [
    'noa_e_c_daisu', 'al_e_c_daisu', 'noa_ctr_daisu', 'al_ctr_daisu', 'noa_r_u_daisu', 'al_r_u_daisu',
    'noa_e_c_em_time', 'al_e_c_em_time', 'noa_ctr_em_time', 'al_ctr_em_time', 'noa_r_u_em_time', 'al_r_u_em_time',
    'noa_e_c_boman', 'al_e_c_boman', 'noa_ctr_boman', 'al_ctr_boman', 'noa_r_u_boman', 'al_r_u_boman',
    'noa_e_c_boketsu', 'al_e_c_boketsu', 'noa_ctr_boketsu', 'al_ctr_boketsu', 'noa_r_u_boketsu', 'al_r_u_boketsu',
    'noa_e_c_shokusei_yobidashi', 'al_e_c_shokusei_yobidashi', 'noa_ctr_shokusei_yobidashi', 'al_ctr_shokusei_yobidashi', 'noa_r_u_shokusei_yobidashi', 'al_r_u_shokusei_yobidashi',
    'noa_e_c_sei_yobidashi', 'al_e_c_sei_yobidashi', 'noa_ctr_sei_yobidashi', 'al_ctr_sei_yobidashi', 'noa_r_u_sei_yobidashi', 'al_r_u_sei_yobidashi'
]

sm_page_data1_columns = common_columns + [
    'smr_daisu', 'sml_daisu', 'roof_daisu', 'header_daisu', 'outer_r_daisu', 'outer_l_daisu',
    'smr_em_time', 'sml_em_time', 'roof_em_time', 'header_em_time', 'outer_r_em_time', 'outer_l_em_time',
    'smr_boman', 'sml_boman', 'roof_boman', 'header_boman', 'outer_r_boman', 'outer_l_boman',
    'smr_boketsu', 'sml_boketsu', 'roof_boketsu', 'header_boketsu', 'outer_r_boketsu', 'outer_l_boketsu',
    'smr_shokusei_yobidashi', 'sml_shokusei_yobidashi', 'roof_shokusei_yobidashi', 'header_shokusei_yobidashi', 'outer_r_shokusei_yobidashi', 'outer_l_shokusei_yobidashi',
    'smr_sei_yobidashi', 'sml_sei_yobidashi', 'roof_sei_yobidashi', 'header_sei_yobidashi', 'outer_r_sei_yobidashi', 'outer_l_sei_yobidashi'
]

sm_page_data2_columns = common_columns + [
    'inner_r_daisu', 'inner_l_daisu', 'cprfr_daisu', 'cprfl_daisu', 'transport_daisu',
    'inner_r_em_time', 'inner_l_em_time', 'cprfr_em_time', 'cprfl_em_time', 'transport_em_time',
    'inner_r_boman', 'inner_l_boman', 'cprfr_boman', 'cprfl_boman', 'transport_boman',
    'inner_r_boketsu', 'inner_l_boketsu', 'cprfr_boketsu', 'cprfl_boketsu', 'transport_boketsu',
    'inner_r_shokusei_yobidashi', 'inner_l_shokusei_yobidashi', 'cprfr_shokusei_yobidashi', 'cprfl_shokusei_yobidashi', 'transport_shokusei_yobidashi',
    'inner_r_sei_yobidashi', 'inner_l_sei_yobidashi', 'cprfr_sei_yobidashi', 'cprfl_sei_yobidashi', 'transport_sei_yobidashi'
]

ndai_page_data_columns = common_columns + [
    'mbm_kotei_ryuju_no', 'mbm_kotei_renban', 'mbm_kotei_shashu', 'mbk1kotei_ub_paretto_no', 'mbk1kotei_shashu', 'mbk1kotei_renban', 'mbk1kotei_uke_koma_no',
    'mbk2kotei_dl_matehanshashu', 'mbk2kotei_renban', 'sm_auta_rl1kotei_670_sukitto_no', 'sm_auta_rl1kotei_shashu', 'sm_auta_rl1kotei_renban', 'sm_auta_rl1kotei_670_shashu',
    'sm_auta_rl1kotei_970_shashu', 'sm_sukiba_rl_kotei_shushu_jikan', 'sm_sukiba_rl_kotei_shashu', 'sm_sukiba_rl_kotei_renban', 'sm_sukiba_rl_kotei_sukitto_no',
    's_drl_kotei_shashu', 's_drl_kotei_renban', 's_drl_kotei_kaiten_jigu_no', 'b_d_kotei_shashu', 'b_d_kotei_renban', 'b_d_kotei_kaiten_jigu_no',
    'e_c_kotei_shashu', 'e_c_kotei_renban', 'e_c_kotei_sukitto_no', 'rr_u_kotei_shashu', 'rr_u_kotei_renban', 'rr_u_kotei_sukitto_no',
    'ctrr_kotei_shashu', 'ctrr_kotei_renban', 'ctrr_kotei_sukitto_no'
]

andon_page_data_columns = common_columns + [
    'chika', 'p_f_ow', 'p_f_ot', 'toso', '_3_kai', 'fsm_l', 'fsm_r', 'ctr_rada', 'dash', 'ec_cv', 'cl_cv', 'ru_cv', 'r_f', 'kai', '_5f_670kai', 'r_u', 'noa_kai',
    'u_b_kari_zo', 's_m_hanso', 'm_b_kari_tsuki', 'm_b_zoda', 'sps', '_4ten_agv', 'roof', 'inner_l', 'outer_l', 's_m_l', 's_m_r', 'outer_r', 'inner_r',
    '_2rain_kaikaku_daisu', '_2rain_shindo_daisu', '_2rain_jisseki_daisu', '_2rain_zangyo_jikan', '_1rain_kaikaku_daisu', '_1rain_shindo_daisu', '_1rain_jisseki_daisu',
    '_1rain_zangyo_jikan', 'sheru_nai', '_3kai_nishi', '_3kai_azuma', 'e_c', '_67cr_rada', '_67_r_u', 'ec_oroshi', 's_m_cv', 'noal_roof', 'S_B_storage_CV',
    'dai1sheru_teishi_chu', 'dai2sheru_teishi_chu', '_4ten_hanso', 'roof_agv', 'agv', '_3f_shikake', '_4f_shikake', 's_m3_l', 's_m3_r', 's_d_l', 'food', 'rsm',
    'u_b3_l', 'u_b3_r', 'rajisapo', 'rokkamenba', 'f_d_l', 'f_d_r', 's_d_r', 'b_d', '_2_sheru_ijou', '_2_sherubo_ketsu', '_2_sherubo_man', '_2_sheru_soku_toma',
    '_2_sheru_sagyo_okure', '_2_sheru_tei_ichi_teishi', '_2_sheru_nazo_teishi', '_1_sheru_ijou', '_1_sherubo_ketsu', '_1_sherubo_man', '_1_sheru_soku_toma',
    '_1_sheru_sagyo_okure', '_1_sheru_tei_ichi_teishi', '_1_sheru_nazo_teishi', 'SPS_delay_1R_work_delay', 'Mezzo_floor_entrance', 'Mezzo_floor_outside_row',
    'Outside_row_input_area', '_3rd_floor_painting', 'Fender', '_3_reikyaku_mizu_ponpu', '_4_reikyaku_mizu_ponpu', 'Gas_atsu', 'Indication_management',
    'E_C_transport', 'CTR_transport', 'R_U_transport', '_5_kai_97_kai', 'Outside_row_removal', '_2_shell_lifter_immediately_stopped', '_970fsm_r', '_970_ap_fsm',
    '_970fsm_l', '_970radio_support', '_970_dash', '_970ctr_rada', '_970_ru', '_970_ec'
]



