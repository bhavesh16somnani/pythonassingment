# -*- coding: utf-8 -*-
"""
Created on Wed Jan 22 16:46:09 2020

@author: jedaix
"""
inp=input("enter the sentence")
a=inp.split(" ")
b=set(a)
c=list(b)
c.sort()
print(c)