#!/usr/bin/env python

# version 0.9.5 - 9/4/18
# https://github.com/the-amaya/sysTAMI

import os
import MySQLdb
import sys

location = (sys.argv[1])
time = (sys.argv[2])
temp = (sys.argv[3])
hum = (sys.argv[4])

con = MySQLdb.connect('','','',''); #host, user, password, database
cursor = con.cursor()

cursor.execute("INSERT INTO database(location,time,temp,humidity) VALUES(%s,%s,%s,%s)",(location,time,temp,hum)) #edit 'database' to match your database name
con.commit()
