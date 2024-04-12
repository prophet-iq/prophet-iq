# -*- coding: utf-8 -*-
"""
Created on Thu May 11 18:58:44 2023

@author: Matt
"""

class Washer:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        
    def wash_start(self):
        print("The "+self.make, "started washing.")
        
    def wash_stop(self):
        print("The " +self.make, "stopped wash cycle.")
        
washer_1 = Washer("Samnsung", "Superwash", 2019)
washer_2 = Washer("Sony", "Ultraspin", 2022)

washer_1.wash_start()
washer_1.wash_stop()

        
    