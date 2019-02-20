import sys
import os
import psycopg2 as dbcooper
import pprint
import csv
#import pandas as pd
#from config import config



def cooperCreate(dbName):
	''' Initial function to create and load data  '''
	#connection string to String
	connString = "host='localhost' user='postgres' password='' "
	# print the connection string we will use to connect
	print("Connecting to database %s" % (connString))
	#get a connection, exception will be raised here if no connection made
	conn = dbcooper.connect(connString)
	print( 'connected to db \ncreating ' + dbName)

	#needed to create a db psycopg2.extensions.ISOLATION_LEVEL_AUTOCOMMIT
	conn.set_isolation_level(dbcooper.extensions.ISOLATION_LEVEL_AUTOCOMMIT)
	#will return object than can be used to query | cursor()
	queryCon = conn.cursor()

	#execute to CREATE TABLE 
	queryCon.execute("CREATE DATABASE " + dbName)

	# retrieve records from db 
	#records = queryCon.fetchall()
	#close out
	queryCon.close()
	conn.close()
	print( "DB %s has been created " %(dbName))
	print( "\n")
	

	#pprint.pprint(records)


def cooperTables(dbName, fName):
	''' Function to create table and load data  '''
	connString = "host='localhost' dbname='%s' user='postgres' password='' " %(dbName)
	# print the connection string we will use to connect
	print("Connecting to database\n	->%s" % (connString))

	#get a connection, exception will be raised here if no connection made
	conn = dbcooper.connect(connString)

	#will return object than can be used to query | cursor()
	queryCon = conn.cursor()

	#create spatial references for point data 
	
	#queryCon.execute("CREATE EXTENSION postgis")
	
	#ID,Case Number,Date,Time,Block,Primary Type,Description,Location Description,Arrest,Domestic,District,Ward,Community Area,FBI Code,Latitude,Longitude
	# queryExpress = '''CREATE TABLE osha_inspection_data
	# (
	# activity_nr int primary key,
	# reporting_id int null,
	# state_flag varchar(6),
	# estab_name varchar(128),
	# site_address varchar(64),
	# site_city varchar(64),
	# site_state char(2),
	# site_zip int,
	# owner_type varchar(32),
	# owner_code smallint null,
	# adv_notice varchar(2),
	# safety_hlth varchar(2),
	# sic_code int null,
	# naics_code int null,
	# insp_type char(20),
	# insp_scope char(20),
	# why_no_insp char(32),
	# union_status char(6),
	# safety_manuf varchar(10),
	# safety_const varchar(10),
	# safety_marit varchar(10),
	# health_manuf varchar(10),
	# health_const varchar(10),
	# health_marit varchar(10),
	# migrant varchar(10),
	# mail_street varchar(64),
	# mail_city varchar(64),
	# mail_state char(2),
	# mail_zip int,
	# host_est_key varchar(20),
	# nr_in_estab int Null,
	# open_date date Null,
	# case_mod_date varchar(32) Null,
	# close_conf_date varchar(32) Null,
	# close_case_date varchar(32) Null,
	# ld_dt TIMESTAMPTZ
	# );'''
	queryExpress = '''CREATE TABLE osha_inspection_data
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

	#execute query 
	queryCon.execute(queryExpress)
	#queryCon.commit()
	print( "TABLE CREATED")
	print("\n")
	print("\n")

	conn.commit()
	queryCon.close()


# def cooperUpload(fName):
# 	count = 0
# 	connString = "host='localhost' dbname='%s' user='postgres' password='' " %(dbName)
# 	# print the connection string we will use to connect
# 	print("Connecting to database\n	->%s" % (connString))
# 	#get a connection, exception will be raised here if no connection made
# 	conn = dbcooper.connect(connString)
# 	#will return object than can be used to query | cursor()
# 	queryCon = conn.cursor()
# 	print("\n")
# 	print("\n")
# 	#print fName
# 	table_name = 'osha_inspection_data'
# 	file_object = fName
# 	SQL_STATEMENT = """
#     COPY %s FROM STDIN WITH
#     DELIMITER AS ','
#     QUOTE '"'
#     HEADER
#     CSV    
#     """
#     while queryCon.copy_expert(sql=SQL_STATEMENT % table_name, file=file_object) == True:
#     	try:
#     		queryCon.copy_expert(sql=SQL_STATEMENT % table_name, file=file_object)
# 			conn.commit()
# 			queryCon.close()
# 			print("UPLOAD SUCCESS!!!!")
# 			print("\n")
# 			print("\n")
# 		except Exception:
# 			count +=1
# 			print(count)
# 			pass


def cooperUpload(fName):
	connString = "host='localhost' dbname='%s' user='postgres' password='' " %(dbName)
	# print the connection string we will use to connect
	print("Connecting to database\n	->%s" % (connString))
	#get a connection, exception will be raised here if no connection made
	conn = dbcooper.connect(connString)
	#will return object than can be used to query | cursor()
	queryCon = conn.cursor()
	print("\n")
	print("\n")
	#print fName
	table_name = 'osha_inspection_data'
	file_object = fName
	SQL_STATEMENT = """
    COPY %s FROM STDIN WITH
    DELIMITER AS ','
    QUOTE '"'
    HEADER
    CSV    
    """
	queryCon.copy_expert(sql=SQL_STATEMENT % table_name, file=file_object)

	conn.commit()
	queryCon.close()
	print("UPLOAD SUCCESS!!!!")
	print("\n")
	print("\n")







##################
#Global Variable 

# pathFile = '/Users/Sigfrido/Documents/GitHub/ChiCrimeDB14/dbUpload2Graph/data/quarter/'

# fileName = pathFile + 'crimes201401_201703.csv'


csv_file = sys.argv[1]

# f = open(csv_file)

with open(csv_file, 'rb') as f:
    # fieldnames = ['first_name', 'last_name']
    # writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    # writer.writeheader()
    # writer.writerow({'first_name': 'Baked', 'last_name': 'Beans'})
    # writer.writerow({'first_name': 'Lovely', 'last_name': 'Spam'})
    # writer.writerow({'first_name': 'Wonderful', 'last_name': 'Spam'})




	#DB NAME
	dbName = 'osha_database'


	# # create DB
	# cooperCreate(dbName)

	# # creates tables 
	# cooperTables(dbName,f)

	#upload csv
	cooperUpload(f)

#	f.close()
