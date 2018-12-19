#!/usr/bin/env python3#
import Common

UP = (-1, 0)
DOWN = (1,0)
RIGHT = (0,1)
LEFT = (0,-1)

directions = (DOWN, RIGHT, LEFT, UP)
    
def getMoveDirection(coord1, coord2, grid):
    maxDirection = []
    minDist =  99999999
    for direction in directions:
        nextCoord = getNextCoord(coord1, direction)
        if(grid[nextCoord.row][nextCoord.col] != "."):
            continue
        dist = nextCoord.getManhattanDistance(coord2)
        if(dist == minDist):
            maxDirection.append(direction)
        elif(dist < minDist):
            maxDirection = []
            maxDirection.append(direction)
            minDist = dist
      
    newCoords = [(getNextCoord(coord1, direction), direction) for direction in maxDirection]
    if not newCoords:
        return None
        
    return min(newCoords, key=lambda coordPair: coordPair[0].row*len(grid) + coordPair[0].col)[1]
        

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
        adjacents = [adjacent for adjacent in target.coords.getAdjacents() if grid[adjacent.row][adjacent.col] == "." or grid[adjacent.row][adjacent.col] == unitNum]
        for adjacent in adjacents:
            dist = unit.coords.getManhattanDistance(adjacent)
            if(dist == 0):
                return False
            if(dist == minDist):
                closest.append(adjacent)
            elif(dist < minDist):
                closest = []
                closest.append(adjacent)
                minDist = dist
    if not closest:
        return False
    targetCoord = readingOrderMin(closest, len(grid))
    targetDirection = getMoveDirection(unit.coords, targetCoord, grid)
    if(not targetDirection):
        return False
    grid[unit.coords.row][unit.coords.col] = "."
    unit.coords = getNextCoord(unit.coords, targetDirection)
    grid[unit.coords.row][unit.coords.col] = unitNum
    
    return True

def getAttackTarget(unit, units, targets, grid):
    adjacentCoords = [adjacent for adjacent in unit.coords.getAdjacents()]
    adjacents = [adjacent for adjacent in adjacentCoords if grid[adjacent.row][adjacent.col] in targets]
    if(not adjacents):
        return None
    minHealth = 99999999
    minTargetCoords = []
    for adjacent in adjacents:
        targetUnit = units[grid[adjacent.row][adjacent.col]]
        if targetUnit.health == minHealth:
            minTargetCoords.append(adjacent)
        elif targetUnit.health < minHealth:
            minTargetCoords = [ adjacent ]
            minHealth = targetUnit.health
    
    targetCoord = readingOrderMin(minTargetCoords, len(grid))
    targetNum = grid[targetCoord.row][targetCoord.col]
    target = units[targetNum]
    return target
    
def attackUnit(unitNum, grid, units, goblins, elves):
    unit = units[unitNum]
    if( not unit.isAlive()):
        return
    
    targets = None
    if(unitNum in goblins):
        targets = elves
    else:
        targets = goblins
        
    target = getAttackTarget(unit, units, targets, grid)
    if not target:
        return
    
    unit.attack(target)

def removeDead(unitNums, units, grid):
    toRemove = []
    for unitNum in unitNums:
        if(not units[unitNum].isAlive()):
            toRemove.append(unitNum)
    
    for deleted in toRemove:
        coords = units[deleted].coords
        grid[coords.row][coords.col] = "."
        unitNums.remove(deleted)
        del units[deleted]

def printGrid(grid, goblins, elves):
    print("")
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            gridPos = grid[i][j]
            if gridPos in elves:
                print("E" + str(grid[i][j]), end="")
            elif gridPos in goblins:
                print("G" + str(grid[i][j]), end="")
            else:
                print(gridPos, end=" ")
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
                grid[row].append("#")
            elif c == ".":
                grid[row].append(".")
                
            elif c == "G":
                unitNum = len(units)
                units[unitNum] = Unit(Coordinate(row,col), 3, 200)
                goblins.append(unitNum)
                grid[row].append(unitNum)
            elif c == "E":
                unitNum = len(units)
                units[unitNum] = Unit(Coordinate(row,col), 3, 200)
                elves.append(unitNum)
                grid[row].append(unitNum)
    rounds = 0
    while len(goblins) > 0 and len(elves) > 0:
        
        for unitNum,unit in sorted(units.items(), key=lambda item: item[1].coords.row*len(grid) + item[1].coords.col ):
            if(not unit.isAlive()):
                continue
            moveUnit(unitNum, grid, units, goblins, elves)
            attackUnit(unitNum, grid, units, goblins, elves)
        removeDead(elves, units, grid)
        removeDead(goblins, units, grid)
        rounds += 1
        print(rounds)
        printGrid(grid, goblins, elves)
        #print(len(elves), len(goblins))

                
    return rounds
            
input = Common.inputAsLines()
#input = Common.inputAsString()

print(part1(input))
#print(part2(input))




