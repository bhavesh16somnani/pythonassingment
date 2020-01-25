# -*- coding: utf-8 -*-
"""
Created on Fri Jan 24 14:20:45 2020

@author: jedaix
"""

class car:
    def __init__(self,color,milage):
        self.color=color
        self.milage=milage
    def __str__(self):
        return self.color,self.milage
c=car('red',92)
print(c.__str__())