# -*- coding: utf-8 -*-
"""
Created on Tue Jan 21 11:28:53 2020

@author: jedaix
"""

string=input("Enter name and numbers after comas")
l=string.split(",")
m=[]
f=l[1:]
for i in range(len(f)):
    m.append(int(f[i]))
s_t,s_p=0,0
s_t=m[0]+m[1]+m[2]+m[3]+m[4]
s_p=m[5]+m[6]+m[7]
per=((s_t+s_p)/590)*100
print(l[0]+"obtained"+s_t+"marks out of 500 in theory and"+s_p+"out of 90 in practical and succesfully passed the exam with"+per+"in aggregate.Many congratulations to "+l[0])