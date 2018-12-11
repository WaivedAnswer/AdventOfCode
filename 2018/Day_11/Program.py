#!/usr/bin/env python3#
import Common

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

def get3Slice(grid, i, j):
       return [row[j:j+3] for row in grid[i:i+3]]
       
def getAnySlice(grid, i, j, size):
       return [row[j:j+size] for row in grid[i:i+size]]
       
def sumGrid(grid):
       return sum([sum(row) for row in grid])
       
def highestTopLeft3x3(grid):
       maxSlice = (0,0)
       maxSum = 0
       for i in range(0, len(grid) - 3):
              for j in range(0, len(grid[i]) - 3):
                     slice3 = get3Slice(grid, i, j)
                     total = sumGrid(slice3)
                     maxSum = max(maxSum, total)
                     if(maxSum == total):
                            maxSlice = (j+1, i+1)
                            
       return maxSlice, maxSum

def calculate2s(grid):
       total2s = defaultdict(int)
       
       for i in range(0, len(grid) - 2):
              for j in range(0, len(grid[i]) - 2):
                     sliceAny = getAnySlice(grid, i, j, 2)
                     total = sumGrid(sliceAny)
                     total2s[(i,j)] = total
       return total2s
       
def calcGridForSize(size, grid, preCalced):
       if(size in preCalced):
              return preCalced[size]
       if(k == 1):
              for i in range(0, len(grid)):
                     for j in range(0. len(grid)):
                            preCalced[size][(i,j)] = grid[i][j]
       else:
              for i in range(0, len(grid) - size + 1):
                     for j in range(0, len(grid) - size + 1):
                            
                            preCalced[size][(i,j)] = calcGridForSize(size - 1, grid, preCalced) + sum([])
                            
       return preCalced[size]

def getMaxForSize(size, grid, preCalced):
       calcGridForSize(size,grid,preCalced)
       return size, max(preCalced[size].items(), key = lambda x:x[1]))
       
def highestTopLeftAny2(grid):
       maxSlice = (0,0)
       maxSum = 0
       gridSize = 0
       preCalced = defaultdict(lambda: defaultdict(int))
       for k in range(1, len(grid)):
              maxSliceForSize, maxSumForSize = getMaxForSize(k, grid, preCalced)
              maxSum = max(maxSum, maxSumForSize)
              if(maxSum == maxSumForSize):
                     maxSlice = maxSliceForSize
                     gridSize = k
                            
       return maxSlice, maxSum, gridSize
       
def highestTopLeftAny(grid):
       maxSlice = (0,0)
       maxSum = 0
       gridSize = 0
       for k in range(1, len(grid)):
              for i in range(0, len(grid) - k):
                     for j in range(0, len(grid[i]) - k):
                            sliceAny = getAnySlice(grid, i, j, k)
                            total = sumGrid(sliceAny)
                            maxSum = max(maxSum, total)
                            if(maxSum == total):
                                   maxSlice = (j+1, i+1)
                                   gridSize = k
                            
       return maxSlice, maxSum, gridSize
       
def part1(input):
       serialNum = input
       grid = []
       for i in range(1, 301):
              grid.append([])
              for j in range(1, 301):
                     grid[i-1].append(getPowerLevel(j, i, serialNum))
       
       
       return highestTopLeft3x3(grid)
       
def part2(input):
       serialNum = input
       grid = []
       for i in range(1, 301):
              grid.append([])
              for j in range(1, 301):
                     grid[i-1].append(getPowerLevel(j, i, serialNum))
       
       
       return highestTopLeftAny(grid)
            
input = Common.inputAsLines()
#input = Common.inputAsString()
grid = [[1,2,3,2],[4,5,6,3],[7,8,9,1],[2,4,5,2]]

#print(part1(18))
#print(part1(42))
#print(part1(5719))
print(part2(5719))

#print(part2(input))




