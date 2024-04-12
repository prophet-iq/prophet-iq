# -*- coding: utf-8 -*-
"""
Created on Sun Apr  9 17:03:10 2023

@author: Matt
"""

#Purpose: Create scatter plot of humidity for period 1. Can replace df1 to df2 to display second period data
#Name: Matt Showalter
#Date: 4/9/2023
import pandas as pd
import matplotlib.pyplot as plt
df1 = pd.read_csv("formatdata1.csv")
df2 = pd.read_csv("formatdata2.csv")
plt.scatter(df1.index.values,df1['Humidity']); plt.suptitle('Humidity')
plt.show()
