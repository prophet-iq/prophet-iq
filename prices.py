# -*- coding: utf-8 -*-
"""
Created on Sun May  7 10:36:23 2023

@author: Matt
"""

count = 0
sum = 0
full_name = input("What is your full name?: ")
min_price = float(input("What is your minimum price?: "))
price_list = [57.0, 59.0, 61.0, 61.5, 63.5, 65.5, 67.0, 69.0, 71.0, 73.0, 73.5]

for price in price_list:
    
    sum += price
    if price > min_price:
        count += 1
        
print("Hello", full_name, "the minimum price is", min_price)
print("There are", count, "prices greater than the minimum price.")
print("The total price is", sum)
