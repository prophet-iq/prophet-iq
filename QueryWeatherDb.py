# -*- coding: utf-8 -*-
"""
Created on Sun Mar 26 09:02:25 2023

@author: Matt
"""

#Purpose: Query database using SQL
#Name: Matt Showalter
#Date: 3/26/2023
#   Run BuildWeatherDB.py to build weather database before running this program

import sqlite3
import pandas as pd


#file names for database and output file
dbFile = "weather.db"

#format output
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', None)
pd.set_option('display.expand_frame_repr', False)

#connect to and query weather database 
conn = sqlite3.connect(dbFile)
#Create SQL command
selectCmd = " SELECT temperature, windSpeed, textDescription FROM observations where textDescription = 'Clear'; "
                
                
#print out the query
result = pd.read_sql_query(selectCmd, conn)
print(result)
