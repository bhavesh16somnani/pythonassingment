# -*- coding: utf-8 -*-
"""
Created on Tue Jan 21 15:16:03 2020

@author: jedaix
"""
fv=[]
ttt=0
wt=0.5
ad=0.5
fcl=[]
trees=int(input("Enter the no of trees"))
time=int(input("Enter the total no of time a bird has"))
for i in range(trees):
    a=int(input("enter the fruit value of each tree"))
    fv.append(a)
for i in range(len(fv)):
    for j in range(len(fv[1:])):
        if ttt<=time:
          fc=fv[i]+fv[j]
          fcl.append(fc)
          ttt=ttt
print(max(fcl))