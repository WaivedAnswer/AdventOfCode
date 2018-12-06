#!/usr/bin/env python#
import Common
import re
from collections import defaultdict
from collections import OrderedDict
import itertools

def manhattanDist(x1,y1,x2,y2):
    return abs(x1-x2) + abs(y1-y2)
    
def getClosest(coords, coord):
    minD = 99999999
    closest = None
    for x,y  in coords:
        dist = manhattanDist(x,y, coord[0], coord[1])
        if( dist == minD):
            closest = None
        elif(dist < minD):
            closest = (x,y)
            minD = dist
    return closest
    
def findClosest(coords, coord, minX, minY, maxX, maxY, seen):
    closest = getClosest(coords, coord)
    if(closest and (closest[0] == minX or closest[1] == minY or closest[0] == maxX or closest[1] == maxY)):
        return None
    return closest
    
def growFromCoord(coordMap, closest, coord):
    
def countClosest(coords):
    closest = {}
    coordMap = defaultdict(lambda: defaultdict(int))
    minX = min(coords, key = lambda x:x[0])
    minY = min(coords, key = lambda x:x[1])
    maxX = max(coords, key = lambda x:x[0])
    maxY = max(coords, key = lambda x:x[1])
    edgeCoords = set([coord for coord in coords if coord[0] == minX or coord[0] == maxX or coord[1] == minY or coord[1] == maxY])
    for coord in coords:
        
    
    
def part1(input):
    coords = []
    coordNum = 1
    for line in input:
        numbers = Common.numbers(line)
        x = numbers[0]
        y = numbers[1]
        coords.append((x,y))
    
    return countClosest(coords)
            
input = Common.inputAsLines()
#input = Common.inputAsString()

#assert(manhattanDist())
print(part1(input))
#print(part2(input))




