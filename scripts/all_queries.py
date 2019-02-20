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
#uploaded 2/20
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



#ogrinfo -so -al zip_codes_shape.shp
zipcodes_shapefile_create_table = '''CREATE TABLE zipcodes_spatial_data
	(
	Name varchar(254) null,
	descriptio varchar(254) null,
	timestamp varchar(32) null,
	timebegin varchar(32) null,
	toimeend varchar(32) null, 
	altitudeMo varchar(254) null,
	tessellate float(10) null,
	extrude float (10) null,
	visibility float(10) null,
	drawOrder float(10) null,
	icon varchar(254) null,
	ZCTA5CE10 varchar(254) null,
	AFFGEOID10 varchar(254) null,
	GEOID10 varchar(254) primary key, 
	ALAND10 varchar(254) null, 
	AWATER10 varchar(254) null,
	geom geometry
	);'''




# shp2pgsql -I -s 2263 SHAPEFILE.shp DATATABLE | psql -U DATABASE_USER -d DATABASE_NAME



# shp2pgsql -I -s 4326 zip_codes_shape.shp zipcodes_spatial_data2 | psql -U postgres -d osha_database

# shp2pgsql -I -s 4326 zip_codes_shape.shp zipcodes_spatial_data2 > SHAPEFILE.sql

# shp2pgsql -I -s 4326 zip_codes_shape.shp zipcodes_spatial_data > SHAPEFILE.sql



# shp2pgsql -I -s <SRID> <PATH/TO/SHAPEFILE> <DBTABLE> > SHAPEFILE.sql
'''
CREATE TABLE TABLE_name(gid integer, code smallint, name varchar(32), shape_leng numeric, shape_area numeric,  geom geometry);
'''
# Name: String (254.0)
# descriptio: String (254.0)
# timestamp: String (24.0)
# begin: String (24.0)
# end: String (24.0)
# altitudeMo: String (254.0)
# tessellate: Integer64 (10.0)
# extrude: Integer64 (10.0)
# visibility: Integer64 (10.0)
# drawOrder: Integer64 (10.0)
# icon: String (254.0)
# ZCTA5CE10: String (254.0)
# AFFGEOID10: String (254.0)
# GEOID10: String (254.0)
# ALAND10: String (254.0)
# AWATER10: String (254.0)


 # public | naics_codes_data        | table | postgres
 # public | osha_fatalities_data    | table | postgres
 # public | osha_inspection_data    | table | postgres
 
 # public | osha_severe_injury_data | table | postgres
 
 # public | sic_codes_data          | table | postgres
 # public | spatial_ref_sys         | table | postgres














































