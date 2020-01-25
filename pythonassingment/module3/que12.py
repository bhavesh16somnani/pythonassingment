# -*- coding: utf-8 -*-
"""
Created on Wed Jan 22 10:23:46 2020

@author: jedaix
"""
rows=int(input("Enter the no of rows"))


for i in range(rows+1,1,-1):
    for j in range(0,i-1):
       print("*",end=" ")
    print("\n")
for i in range(1,rows+1):
    for j in range(1,i+1):
        print("*",end=" ")
    print("\n")