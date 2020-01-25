# -*- coding: utf-8 -*-
"""
Created on Wed Jan 22 15:31:15 2020

@author: jedaix
"""
li=[]
ci,nl=[],[]
no = int(input("Enter the size of the list"))
for i in range(no):
    a=int(input(""))
    li.append(a)
li.sort()
for j in range(no):
    count=1
    c=li[j]
    for k in range(no):
         if c==li[k] and k!=j:
             count=count+1;
    ci.append(count)
print(ci)   

for i in range(len(ci)):
   a=ci.index(max(ci))
   b=li[a]
   nl.append(b)
   ci[a]=0
   
print(nl)




    