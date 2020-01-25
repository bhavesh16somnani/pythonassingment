# -*- coding: utf-8 -*-
"""
Created on Tue Jan 21 13:59:11 2020

@author: jedaix
"""
sum1=input("enter the value of sum1")
sum1=int(sum1)
l=[]
no=int(input("enter the no of elements in array"))
for i in range(no):
    a=int(input())
    l.append(a)
    
for j in range(len(l)):
    for k in range(len(l[1:])):
        sum2=l[j]+l[k]
        if sum2==sum1:
            print(l[j],l[k])
        else:
            print("there is no matching sum sequence")
        