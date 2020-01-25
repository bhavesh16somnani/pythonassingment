# -*- coding: utf-8 -*-
"""
Created on Thu Jan 23 14:11:36 2020

@author: jedaix
"""

datastore={'office':{'medical':[
          {'room-number':100,'use':'reception','sqt-ft':50,'price':75}
         ,{'room-number':101,'use':'waiting','sqt-ft':250,'price':75}
         ,{'room-number':102,'use':'exmaniation','sqt-ft':125,'price':150}
         ,{'room-number':103,'use':'examination','sqt-ft':125,'price':150}
         ,{'room-number':104,'use':'office','sqt-ft':150,'price':100}]
         ,'parking':{'location':'premium','style':'covered','price':750}
          }}
#print(datastore)

def change_roomnop(datastore):
    change=int(input("Enter the room no you want to change the price"))
    price=int(input("enter the price you want to give"))
    for i in range(0,3):
        for j in range(0,5):
            if change==datastore['office']['medical'][j]['room-number']:
                datastore['office']['medical'][j]['price']=price
    print(datastore)
change_roomnop(datastore)

def change_roomno(datastore):
    change=int(input("Enter the room no you want to change no"))
    nr=int(input("enter the new room no"))
    for i in range(0,3):
        for j in range(0,5):
            if change==datastore['office']['medical'][j]['room-number']:
                datastore['office']['medical'][j]['room-number']=nr
    print(datastore)
change_roomno(datastore)

def del_room(datastore):
    change=int(input("enter the room no you want to delete the room"))
    for i in range(0,5):
        if change==datastore['office']['medical'][i]['room-number']:
            break
    print(datastore)
del_room(datastore)

def add_room(datastore):
   room_number=int(input("enter the room no you want to add"))
   use=input("enter reception or waiting or examination or office")
   sqt_ft=int(input("enter the square feet of room"))
   price=int(input("Enter the price of room"))
   
   d={'room-number':room_number,'use':use,'sqt-ft':sqt_ft,'price':price}
   datastore['office']['medical'].append(d)
   print(datastore)
add_room(datastore)
   
Input=input("Do you want to change price of the room enter yes or no")
if Input=='yes' or Input=='Yes' or Input=='YES':
    add_room()
if Input=='yes' or Input=='Yes' or Input=='YES':
    add_room()
if Input=='yes' or Input=='Yes' or Input=='YES':
    add_room()

    