# -*- coding: utf-8 -*-
"""
Created on Tue Jan 21 11:06:54 2020

@author: jedaix
"""

string=input("enter any url")
c=string.split("/")
s=c[-1].split(".")
print(s[0]+".pdf")