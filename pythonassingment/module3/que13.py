# -*- coding: utf-8 -*-
"""
Created on Wed Jan 22 11:16:57 2020

@author: jedaix
"""
i=0
rows=int(input("enter the no rows"))
columns=rows//2
for i in range(1,rows+1):
    print("                         *")

    print(" \n")
    i=1+i
    if i==columns:
       print("                         *")
       for j in range(1,rows+1):
           print("   *",end="  ")
     