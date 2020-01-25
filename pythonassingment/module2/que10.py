# -*- coding: utf-8 -*-
"""
Created on Mon Jan 20 15:13:17 2020

@author: jedaix
"""

packages=input("Enter the no of packages")
y=int(packages)
price=99
discount=0
discounted_money=0
if y >10: 
    discount=10
elif y>=20:
    discount=20  
elif y>=50:
    discount=30  
elif y>=100:
    discount=40

discounted_money=(discount/100)*price*y
print(discounted_money)    
    
discounted_price=(price*y)-discounted_money    
print(discounted_price)