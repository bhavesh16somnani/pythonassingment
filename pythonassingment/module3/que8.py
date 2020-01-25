# -*- coding: utf-8 -*-
"""
Created on Tue Jan 21 14:34:35 2020

@author: jedaix
"""
sum1=input("enter the value of sum1")
sum1=int(sum1)
l,m=[],[]
no=int(input("enter the no of elements in array"))
for i in range(no):
    a=int(input())
    l.append(a)
for i in range(no):
    b=int(input())
    m.append(b)
for j in range(len(l)):
    for k in range(len(m)):
        sum2=l[j]+m[k]
        if sum2==sum1:
            print(l[j],m[k])
        else:
          pass