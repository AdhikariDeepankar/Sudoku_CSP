# -*- coding: utf-8 -*-
"""
Created on Wed Apr  8 10:29:22 2020

@author: deepa
"""
"""
def random_selection_domain():
    value = randint(1, 9)
    return value
"""
import random
from random import randint
import time
totaltime = time.time()
matrix = [[0,0,2,1,0,6,0,0,4],
          [1,0,0,0,0,9,0,0,6],
          [0,0,4,0,5,0,1,8,3],
          [0,4,0,0,0,0,0,0,0],
          [0,1,0,9,2,0,3,7,8],
          [2,3,0,5,0,8,4,0,0],
          [0,0,0,8,7,5,2,9,1],
          [8,5,0,4,9,2,6,0,0],
          [0,0,9,0,0,1,8,0,5]]

#code to input the suduko into matrix
cl=[-1,-1,-1,-1]
nE = 0


def getDomain(a,b):
    crossCheckMatrix = matrix
    list1=[1,2,3,4,5,6,7,8,9]
    finalList=[]
    for i in list1:
        crossCheckMatrix[a][b]=i
        if rowCheck(crossCheckMatrix)==1 and columnCheck(crossCheckMatrix)==1 and checkGrids(crossCheckMatrix)==1:
            finalList.append(i)
        crossCheckMatrix[a][b]=0
    random.shuffle(finalList)
    return finalList

# return 0 if any check condition is not fullfilled
def rowCheck(matrix):
    checkList=[]
    for i in range(0,9):        
        for j in range(0,9):
            if matrix[i][j] != 0:
                if matrix[i][j] in checkList:
                    return 0
                checkList.append(matrix[i][j])            
        checkList.clear()
    return 1

def columnCheck(matrix):
    checkList=[]
    for i in range(0,9):        
        for j in range(0,9):
            if matrix[j][i] != 0:
                if matrix[j][i] in checkList:
                    return 0
                checkList.append(matrix[j][i])            
        checkList.clear()
    return 1

def checkGrids(matrix):
    checkList=[]
    for i in range(0,9):
        start_Row=int((i/3))*3
        for j in range(start_Row,start_Row+3):
            start_Col=int((i%3))*3
            for k in range(start_Col,start_Col+3):
                if matrix[j][k] != 0:
                    if matrix[j][k] in checkList:
                        return 0
                    checkList.append(matrix[j][k]) 
        checkList.clear()
    return 1

def returnVariables(matrix):
    var_Coords=[]
    for i in range(0,9):        
        for j in range(0,9):
            if matrix[i][j] == 0:
                var_Coords.append((i,j)) 
    return var_Coords


def backtrack(matrix):
    global nE
    nE = nE+1
    
    if len(remaining_vars)==0:
        return 1
    mindomLen=10
    for c,d in remaining_vars:  #applying heuristics choosing the variable with smallest domain size
        if len(getDomain(c,d))<mindomLen:
            x=c
            y=d
    a=x
    b=y
    remaining_vars.remove((a,b))
    for i in getDomain(a,b):
        matrix[a][b]=i
        if rowCheck(matrix)==1 and columnCheck(matrix)==1 and checkGrids(matrix)==1:
            var_values.append((a,b,i))
            result= backtrack(matrix)
            if result == 1:
                return 1
            matrix[a][b]=0
            var_values.remove((a,b,i))
        matrix[a][b]=0
    remaining_vars.append((a,b))
    return 0
        

#input file has suduko in text format where multiple sudukos are seperated by -1 in the new line
import numpy as np
f = open("input.txt").read()
wf=open('output.txt','a')
a=0
for line in f.split():
    if(line!="-1"):
        matrix[int(a/9)][int(a%9)]= int(line)
        a=a+1
        if(a==81):
            variables_Coordinates = returnVariables(matrix)
            num_vars = len(variables_Coordinates)
            var_values=[]
            remaining_vars=variables_Coordinates
            start_time = time.time()
            sol=backtrack(matrix)
            print("----%d nodes expanded ---",nE)
            nE=0
            print("--- %s seconds ---" % (time.time() - start_time))
            print(matrix)
            np.savetxt(wf, matrix, fmt='%s')
            np.savetxt(wf, cl, fmt='%s')
    if line == "-1":
        a=0
        

wf.close()

print("Total time %s seconds ---" % (time.time() - totaltime))












































