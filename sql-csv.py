#import from csv

import csv
import sqlite3

#create connection object
conn = sqlite3.connect("new.db")

#get a cursor object used to execute SQL commands
cursor = conn.cursor()

try:
	#insert data
	cursor.execute("INSERT INTO populations VALUES('New York City', 'NY', 8200000)")
	cursor.execute("INSERT INTO populations VALUES('San Francisco', 'CA', 8000000)")

	#open the csv file and assign it to a variable
	conn.commit()
except sqlite3.OperationalError:
	print "Oops! Something went wrong. Try again!"

#close the database connection
conn.close()