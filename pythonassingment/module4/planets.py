# -*- coding: utf-8 -*-
"""
Created on Thu Jan 23 10:56:47 2020

@author: jedaix
"""

matrix=[]
for i in range(5):
    matrix.append([])
    for j in range(5):
        matrix[i].append(j)
print(matrix)
matrix1=[[j for j in range(5)] for i in range(5)]
print(matrix1)

#flatter list
matrix=[[1,2,3],[4,5],[6,7,8,9]]
flatten_matrix=[]
for sublist in matrix:
    for var in sublist:
        flatten_matrix.append(var)
print(flatten_matrix)
flatten_matrix1=[var for sublist in matrix for var in sublist]
print(flatten_matrix1)


planets=[['Mercury','Venus','Earth'],['Mars','Jupiter','Saturn'],['Uranus','Neptune','Pluto']]
flatten_planets=[planet for sublist in planets for planet in sublist if len(planet)<6]
print(flatten_planets)
