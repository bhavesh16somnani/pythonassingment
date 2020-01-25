# -*- coding: utf-8 -*-
"""
Created on Thu Jan 23 10:24:33 2020

@author: jedaix
"""

people={1:{'name':'john','age':'27','sex':'male'},2:{'name':'marie','age':'22','sex':'female'}}
print(people)
print(people[1]['name'])
print(people[1]['age'])
print(people[1]['sex'])
people[3]={}
people[3]['name']='Luna'
people[3]['age']='24'
people[3]['sex']='female'
people[3]['married']='no'
print(people[3])

people[4]={'name':'peter','age':'29','sex':'male','married':'yes'}
print(people[4])
del people[3]['married']
del people[4]['married']
print(people[3])
print(people[4])

del people[3],people[4]
print(people)

for p_id,p_info in people.items():
    print("\nPerson ID",p_id)
    for key in p_info:
        print(key,'',p_info[key])