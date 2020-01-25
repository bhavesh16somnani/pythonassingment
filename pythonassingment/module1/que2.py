# -*- coding: utf-8 -*-
"""
Created on Mon Jan 20 11:38:47 2020

@author: jedaix
"""

a,b,x,y = 4,2,5,4
result = 5*b*b*x-3*a*y*y-8*b*b*x+10*a*y

a,y,c= 2,3,7
calc = 4*a*y/c-a*y/c

a,b,c,y=4.4,0.0,4.2,3.0
try:
    ans = c+a*y*y/b
except:
    print("cant be divided by zero")