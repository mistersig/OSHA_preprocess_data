import sys
import os
import psycopg2 as dbcooper
import pprint
import csv
from all_queries import *
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

	#execute query 
	##inspection data
	#queryCon.execute(inspection_data_create_table)
	
	##execute query 
	##spatial data 
	# queryCon.execute("CREATE EXTENSION postgis")
	# queryCon.execute(severe_injury_data_create_table)
	##execute query 
	##fatalities
	# queryCon.execute(fatalities_data_create_table)
	# ##execute query 
	# ##sic codes
	queryCon.execute(sic_codes_data_create_table)
	# ##execute query 
	# ##fnaics
	# queryCon.execute(naics_codes_create_table)		
	#queryCon.commit()
	print( "TABLE CREATED")
	print("\n")
	print("\n")

	conn.commit()
	queryCon.close()



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
	table_name = 'sic_codes_data'
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




# dbName = 'osha_database'
# cooperTables(dbName)

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


	## create DB
	# cooperCreate(dbName)

	##creates tables 
	# cooperTables(dbName,f)

	##upload csv
	cooperUpload(f)

	f.close()
