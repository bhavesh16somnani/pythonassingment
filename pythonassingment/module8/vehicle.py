# -*- coding: utf-8 -*-
"""
Created on Sat Jan 25 10:47:45 2020

@author: jedaix
"""

from automob import automobile as a
class Car(a):
    def __init__(self,make,model,mileage,price,door):
       a.__init__(self,make,model,mileage,price)
    def set_door(self,door):
        self.door=door
    def get_door(self):
        return self.door

c=Car('make','model','mileage','price','door')
c.set_door('4')
print(c.get_door())
c.set_model('1')
print(c.get_model())
    
class Truck(a):
    def __init__(self,make,model,mileage,price,drive_type):
       a.__init__(self,make,model,mileage,price)
    def set_drive_type(self,drive_type):
        self.drive_type=drive_type
    def get_drive_type(self):
        return self.drive_type
t=Truck('make','model','mileage','price','drive_type')


class SUV(a):
    def __init__(self,make,model,mileage,price,pass_cap):
       a.__init__(self,make,model,mileage,price)       
    def set_pass_cap(self,pass_cap):
        self.pass_cap=pass_cap
    def get_pass_cap(self):
        return self.pass_cap
s=SUV('make','model','mileage','price','pass_cap')