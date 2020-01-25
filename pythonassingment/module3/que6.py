# -*- coding: utf-8 -*-
"""
Created on Tue Jan 21 12:42:05 2020

@author: jedaix
"""

i=input("Enter the total no of items")
n=int(item)
c=[]
whole=0
for i in range(0,n):
   while(True):
      print("Enter values",i)
      a=int(input())
      if a>0:
         whole=whole+a
         break
      else:
         pass
retail=whole*0.5
print("retail",retail)
        
            