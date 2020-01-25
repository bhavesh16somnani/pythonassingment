# -*- coding: utf-8 -*-
"""
Created on Mon Jan 20 12:57:02 2020

@author: jedaix
"""
#a
l=input("enter 5 digit no")
list(l)


sum=0
for i in range(len(l)):
    sum=sum+int(l[i])
    
    
print(sum)

#b
y=input("enter 5 digit no")
s=""
x=list(y)
for i in range(len(x)):
    x[i]=int(x[i])+1
    s=s+str(x[i])
    
    
print(s)

#c
