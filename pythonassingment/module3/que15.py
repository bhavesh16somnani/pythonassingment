# -*- coding: utf-8 -*-
"""
Created on Wed Jan 22 12:44:44 2020

@author: jedaix
"""

rows=int(input("enter the no of rows"))
for i in range(1,rows+1):
    print(" "*(rows-i),"*")
    print(" "*(rows+i),"*")
