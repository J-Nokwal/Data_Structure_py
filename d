import copy 
import numpy as np
import random
import time
def Position(val,arr):
    for i in range(len(arr)):
            for j in range(len(arr)):
                        if(arr[i][j] == val):
                                        return (i,j)
def up(i, j, strt):
    if i - 1 < 0:
            return strt
                new = copy.deepcopy(strt)
                    temp = new[i][j]
                        new[i][j] = new[i - 1][j]
                            new[i - 1][j] = temp
                                return new

def down(i, j, strt):
    if i + 1 > 2:
            return strt
                new = copy.deepcopy(strt)
                    temp = new[i][j]
                        new[i][j] = new[i + 1][j]
                            new[i + 1][j] = temp
                                return new
def left(i, j, strt):
    if j - 1 < 0:
            return strt
                new = copy.deepcopy(strt)
                    temp = new[i][j]
                        new[i][j] = new[i][j - 1]
                            new[i][j - 1] = temp
                                return new
def right(i, j, strt):
    if j + 1 > 2:
            return strt
                new = copy.deepcopy(strt)
                    temp = new[i][j]
                        new[i][j] = new[i][j + 1]
                            new[i][j + 1] = temp
                                return new
def solve(crnt, final):
    count = 0
        for i in range(3):
                for j in range(3):
                            if(crnt[i][j] != final[i][j]):
                                            count += 1
                                                return count
def ran():
    arr=[i for i in range(0,9)]
        random.shuffle(arr)
            li=[]
                for i in range(3):
                        p=[]
                                p.append(arr[(3*i)+0])
                                        p.append(arr[(3*i)+1])
                                                p.append(arr[(3*i)+2])
                                                        li.append(p)
                                                            return li
def BFS(start, final):
    count = 0
        visited = []
            parent_value = solve(start, final)
                distance=[]
                    new = start
                        while(True):
                                count =count+ 1
                                        temp = new
                                                visited.append(temp)
                                                        distance.append(new)
                                                                row,col = Position(0,temp) 
                                                                        for state in range(1,5):
                                                                            if(state == 1): 
                                                                                next = up(row,col,temp)
                                                                            if(state == 2): 
                                                                                next = down(row,col,temp)
                                                                            if(state == 3): 
                                                                                next = left(row,col,temp)
                                                                            if(state == 4):
                                                                                next = right(row,col,temp)
                                                                            if(next == final): 
                                                                                distance.append(final)
                                                                                                print("Total Iteration: ", count)
                                                                                                                return True,count,distance
                                                                            if(next != temp and next not in visited): 
                                                                                            hvalue = solve(next, final) 
                                                                                                            if(parent_value >= hvalue):
                                                                                                                                parent_value = hvalue
                                                                                                                                                    new = next
                                                                                                                                                            if(new != temp):
                                                                                                                                                                            temp = new
                                                                                                                                                                                    else:
                                                                                                                                                                                                break
    return False,-1,-1
starttime = time.time()
start = [
        [2, 8, 3], 
        [1, 0, 4], 
        [7, 6, 9]
        ]
final =[
        [1, 2, 3], 
        [8, 0, 4], 
        [7, 6, 5]
    ]
flag,k,distance = BFS(start, final)
if(flag==True):
    print("Initial Stage :  ",start)
else:
    while flag==False:
        t=ran()
        if(t!=final):
            flag,k,distance=BFS(t,final)
                print("Initial Stage : ",t)
                # print(t,k)
                # print("Initial Stage : ",t)
                print('Total No. of Iterations : ',k)
                print("Distance : ")
                print(distance)
                end = time.time()
                print("Time Taken : ",end - starttime)
                itrp