CREATE TABLE id_master (
    id BIGINT PRIMARY KEY GENERATED ALWAYS AS IDENTITY,
    table_name VARCHAR(255) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    delete_flag BOOLEAN DEFAULT FALSE
);


CREATE TABLE parameter_master (
    parameter_id INT PRIMARY KEY GENERATED ALWAYS AS IDENTITY,
    parameter_name VARCHAR(255) NOT NULL,
    parameter_value VARCHAR(255),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    delete_flag BOOLEAN DEFAULT FALSE
)


CREATE TABLE round_master (
    round_id INT PRIMARY KEY GENERATED ALWAYS AS IDENTITY,
    round_number SMALLINT NOT NULL,
    start_time TIME NOT NULL,
    end_time TIME NOT NULL,
    is_morning SMALLINT,
    delete_flag BOOLEAN DEFAULT FALSE,
    update_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    -- UNIQUE (round_number, is_morning),
);



CREATE TABLE sm_page_data1 (
 id INTEGER PRIMARY KEY GENERATED ALWAYS AS IDENTITY,
    round SMALLINT, 
    round_update BOOLEAN DEFAULT FALSE,
    is_morning SMALLINT ,
    year SMALLINT,
    month SMALLINT,
    day SMALLINT,
    hour  SMALLINT,
    minute  SMALLINT,
    smr_daisu INTEGER,
    sml_daisu INTEGER,
    roof_daisu INTEGER,
    header_daisu INTEGER,
    outer_r_daisu INTEGER,
    outer_l_daisu INTEGER,
    smr_em_time INTEGER,
    sml_em_time INTEGER,
    roof_em_time INTEGER,
    header_em_time INTEGER,
    outer_r_em_time INTEGER,
    outer_l_em_time INTEGER,
    smr_boman INTEGER,
    sml_boman INTEGER,
    roof_boman INTEGER,
    header_boman INTEGER,
    outer_r_boman INTEGER,
    outer_l_boman INTEGER,
    smr_boketsu INTEGER,
    sml_boketsu INTEGER,
    roof_boketsu INTEGER,
    header_boketsu INTEGER,
    outer_r_boketsu INTEGER,
    outer_l_boketsu INTEGER,
    smr_shokusei_yobidashi INTEGER,
    sml_shokusei_yobidashi INTEGER,
    roof_shokusei_yobidashi INTEGER,
    header_shokusei_yobidashi INTEGER,
    outer_r_shokusei_yobidashi INTEGER,
    outer_l_shokusei_yobidashi INTEGER,
    smr_sei_yobidashi INTEGER,
    sml_sei_yobidashi INTEGER,
    roof_sei_yobidashi INTEGER,
    header_sei_yobidashi INTEGER,
    outer_r_sei_yobidashi INTEGER,
    outer_l_sei_yobidashi INTEGER,
    update_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    delete_flag BOOLEAN DEFAULT FALSE
);



CREATE TABLE sm_page_data2 (
 id INTEGER PRIMARY KEY GENERATED ALWAYS AS IDENTITY,
    round SMALLINT, 
    round_update BOOLEAN DEFAULT FALSE,
    is_morning SMALLINT ,
      year SMALLINT,
    month SMALLINT,
    day SMALLINT,
    hour  SMALLINT,
    minute  SMALLINT,
    inner_r_daisu INTEGER,
    inner_l_daisu INTEGER,
    cprfr_daisu INTEGER,
    cprfl_daisu INTEGER,
    transport_daisu INTEGER,
    inner_r_em_time INTEGER,
    inner_l_em_time INTEGER,
    cprfr_em_time INTEGER,
    cprfl_em_time INTEGER,
    transport_em_time INTEGER,
    inner_r_boman INTEGER,
    inner_l_boman INTEGER,
    cprfr_boman INTEGER,
    cprfl_boman INTEGER,
    transport_boman INTEGER,
    inner_r_boketsu INTEGER,
    inner_l_boketsu INTEGER,
    cprfr_boketsu INTEGER,
    cprfl_boketsu INTEGER,
    transport_boketsu INTEGER,
    inner_r_shokusei_yobidashi INTEGER,
    inner_l_shokusei_yobidashi INTEGER,
    cprfr_shokusei_yobidashi INTEGER,
    cprfl_shokusei_yobidashi INTEGER,
    transport_shokusei_yobidashi INTEGER,
    inner_r_sei_yobidashi INTEGER,
    inner_l_sei_yobidashi INTEGER,
    cprfr_sei_yobidashi INTEGER,
    cprfl_sei_yobidashi INTEGER,
    transport_sei_yobidashi INTEGER,
    update_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    delete_flag BOOLEAN DEFAULT FALSE
-- FOREIGN KEY (round, is_morning) REFERENCES round_master(round_number, is_morning)
);


CREATE TABLE door_page_data1 (
id INTEGER PRIMARY KEY GENERATED ALWAYS AS IDENTITY,
    round SMALLINT, 
    round_update BOOLEAN DEFAULT FALSE,
    is_morning SMALLINT ,
      year SMALLINT,
    month SMALLINT,
    day SMALLINT,
    hour  SMALLINT,
    minute  SMALLINT,
    f_dr_daisu INTEGER,
    f_dl_daisu INTEGER,
    s_dr_daisu INTEGER,
    s_dl_daisu INTEGER,
    food_daisu INTEGER,
    b_d_daisu INTEGER,
    f_dr_em_time INTEGER,
    f_dl_em_time INTEGER,
    s_dr_em_time INTEGER,
    s_dl_em_time INTEGER,
    food_em_time INTEGER,
    b_d_em_time INTEGER,
    f_dr_boman INTEGER,
    f_dl_boman INTEGER,
    s_dr_boman INTEGER,
    s_dl_boman INTEGER,
    food_boman INTEGER,
    b_d_boman INTEGER,
    f_dr_boketsu INTEGER,
    f_dl_boketsu INTEGER,
    s_dr_boketsu INTEGER,
    s_dl_boketsu INTEGER,
    food_boketsu INTEGER,
    b_d_boketsu INTEGER,
    f_dr_shokusei_yobidashi INTEGER,
    f_dl_shokusei_yobidashi INTEGER,
    s_dr_shokusei_yobidashi INTEGER,
    s_dl_shokusei_yobidashi INTEGER,
    food_shokusei_yobidashi INTEGER,
    b_d_shokusei_yobidashi INTEGER,
    f_dr_sei_yobidashi INTEGER,
    f_dl_sei_yobidashi INTEGER,
    s_dr_sei_yobidashi INTEGER,
    s_dl_sei_yobidashi INTEGER,
    food_sei_yobidashi INTEGER,
    b_d_sei_yobidashi INTEGER,
    update_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    delete_flag BOOLEAN DEFAULT FALSE
-- FOREIGN KEY (round, is_morning) REFERENCES round_master(round_number, is_morning)
);


CREATE TABLE door_page_data2 (
id INTEGER PRIMARY KEY GENERATED ALWAYS AS IDENTITY,

    round SMALLINT, 
    round_update BOOLEAN DEFAULT FALSE,
    is_morning SMALLINT ,
      year SMALLINT,
    month SMALLINT,
    day SMALLINT,
    hour  SMALLINT,
    minute  SMALLINT,
    fender_daisu INTEGER,
    sps_daisu INTEGER,
    fender_em_time INTEGER,
    sps_em_time INTEGER,
    fender_boman INTEGER,
    sps_boman INTEGER,
    fender_boketsu INTEGER,
    sps_boketsu INTEGER,
    fender_shokusei_yobidashi INTEGER,
    sps_shokusei_yobidashi INTEGER,
    fender_sei_yobidashi INTEGER,
    sps_sei_yobidashi INTEGER,
    update_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    delete_flag BOOLEAN DEFAULT FALSE
-- FOREIGN KEY (round, is_morning) REFERENCES round_master(round_number, is_morning)         
)


CREATE TABLE under_body_page_data1 (

    round SMALLINT, 
    round_update BOOLEAN DEFAULT FALSE,
    is_morning SMALLINT ,
    year SMALLINT,
    month SMALLINT,
    day SMALLINT,
    hour  SMALLINT,
    minute  SMALLINT,
    frfr_r_daisu INTEGER,
    frfr_l_daisu INTEGER,
    apron_r_daisu INTEGER,
    apron_l_daisu INTEGER,
    inner_r_daisu INTEGER,
    inner_l_daisu INTEGER,
    frfr_r_em_time INTEGER,
    frfr_l_em_time INTEGER,
    apron_r_em_time INTEGER,
    apron_l_em_time INTEGER,
    inner_r_em_time INTEGER,
    inner_l_em_time INTEGER,
    frfr_r_boman INTEGER,
    frfr_l_boman INTEGER,
    apron_r_boman INTEGER,
    apron_l_boman INTEGER,
    inner_r_boman INTEGER,
    inner_l_boman INTEGER,
    frfr_r_boketsu INTEGER,
    frfr_l_boketsu INTEGER,
    apron_r_boketsu INTEGER,
    apron_l_boketsu INTEGER,
    inner_r_boketsu INTEGER,
    inner_l_boketsu INTEGER,
    frfr_r_shokusei_yobidashi INTEGER,
    frfr_l_shokusei_yobidashi INTEGER,
    apron_r_shokusei_yobidashi INTEGER,
    apron_l_shokusei_yobidashi INTEGER,
    inner_r_shokusei_yobidashi INTEGER,
    inner_l_shokusei_yobidashi INTEGER,
    frfr_r_sei_yobidashi INTEGER,
    frfr_l_sei_yobidashi INTEGER,
    apron_r_sei_yobidashi INTEGER,
    apron_l_sei_yobidashi INTEGER,
    inner_r_sei_yobidashi INTEGER,
    inner_l_sei_yobidashi INTEGER,
    update_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    delete_flag BOOLEAN DEFAULT FALSE,
-- FOREIGN KEY (round, is_morning) REFERENCES round_master(round_number, is_morning)
);



CREATE TABLE under_body_page_data2 (
 id INTEGER PRIMARY KEY GENERATED ALWAYS AS IDENTITY,
    round SMALLINT, 
    round_update BOOLEAN DEFAULT FALSE,
    is_morning SMALLINT ,
    year SMALLINT,
    month SMALLINT,
    day SMALLINT,
    hour  SMALLINT,
    minute  SMALLINT,
    fsmr_daisu INTEGER,
    fsml_daisu INTEGER,
    dash_daisu INTEGER,
    locker_daisu INTEGER,
    rfloor_daisu INTEGER,
    fsmr_em_time INTEGER,
    fsml_em_time INTEGER,
    dash_em_time INTEGER,
    locker_em_time INTEGER,
    rfloor_em_time INTEGER,
    fsmr_boman INTEGER,
    fsml_boman INTEGER,
    dash_boman INTEGER,
    locker_boman INTEGER,
    rfloor_boman INTEGER,
    fsmr_boketsu INTEGER,
    fsml_boketsu INTEGER,
    dash_boketsu INTEGER,
    locker_boketsu INTEGER,
    rfloor_boketsu INTEGER,
    fsmr_shokusei_yobidashi INTEGER,
    fsml_shokusei_yobidashi INTEGER,
    dash_shokusei_yobidashi INTEGER,
    locker_shokusei_yobidashi INTEGER,
    rfloor_shokusei_yobidashi INTEGER,
    fsmr_sei_yobidashi INTEGER,
    fsml_sei_yobidashi INTEGER,
    dash_sei_yobidashi INTEGER,
    locker_sei_yobidashi INTEGER,
    rfloor_sei_yobidashi INTEGER,
    update_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    delete_flag BOOLEAN DEFAULT FALSE,
-- FOREIGN KEY (round, is_morning) REFERENCES round_master(round_number, is_morning)
);


CREATE TABLE under_body_page_data3 (
 id INTEGER PRIMARY KEY GENERATED ALWAYS AS IDENTITY,
    round SMALLINT, 
    round_update BOOLEAN DEFAULT FALSE,
    is_morning SMALLINT ,
    year SMALLINT,
    month SMALLINT,
    day SMALLINT,
    hour  SMALLINT,
    minute  SMALLINT,
    noa_e_c_daisu INTEGER,
    al_e_c_daisu INTEGER,
    noa_ctr_daisu INTEGER,
    al_ctr_daisu INTEGER,
    noa_r_u_daisu INTEGER,
    al_r_u_daisu INTEGER,
    noa_e_c_em_time INTEGER,
    al_e_c_em_time INTEGER,
    noa_ctr_em_time INTEGER,
    al_ctr_em_time INTEGER,
    noa_r_u_em_time INTEGER,
    al_r_u_em_time INTEGER,
    noa_e_c_boman INTEGER,
    al_e_c_boman INTEGER,
    noa_ctr_boman INTEGER,
    al_ctr_boman INTEGER,
    noa_r_u_boman INTEGER,
    al_r_u_boman INTEGER,
    noa_e_c_boketsu INTEGER,
    al_e_c_boketsu INTEGER,
    noa_ctr_boketsu INTEGER,
    al_ctr_boketsu INTEGER,
    noa_r_u_boketsu INTEGER,
    al_r_u_boketsu INTEGER,
    noa_e_c_shokusei_yobidashi INTEGER,
    al_e_c_shokusei_yobidashi INTEGER,
    noa_ctr_shokusei_yobidashi INTEGER,
    al_ctr_shokusei_yobidashi INTEGER,
    noa_r_u_shokusei_yobidashi INTEGER,
    al_r_u_shokusei_yobidashi INTEGER,
    noa_e_c_sei_yobidashi INTEGER,
    al_e_c_sei_yobidashi INTEGER,
    noa_ctr_sei_yobidashi INTEGER,
    al_ctr_sei_yobidashi INTEGER,
    noa_r_u_sei_yobidashi INTEGER,
    al_r_u_sei_yobidashi INTEGER,
    update_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    delete_flag BOOLEAN DEFAULT FALSE
-- FOREIGN KEY (round, is_morning) REFERENCES round_master(round_number, is_morning)
);


CREATE TABLE ndai_page_data (
   id INTEGER PRIMARY KEY GENERATED ALWAYS AS IDENTITY,
    round SMALLINT,
    round_update BOOLEAN DEFAULT FALSE,
    is_morning SMALLINT DEFAULT 1,
     year SMALLINT,
    month SMALLINT,
    day SMALLINT,
    hour  SMALLINT,
    minute  SMALLINT,
    mbm_kotei_ryuju_no INTEGER,
    mbm_kotei_renban INTEGER,
    mbm_kotei_shashu INTEGER,
    mbk1kotei_ub_paretto_no INTEGER,
    mbk1kotei_shashu INTEGER,
    mbk1kotei_renban INTEGER,
    mbk1kotei_uke_koma_no INTEGER,
    mbk2kotei_dl_matehanshashu INTEGER,
    mbk2kotei_renban INTEGER,
    sm_auta_rl1kotei_670_sukitto_no INTEGER,
    sm_auta_rl1kotei_shashu INTEGER,
    sm_auta_rl1kotei_renban INTEGER,
    sm_auta_rl1kotei_670_shashu INTEGER,
    sm_auta_rl1kotei_970_shashu INTEGER,
    sm_sukiba_rl_kotei_shushu_jikan INTEGER,
    sm_sukiba_rl_kotei_shashu INTEGER,
    sm_sukiba_rl_kotei_renban INTEGER,
    sm_sukiba_rl_kotei_sukitto_no INTEGER,
    s_drl_kotei_shashu INTEGER,
    s_drl_kotei_renban INTEGER,
    s_drl_kotei_kaiten_jigu_no INTEGER,
    b_d_kotei_shashu INTEGER,
    b_d_kotei_renban INTEGER,
    b_d_kotei_kaiten_jigu_no INTEGER,
    e_c_kotei_shashu INTEGER,
    e_c_kotei_renban INTEGER,
    e_c_kotei_sukitto_no INTEGER,
    rr_u_kotei_shashu INTEGER,
    rr_u_kotei_renban INTEGER,
    rr_u_kotei_sukitto_no INTEGER,
    ctrr_kotei_shashu INTEGER,
    ctrr_kotei_renban INTEGER,
    ctrr_kotei_sukitto_no INTEGER,
    update_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    delete_flag BOOLEAN DEFAULT FALSE
);



CREATE TABLE andon_page_data (
    id INTEGER PRIMARY KEY GENERATED ALWAYS AS IDENTITY,
    round SMALLINT,
    round_update BOOLEAN DEFAULT FALSE,
    is_morning SMALLINT DEFAULT 1,
     year SMALLINT,
    month SMALLINT,
    day SMALLINT,
    hour  SMALLINT,
    minute  SMALLINT,
    chika INTEGER,
    p_f_ow INTEGER,
    p_f_ot INTEGER,
    toso INTEGER,
    _3_kai INTEGER,
    fsm_l INTEGER,
    fsm_r INTEGER,
    ctr_rada INTEGER,
    dash INTEGER,
    ec_cv INTEGER,
    cl_cv INTEGER,
    ru_cv INTEGER,
    r_f INTEGER,
    kai INTEGER,
    _5f_670kai INTEGER,
    r_u INTEGER,
    noa_kai INTEGER,
    u_b_kari_zo INTEGER,
    s_m_hanso INTEGER,
    m_b_kari_tsuki INTEGER,
    m_b_zoda INTEGER,
    sps INTEGER,
    _4ten_agv INTEGER,
    roof INTEGER,
    inner_l INTEGER,
    outer_l INTEGER,
    s_m_l INTEGER,
    s_m_r INTEGER,
    outer_r INTEGER,
    inner_r INTEGER,
    _2rain_kaikaku_daisu INTEGER,
    _2rain_shindo_daisu INTEGER,
    _2rain_jisseki_daisu INTEGER,
    _2rain_zangyo_jikan INTEGER,
    _1rain_kaikaku_daisu INTEGER,
    _1rain_shindo_daisu INTEGER,
    _1rain_jisseki_daisu INTEGER,
    _1rain_zangyo_jikan INTEGER,
    sheru_nai INTEGER,
    _3kai_nishi INTEGER,
    _3kai_azuma INTEGER,
    e_c INTEGER,
    _67cr_rada INTEGER,
    _67_r_u INTEGER,
    ec_oroshi INTEGER,
    s_m_cv INTEGER,
    noal_roof INTEGER,
    S_B_storage_CV INTEGER,
    dai1sheru_teishi_chu INTEGER,
    dai2sheru_teishi_chu INTEGER,
    _4ten_hanso INTEGER,
    roof_agv INTEGER,
    agv INTEGER,
    _3f_shikake INTEGER,
    _4f_shikake INTEGER,
    s_m3_l INTEGER,
    s_m3_r INTEGER,
    s_d_l INTEGER,
    food INTEGER,
    rsm INTEGER,
    u_b3_l INTEGER,
    u_b3_r INTEGER,
    rajisapo INTEGER,
    rokkamenba INTEGER,
    f_d_l INTEGER,
    f_d_r INTEGER,
    s_d_r INTEGER,
    b_d INTEGER,
    _2_sheru_ijou INTEGER,
    _2_sherubo_ketsu INTEGER,
    _2_sherubo_man INTEGER,
    _2_sheru_soku_toma INTEGER,
    _2_sheru_sagyo_okure INTEGER,
    _2_sheru_tei_ichi_teishi INTEGER,
      _2_sheru_nazo_teishi INTEGER,
     _1_sheru_ijou INTEGER,
      _1_sherubo_ketsu INTEGER,
      _1_sherubo_man INTEGER,
      _1_sheru_soku_toma INTEGER,
      _1_sheru_sagyo_okure INTEGER,
      _1_sheru_tei_ichi_teishi INTEGER,
      _1_sheru_nazo_teishi INTEGER,
    SPS_delay_1R_work_delay INTEGER,
    Mezzo_floor_entrance INTEGER,
    Mezzo_floor_outside_row INTEGER,
    Outside_row_input_area INTEGER,
      _3rd_floor_painting INTEGER,
    Fender INTEGER,
      _3_reikyaku_mizu_ponpu INTEGER,
      _4_reikyaku_mizu_ponpu INTEGER,
    Gas_atsu INTEGER,
    Indication_management INTEGER,
    E_C_transport INTEGER,
    CTR_transport INTEGER,
    R_U_transport INTEGER,
      _5_kai_97_kai INTEGER,
    Outside_row_removal INTEGER,
      _2_shell_lifter_immediately_stopped INTEGER,
      _970fsm_r INTEGER,
      _970_ap_fsm INTEGER,
      _970fsm_l INTEGER,
      _970radio_support INTEGER,
      _970_dash INTEGER,
      _970ctr_rada INTEGER,
      _970_ru INTEGER,
      _970_ec INTEGER,
    update_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    delete_flag BOOLEAN DEFAULT FALSE,
);

insert into id_master (table_name, created_at, delete_flag) 
values 
('door_page_data1','2025-03-17 08:36:48' ,'false' ),
('door_page_data2','2025-03-17 08:36:48' ,'false' ),
('under_body_page_data1','2025-03-17 08:36:48' ,'false' ),
('under_body_page_data2','2025-03-17 08:36:48' ,'false' ),
('under_body_page_data3','2025-03-17 08:36:48' ,'false' );


insert into round_master (round_number, start_time, end_time,is_morning,delete_flag, update_time, id_master_id,parameter_master_id)
values 
(1,'08:00:00','09:00:00',1,'false','2025-03-17 08:36:48',1,1),
(2,'09:00:00','10:00:00',1,'false','2025-03-17 08:36:48',1,1),
(3,'10:00:00','11:00:00',1,'false','2025-03-17 08:36:48',1,1),
(4,'11:00:00','12:00:00',1,'false','2025-03-17 08:36:48',1,1),
(5,'12:00:00','13:00:00',1,'false','2025-03-17 08:36:48',1,1),
(6,'13:00:00','14:00:00',1,'false','2025-03-17 08:36:48',1,1),
(7,'14:00:00','15:00:00',1,'false','2025-03-17 08:36:48',1,1),
(8,'15:00:00','16:00:00',1,'false','2025-03-17 08:36:48',1,1),


