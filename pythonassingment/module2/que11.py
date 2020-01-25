# -*- coding: utf-8 -*-
"""
Created on Mon Jan 20 15:59:32 2020

@author: jedaix
"""

pockets=input("enter no from 0 to 36")
color=0
y=int(pockets)
if y==0:
    color="green"
elif y>=1 and y<=10 :
    if y%2==0:
        color="black"
    else:
        color="red"
elif y>=11 and y<=18:
     if y%2==0:
        color="red"
     else:
        color="black"
elif y>=19 and y<=28:
    if y%2==0:
        color="black"
    else:
        color="red"
elif y>=29 and y<=36:
     if y%2==0:
        color="red"
     else:
        color="black"
else:
    print("the value is out of range")

print(color)
