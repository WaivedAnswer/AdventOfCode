#!/usr/bin/env python3#
import Common

UP = (-1, 0)
DOWN = (1,0)
RIGHT = (0,1)
LEFT = (0,-1)

directions = (DOWN, RIGHT, LEFT, UP)

def makeVecFrom(coord1, coord2):
    return (coord2.row - coord1.row, coord2.col - coord1.col)

def dotProduct(vec1, vec2):
    return vec1[0] * vec2[0] + vec1[1] * vec2[1]
    
def getMoveDirection(coord1, coord2, grid):
    coordVector = makeVecFrom(coord1, coord2)
    maxDirection = []
    maxDot =  -9999999
    for direction in directions:
        nextCoord = getNextCoord(coord1, direction)
        if(grid[nextCoord.row][nextCoord.col][0] != "."):
            continue
        dot = dotProduct(direction, coordVector)
        if(dot <= 1):
            return False
        if(dot == maxDot):
            maxDirection.append(direction)
        elif(dot > maxDot):
            maxDirection = []
            maxDirection.append(direction)
            maxDot = dot
    
    newCoords = [getNextCoord(coord1, direction) for direction in maxDirection]
    return readingOrderMin(maxCoords, len(grid))
        

def getNextCoord(coords, movementVec):
    row = coords.row + movementVec[0]
    col = coords.col + movementVec[1]
    return Coordinate(row, col)

class Coordinate:
    def __init__(self, row, col):
        self.row = row
        self.col = col  
        
    def getManhattanDistance(self, otherRow, otherCol):
        return abs(self.row - otherRow) + abs(self.col - otherCol)
    
    def getManhattanDistance(self, otherCoord):
        return abs(self.row - otherCoord.row) + abs(self.col - otherCoord.col)
        
    def getAdjacents(self):
        return [getNextCoord(self, direction) for direction in directions]
        
class Unit:
    def __init__(self, coords, attackPower, health):
        self.coords = coords
        self.attackPower = attackPower
        self.health = health
        
    def attack(self, other):
        other.health -= self.attackPower
        
    def isAlive(self):
        return self.health > 0

def readingOrderMin(closest, gridLength):
    return min(closest, key=lambda coord: coord.row*gridLength + coord.col)

def moveUnit(unitNum, grid, units, goblins, elves):      
    unit = units[unitNum]
    if( not unit.isAlive()):
        return False
    
    targets = None
    if(unitNum in goblins):
        targets = elves
    else:
        targets = goblins
    closest = []
    minDist = 999999999999
    for targetNum in targets:
        target = units[targetNum]
        adjacents = [adjacent for adjacent in target.coords.getAdjacents() if (grid[adjacent.row][adjacent.col][1] == None and grid[adjacent.row][adjacent.col][0] == ".")]
        for adjacent in adjacents:
            dist = unit.coords.getManhattanDistance(adjacent)
            if(dist <= 1):
                return False
            if(dist == minDist):
                closest.append(adjacent)
            elif(dist < minDist):
                closest = []
                closest.append(adjacent)
                minDist = dist
    
    targetCoord = readingOrderMin(closest, len(grid))
    print(targetCoord)
    targetDirection = getMoveDirection(unit.coords, targetCoord, grid)
    if(not targetDirection):
        return False
    print(targetDirection)
    grid[unit.coords.row][unit.coords.col] = (".", None)
    print(unit.coords)
    unit.coords = getNextCoord(unit.coords, targetDirection)
    print(unit.coords)
    grid[unit.coords.row][unit.coords.col] = (".", unitNum)
    
    return True
    
def attackUnit(unitNum, grid, units, goblins, elves):
    unit = units[unitNum]
    if( not unit.isAlive()):
        return
    
    targets = None
    if(unitNum in goblins):
        targets = elves
    else:
        targets = goblins
    adjacentCoords = [adjacent for adjacent in unit.coords.getAdjacents()]
    #for adjacent in adjacentCoords:
        #print(grid[adjacent.row][adjacent.col][1])
    adjacents = [adjacent for adjacent in adjacentCoords if grid[adjacent.row][adjacent.col][1] in targets]
    if(not adjacents):
        return
    print(adjacents)
    targetCoord = readingOrderMin(adjacents, len(grid))
    targetNum = grid[targetCoord.row][targetCoord.col][1]
    target = units[targetNum]
    unit.attack(target)
    print(target.health)

def removeDead(unitNums, units):
    toRemove = []
    for unitNum in unitNums:
        if(not units[unitNum].isAlive()):
            toRemove.append(unitNum)
         
    unitNums = [unit for unit in unitNums if unit not in toRemove]
    
    for deleted in toRemove:
        del units[deleted]

def printGrid(grid, goblins, elves):
    print("")
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            gridPos = grid[i][j]
            if gridPos[1] in elves:
                print("E", end="")
            elif gridPos[1] in goblins:
                print("G", end="")
            else:
                print(gridPos[0], end="")
        print("")
    print("")
def part1(input):
    grid = []
    goblins = []
    elves = []
    units = {}
    for row,line in enumerate(input):
        grid.append([])
        for col,c in enumerate(line):
            if c == "#":
                grid[row].append(("#", None))
            elif c == ".":
                grid[row].append((".", None))
                
            elif c == "G":
                unitNum = len(units)
                units[unitNum] = Unit(Coordinate(row,col), 3, 200)
                goblins.append(unitNum)
                grid[row].append((".", unitNum))
            elif c == "E":
                unitNum = len(units)
                units[unitNum] = Unit(Coordinate(row,col), 3, 200)
                elves.append(unitNum)
                grid[row].append((".", unitNum))
    rounds = 0
    while len(goblins) > 0 and len(elves) > 0:
        for unitNum,unit in sorted(units.items(), key=lambda item: item[1].coords.row*len(grid) + item[1].coords.col ):
            if(not unit.isAlive()):
                continue
            elif( not moveUnit(unitNum, grid, units, goblins, elves)):
                attackUnit(unitNum, grid, units, goblins, elves)
        removeDead(elves, units)
        removeDead(goblins, units)
        printGrid(grid, goblins, elves)
        #print(len(elves), len(goblins))
        rounds += 1
                
    return rounds
            
input = Common.inputAsLines()
#input = Common.inputAsString()

print(part1(input))
#print(part2(input))




