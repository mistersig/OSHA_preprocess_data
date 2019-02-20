'''
a place to hold all my queries for this project

'''
#
#inspection CSV files
#completed 2/16

inspection_data_create_table = '''CREATE TABLE osha_inspection_data
	(
	activity_nr int primary key,
	reporting_id int null,
	state_flag varchar(6),
	estab_name varchar(128),
	site_address varchar(200),
	site_city varchar(64),
	site_state char(2),
	site_zip int,
	owner_type varchar(32),
	owner_code int null,
	adv_notice varchar(2),
	safety_hlth varchar(2),
	sic_code int null,
	naics_code int null,
	insp_type char(20),
	insp_scope char(20),
	why_no_insp char(32),
	union_status char(6),
	safety_manuf varchar(10),
	safety_const varchar(10),
	safety_marit varchar(10),
	health_manuf varchar(10),
	health_const varchar(10),
	health_marit varchar(10),
	migrant varchar(10),
	mail_street varchar(200),
	mail_city varchar(64),
	mail_state char(2),
	mail_zip int,
	host_est_key varchar(20),
	nr_in_estab int Null,
	open_date date Null,
	case_mod_date date Null,
	close_conf_date date Null,
	close_case_date date Null,
	ld_dt TIMESTAMPTZ
	);'''

#severe injury CSV
# incident_id,event_date,employer,address1,address2,city,state,zipcode,latitude,longitude,naics_code,hospitalized,amputation,final_description,body_part
##injury_index,incident_id,event_date,employer,address1,address2,city,state,zipcode,latitude,longitude,naics_code,hospitalized,amputation,final_description,body_part
#completed 2/18
#uploaded 2/19
severe_injury_data_create_table = '''CREATE TABLE osha_severe_injury_data
	(
	injury_index int primary key,
	incident_id BIGINT null,
	event_date date null,
	employer varchar(128) null,
	address1 varchar(128) null,
	address2 varchar(128) null,
	city char(64) null,
	state char(32) null,
	zipcode int null,
	latitude float(32),
	longitude float(32),
	naics_code int,
	hospitalized smallint,
	amputation smallint,
	final_description varchar(3000),
	body_part varchar(64)

	);'''

#fatalities CSV
#date,company,city,state,zipcode
#complete 2/18
fatalities_data_create_table = '''CREATE TABLE osha_fatalities_data
	(
	incident_date date,
	company  varchar(100) null, 
	city varchar(50) null,
	state char(2) null,
	zipcode int null
	);'''

#sic codes CSV
#completed 2/18
sic_codes_data_create_table = '''CREATE TABLE sic_codes_data
	(
	code smallint primary key,
	description varchar(128)
	);'''



#nics codes CSV
#codes,titles
#completed2/178
#uploaded 2/19
naics_codes_create_table = '''CREATE TABLE naics_codes_data
	(
	codes int primary key,
	titles varchar(300) null
	);'''



 # public | naics_codes_data        | table | postgres
 # public | osha_fatalities_data    | table | postgres
 # public | osha_inspection_data    | table | postgres
 
 # public | osha_severe_injury_data | table | postgres
 
 # public | sic_codes_data          | table | postgres
 # public | spatial_ref_sys         | table | postgres














































