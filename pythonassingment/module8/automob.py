# -*- coding: utf-8 -*-
"""
Created on Sat Jan 25 10:30:59 2020

@author: jedaix
"""

class automobile:
    def __init__(self,make,model,mileage,price):
        pass
    def set_make(self,make):
        self.make=make
    def set_model(self,model):
        self.model=model
    def set_mileage(self,mileage):
        self.mileage=mileage
    def set_price(self,price):
        self.price=price
    def get_make(self):
        return self.make
    def get_model(self):
        return self.model
    def get_mileage(self):
        return self.mileage
    def get_price(self):
        return self.price

"""a=automobile('make','model','mileage','color')
a.set_make('india')
print(a.get_make())"""