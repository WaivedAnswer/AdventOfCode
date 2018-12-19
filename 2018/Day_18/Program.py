#!/usr/bin/env python3#
import Common
from enum import Enum
from collections import defaultdict

UP = (-1, 0)
DOWN = (1,0)
RIGHT = (0,1)
LEFT = (0,-1)
UPRIGHT = (-1,1)
UPLEFT = (-1,-1)
DOWNRIGHT = (1, 1)
DOWNLEFT = (1, -1)
     
directions = (DOWN, RIGHT, LEFT, UP, UPRIGHT, UPLEFT, DOWNRIGHT, DOWNLEFT)

def getAdjacents(currCoords):
    return [getNextCoord(currCoords, direction) for direction in directions]

def getNextCoord(coords, movementVec):
    row = coords[0] + movementVec[0]
    col = coords[1] + movementVec[1]
    return (row, col)
    
def isCoordInGrid(coord, grid):
    return coord[0] < len(grid) and coord[0] >= 0 and coord[1] < len(grid[0]) and coord[1] >= 0
    

    
def morphGrid(grid):
    newGrid = defaultdict(lambda: defaultdict(chr))
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            adjacents = [adjacent for adjacent in getAdjacents((i,j)) if isCoordInGrid(adjacent,grid)]
            if grid[i][j] == "." and sum(1 for adjacent in adjacents if grid[adjacent[0]][adjacent[1]] == "|") >= 3:
                newGrid[i][j] = "|"
            elif grid[i][j] == "|" and sum(1 for adjacent in adjacents if grid[adjacent[0]][adjacent[1]] == "#") >= 3:
                newGrid[i][j] = "#"
            elif grid[i][j] == "#" and not (sum(1 for adjacent in adjacents if grid[adjacent[0]][adjacent[1]] == "#") >= 1 and sum(1 for adjacent in adjacents if grid[adjacent[0]][adjacent[1]] == "|") >= 1):
                newGrid[i][j] = "."
            else:
                newGrid[i][j] = grid[i][j]
    return newGrid
    
def printGrid(grid):
    print("")
    for row in range(len(grid)):
        for col in range(len(grid[row])):
            print(grid[row][col], end="")
        print("")
    print("")
    
def getGridScore(grid):
    trees = 0 
    lumber = 0
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if(grid[i][j] == "|"):
                trees += 1
            elif(grid[i][j] == "#"):
                lumber += 1
                
    return trees * lumber
    
def part1(input):
    gridLength = 10
    grid = defaultdict(lambda: defaultdict(chr))
    for i,line in enumerate(input):
        for j,c in enumerate(line):
            print(i,j, c)
            grid[i][j] = c
    print(grid)
    printGrid(grid)
    totals = defaultdict(lambda: [])
    for minute in range(1,11):
        grid = morphGrid(grid)
        total = getGridScore(grid)
        if(total in totals):
            print(totals[total],minute)
        totals[total].append(minute)
    
    return getGridScore(grid)
    
def part2(input):
    gridLength = 10
    grid = defaultdict(lambda: defaultdict(chr))
    for i,line in enumerate(input):
        for j,c in enumerate(line):
            print(i,j, c)
            grid[i][j] = c
    #print(grid)
    #printGrid(grid)
    totals = defaultdict(lambda: [])
    maxMorph = 568 + (1000000000 - 568) % 28
    for minute in range(1,maxMorph + 1):
        grid = morphGrid(grid)
        total = getGridScore(grid)
        if(total in totals):
            print(totals[total],minute)
        totals[total].append(minute)
    
    return getGridScore(grid)
                
input = Common.inputAsLines()
#input = Common.inputAsString()

#print(part1(input))
print(part2(input))




