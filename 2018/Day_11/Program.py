#!/usr/bin/env python3#
import Common
import time
from collections import defaultdict

def getHundreds(num):
       if(num < 100):
              return 0
       return int(str(num)[-3])
       
def getPowerLevel(x,y,serialNum):
       rackId = x + 10
       powerLevel = rackId * y + serialNum
       powerLevel = powerLevel * rackId
       powerLevel = getHundreds(powerLevel) - 5
       return powerLevel
       
def sumGrid(grid):
       return sum([sum(row) for row in grid])
       
def highestTopLeft3x3(grid):
	   preCalced = defaultdict(lambda: defaultdict(int))
	   maxSlice, maxSum = getMaxForSize(3, grid, preCalced)
	   return gridSliceToXY(maxSlice), maxSum
	   
def sumBottomEdge(grid, i, j , size):
	return sum(grid[i + size - 1][j:j+size])
	   
def sumRightEdge(grid, i, j , size):
	return sum([row[j + size - 1] for row in grid[i:i+size]])
	   
def calcGridForSize(size, grid, preCalced):
       if(size in preCalced):
              return preCalced[size]
       if(size == 1):
              for i in range(0, len(grid)):
                     for j in range(0, len(grid)):
                            preCalced[size][(i,j)] = grid[i][j]
       else:
              for i in range(0, len(grid) - size + 1):
                     for j in range(0, len(grid) - size + 1):
                            preCalced[size][(i,j)] = calcGridForSize(size - 1, grid, preCalced)[(i,j)] + sumBottomEdge(grid, i, j, size) + sumRightEdge(grid,i,j,size) - grid[i+size - 1][j + size - 1]
                            
       return preCalced[size]

def getMaxForSize(size, grid, preCalced):
       preCalced = calcGridForSize(size,grid,preCalced)
       return max(preCalced.items(), key = lambda x:x[1])
	  
def gridSliceToXY(gridSlice):
	return (gridSlice[1] + 1, gridSlice[0] + 1)
       
def highestTopLeftAny(grid):
       maxGridSlice = (0,0)
       maxSum = 0
       gridSize = 0
       preCalced = defaultdict(lambda: defaultdict(int))
       for k in range(1, len(grid)):
              maxGridSliceForSize, maxSumForSize = getMaxForSize(k, grid, preCalced)
              maxSum = max(maxSum, maxSumForSize)
              if(maxSum == maxSumForSize):
                     maxGridSlice = maxGridSliceForSize
                     gridSize = k
                            
       return gridSliceToXY(maxGridSlice), maxSum, gridSize

def getPowerGrid(serialNum):
	grid = []
	for i in range(1, 301):
			grid.append([])
			for j in range(1, 301):
					grid[i-1].append(getPowerLevel(j, i, serialNum))
	return grid
	
def part1(serialNum):
	grid = getPowerGrid(serialNum) 
	return highestTopLeft3x3(grid)
       
def part2(serialNum):
	grid = getPowerGrid(serialNum) 
	return highestTopLeftAny(grid)
            
input = Common.inputAsLines()

start1 = time.clock()
print(part1(5719))
end1 = time.clock()
print(end1 - start1)

start2 = time.clock()
print(part2(5719))
end2 = time.clock()
print(end2 - start2)

#print(part2(input))




