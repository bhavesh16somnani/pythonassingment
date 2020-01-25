# -*- coding: utf-8 -*-
"""
Created on Wed Jan 22 13:50:39 2020

@author: jedaix
"""
#str="b9nh9na9nv9ne9ns9nh9n"
#def create_letter(str):
 #   mat=[[0]*4]*6
 #   for i in range(0,len(str),2):
  #      if str[i]=="b":
   #         print("*"*int(str[i+1]),end="")
    #return(mat)
     #   if str[i]=="h" 
#print(create_letter(str))
l=[[0]*3]*3
def b():
    for i in range(0,3):
        for j in range(0,3):
            if (i==0 and j==0) or (i==1 and j==0) or (i==2 and j==0) or (i==0 and j==1) or (i==1 and j==2) or (i==1 and j==0) or (i==1 and j==1) or (i==1 and j==2) or (i==2 and j==0) or (i==2 and j==1) and (i==2 and j==2):
              l[i][j]="*"
            else:
              l[i][j]="0"
    print(l[0])
    print(l[1])
    print(l[2])
print(b())
def h():
    for i in range(0,3):
        for j in range(0,3):
            if (i==0 and j==0) or (i==1 and j==0) or (i==2 and j==0)   or (i==1 and j==1)  or (i==2 and j==0) or (i==2 and j==1) and (i==2 and j==2):
              l[i][j]="* "
    print(l[0])
    print(l[1])
    print(l[2])
print(h())