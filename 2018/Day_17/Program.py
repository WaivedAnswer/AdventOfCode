#!/usr/bin/env python3#
import Common
import random
from collections import defaultdict, deque

import sys

class recursionlimit:
    def __init__(self, limit):
        self.limit = limit
        self.old_limit = sys.getrecursionlimit()

    def __enter__(self):
        sys.setrecursionlimit(self.limit)

    def __exit__(self, type, value, tb):
        sys.setrecursionlimit(self.old_limit)

UP = (-1, 0)
DOWN = (1,0)
RIGHT = (0,1)
LEFT = (0,-1)

def getNextCoord(coords, movementVec):
    row = coords[0] + movementVec[0]
    col = coords[1] + movementVec[1]
    return (row, col)
    
def printGrid(grid, xRange, yRange):
    print("")
    for row in range(yRange[0] - 15, yRange[1] + 16):
        for col in range(xRange[0] - 15, xRange[1] + 16):
            print(getGridItem((row,col), grid), end="")
        print("")
    print("")

def getGridItem(coord, grid):
    row,col = coord
    if(row not in grid or col not in grid[row]):
        return "."
        
    return grid[row][col]
    
def isSideClosed(grid, currCoords, direction):
    if getGridItem(currCoords, grid) == "#":
        return True
    downCoord = getNextCoord(currCoords, DOWN)
    downGridItem = getGridItem(downCoord, grid)
    isSupported = downGridItem == "#" or downGridItem == "~"
    
    return isSupported and isSideClosed(grid, getNextCoord(currCoords, direction), direction)
    
def isClosed(grid, currCoords):
    return isSideClosed(grid, currCoords, LEFT) and isSideClosed(grid, currCoords, RIGHT)
    
def addCoordToQueue(coord, fillQueue, filled):
     if coord not in filled:
         fillQueue.append(coord)

def flowFill(grid, xRange, yRange, currCoords, fillQueue, filled):
    row,col = currCoords
    #print(row,col)
    if currCoords in filled or getGridItem(currCoords, grid) == "#" or getGridItem(currCoords, grid) == "~":
        return
    elif row > yRange[1]:
        return 

    grid[row][col] = "|"
    filled[currCoords] = True
    
    downCoord = getNextCoord(currCoords, DOWN)
    flowFill(grid, xRange, yRange, downCoord, fillQueue, filled)
    downGridItem = getGridItem(downCoord, grid)
    
    if(downGridItem == "#" or downGridItem == "~"):
        if isClosed(grid, currCoords):
            grid[row][col] = "~"
        addCoordToQueue(getNextCoord(currCoords, LEFT), fillQueue, filled)
        addCoordToQueue(getNextCoord(currCoords, RIGHT), fillQueue, filled)
    

    
    #printGrid(grid, xRange, yRange)
    
def getGridWaterCount(grid, minY, maxY):
    total = 0
    for row in grid:
        for col in grid[row]:
            if (grid[row][col] == "~" or grid[row][col] == "|") and row >= minY and row <= maxY:
                total += 1
    return total
    
def getSettledWaterCount(grid, minY, maxY):
    total = 0
    for row in grid:
        for col in grid[row]:
            if (grid[row][col] == "~") and row >= minY and row <= maxY:
                total += 1
    return total
    
        
def part1(input):
    grid = defaultdict(lambda: defaultdict(chr))
    grid[0][500] = "+"
    minX = 99999999
    maxX = -99999999
    minYClay = 9999999999999
    for line in input:
        numbers = Common.numbers(line)
        if line.index("x") < line.index("y"):
            x = numbers[0]
            minX = min(minX, x)
            maxX = max(maxX, x)
            yRange1 = numbers[1]
            minYClay = min(minYClay, yRange1)
            yRange2 = numbers[2]
            for y in range(yRange1, yRange2 + 1):
                grid[y][x] = "#"
        else:
            y = numbers[0]
            minYClay = min(minYClay, y)
            xRange1 = numbers[1]
            xRange2 = numbers[2]
            minX = min(minX, xRange1)
            maxX = max(maxX, xRange2)
            for x in range(xRange1, xRange2 + 1):
                grid[y][x] = "#"
        numbers = Common.numbers(line)
        
    minY = min(grid)
    maxY = max(grid)
    #printGrid(grid, (minX,maxX), (minY, maxY))
    source = (1,500)
    prevScore = 0
    while True:
        fillQueue = deque([source])
        filled = {}
        while len(fillQueue) > 0:
            flowFill(grid, (minX,maxX), (minY, maxY), fillQueue.popleft(), fillQueue, filled)
            #printGrid(grid,(minX,maxX), (minY, maxY))
        currScore = getGridWaterCount(grid, minYClay, maxY)
        print(currScore)
        if(currScore == prevScore):
            break
        prevScore = currScore
    printGrid(grid,(minX,maxX), (minY, maxY))
    return getGridWaterCount(grid, minYClay, maxY)
    
def part2(input):
    grid = defaultdict(lambda: defaultdict(chr))
    grid[0][500] = "+"
    minX = 99999999
    maxX = -99999999
    minYClay = 9999999999999
    for line in input:
        numbers = Common.numbers(line)
        if line.index("x") < line.index("y"):
            x = numbers[0]
            minX = min(minX, x)
            maxX = max(maxX, x)
            yRange1 = numbers[1]
            minYClay = min(minYClay, yRange1)
            yRange2 = numbers[2]
            for y in range(yRange1, yRange2 + 1):
                grid[y][x] = "#"
        else:
            y = numbers[0]
            minYClay = min(minYClay, y)
            xRange1 = numbers[1]
            xRange2 = numbers[2]
            minX = min(minX, xRange1)
            maxX = max(maxX, xRange2)
            for x in range(xRange1, xRange2 + 1):
                grid[y][x] = "#"
        numbers = Common.numbers(line)
        
    minY = min(grid)
    maxY = max(grid)
    #printGrid(grid, (minX,maxX), (minY, maxY))
    source = (1,500)
    prevScore = 0
    while True:
        fillQueue = deque([source])
        filled = {}
        while len(fillQueue) > 0:
            flowFill(grid, (minX,maxX), (minY, maxY), fillQueue.popleft(), fillQueue, filled)
            #printGrid(grid,(minX,maxX), (minY, maxY))
        currScore = getGridWaterCount(grid, minYClay, maxY)
        print(currScore)
        if(currScore == prevScore):
            break
        prevScore = currScore
    printGrid(grid,(minX,maxX), (minY, maxY))
    return getSettledWaterCount(grid, minYClay, maxY)
            
input = Common.inputAsLines()
#input = Common.inputAsString()

#print(part1(input))
print(part2(input))




