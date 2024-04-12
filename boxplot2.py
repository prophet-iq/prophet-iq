# -*- coding: utf-8 -*-
"""
Created on Sun Apr  9 16:47:44 2023

@author: Matt
"""

#Purpose: Create box plot for week 2 data
#Name: Matt Showalter
#Date: 4/9/2023
import pandas as pd
import matplotlib.pyplot as plt
df2 = pd.read_csv("formatdata2.csv")
df2.boxplot(); plt.suptitle('Week 2 box plot')
plt.show()
