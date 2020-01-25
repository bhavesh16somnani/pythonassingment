# -*- coding: utf-8 -*-
"""
Created on Sat Jan 25 11:27:42 2020

@author: jedaix
"""
import random
from itertools import product
class Card:
    suit={'hearts','spades','dimond','clubs'}
    ranks={'two','three','four','five','six','seven','eight','nine','ten','jack','queen','king','ace'}
    values={'two':2,'three':3,'four':4,'five':5,'six':6,'seven':7,'eight':8,'nine':9,'ten':10,'jack':11,'queen':12,'king':13,'ace':1}        
    def __init__(self,suit,ranks,value,deck):
        self.card=deck.next_card()
        if self.card==0:
            raise Exception('all card are taken')
        self.suit=suit.card[0]
        self.ranks=suit.card[1]
        self.value=self.values[self.ranks]
    def __str__(self):
        return  {self.rank},{self.suit},{self.value}
    def getval(self):
        return self.value

class Deck(Card):
   
    def __init__(self):
        self.deck1=list(product(Deck.suit,Deck.ranks))
        random.shuffle(self.deck1)
    def next_card(self):
        if len(self.deck1)==0:
            return 0
        else:
            return self.deck1.pop()
    def shuffle(self):
        random.shuffle(self.deck1)
    def return_card(self):
        return (self.deck1)

d=Deck()
d.shuffle()
print(d.next_card())
