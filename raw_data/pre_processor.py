import os
import pandas as pd
import csv 
import sys


csv_file = sys.argv[1]
print('the file is called ' + csv_file)

preprocess_file = open(csv_file)
raw_data = list(csv.reader(preprocess_file))
print(raw_data[2])
# print(raw_data[2][1][-6])
raw_data = raw_data[2:] #remove headers + additional row

# num_rows = 0 
# for row in raw_data:
# 	num_rows += 1
# 	print(row[1])
# print(num_rows)



for row in raw_data:
	address = row[1]
	address_list = address.split(", ")
	print(address_list)
	# print(address[-6])
	# address = address.replace(address[-6],"','")
	# print(address)


data_url='https://www.osha.gov/oshstats/'


https://www.dataquest.io/m/351/working-with-strings-in-python/3/replacing-characters-and-substrings
# import csv

# f = open('artworks.csv')
# moma = list(csv.reader(f))
# # remove the header row
# moma = moma[1:]

# # Write your code here
# num_rows = 0 
# for row in moma:
#     num_rows += 1
# print(num_rows)