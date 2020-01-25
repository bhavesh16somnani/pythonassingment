# -*- coding: utf-8 -*-
"""
Created on Fri Jan 24 13:47:36 2020

@author: jedaix
"""
import random
class Coin:
    def __init__(self):
        self.sideup='heads'
    def toss(self):
        if random.randint(0,1)==0:
            self.sideup='heads'
        else:
            self.sideup='tails'
    def get_sideup(self):
        return self.sideup
    
coin=Coin()
print('the side of the coin is\n'+coin.get_sideup())
i=input('enter yes to toss \n')
if i=='yes' or i=='Yes' or i=='YES':
   usd=input('enter heads or tails\n')
   coin.toss()
   c=coin.get_sideup()
   if c==usd:
       print('you won\n'+coin.get_sideup())
   else:
       print('you loose\n'+coin.get_sideup())
   

