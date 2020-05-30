# -*- coding: utf-8 -*-
"""
Created on Sat May 16 09:01:18 2020

@author: marco
"""
MAZE = [[0,0,0,0,0,0,1,1],
        [1,1,0,1,0,1,1,1],
        [0,0,0,0,1,0,0,0],
        [1,0,1,0,1,1,0,1],
        [1,0,1,0,1,0,0,0],
        [1,1,0,0,0,1,0,1],
        [1,1,0,1,0,0,0,1],
        [1,1,1,1,1,1,0,0]]

START = [0,0]
END = [7,7]

visit = [[0 for _ in range(len(MAZE))] for _ in range(len(MAZE[0]))]
pathStack = [(START[0],START[1])]

def run(x,y):
    if [x,y] == END:
        print(pathStack)
        print("Completed")
    
    if x+1<len(MAZE[0]) and MAZE[y][x+1] == 0 and visit[y][x+1] == 0:
        visit[y][x+1] = 2
        pathStack.append([x+1,y])
        run(x+1,y)
        pathStack.pop()
        
    if x-1>len(MAZE[0]) and MAZE[y][x-1] == 0 and visit[y][x-1] == 0:
        visit[y][x-1] = 2
        pathStack.append([x-1,y])
        run(x-1,y)
    
    if y+1<len(MAZE[0]) and MAZE[y+1][x] == 0 and visit[y+1][x] == 0:
        visit[y+1][x] = 2
        pathStack.append([x,y+1])
        run(x,y+1)
    
    if y-1>len(MAZE[0]) and MAZE[y-1][x] == 0 and visit[y-1][x] == 0:
        visit[y-1][x] = 2
        pathStack.append([x,y-1])
        run(x,y-1)
    
run(START[0],START[1])
