# -*- coding: utf-8 -*-
"""
Created on Tue Jan 21 10:32:07 2020

@author: jedaix
"""

string=input("enter any string with lower and upper string charchters")
string1=""
string2=""
for i in range(len(string)):
    if string[i].islower():
        string1=string1+string[i]
    elif string[i].isupper():
        string2=string2+string[i]
print(string1+string2)