# -*- coding: utf-8 -*-
"""
Created on Tue Jan 21 12:00:03 2020

@author: jedaix
"""

string=input("enter the sumject and there no")
s,l=string.split(" "),[]
for i in range(len(s)):
    if s[i]!='=':
        l.append(s[i])
j,total=0,0
for i in range(len(l)):
    if i%2!=0 and i!=0:
        total=total+int(l[i])
        j=j+1
average=total/j
print(total)
print(average)

#or
string=input("Enter sub and there no")

sum1,sub=0,0
k=string.split(" ")
while i<= len(k):
    try:
        sum1=sum1+int(k[i])
        sub=sub+1
    except:
        i=i+1
average=sum1/sub
print(sum1)
print(average)
