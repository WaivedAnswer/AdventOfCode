#!/usr/bin/env python#
import Common
import re
from collections import defaultdict
from collections import OrderedDict
import itertools


def distFromOrigin(x, y):
	return manhattanDist(x, y, 0, 0)


def manhattanDist(x1, y1, x2, y2):
       return abs(x1 - x2) + abs(y1 - y2)


def getClosest(coords, coord):
       minD = 99999999
       closest = None
       for x, y in coords:
              dist = manhattanDist(x, y, coord[0], coord[1])
              if(dist == minD):
                     closest = None
              elif(dist < minD):
                     closest = (x, y)
                     minD = dist
       return closest


def getDistVectors(dist):
	possibles = range(-dist, dist + 1)
	return [pair for pair in itertools.product(possibles, repeat=2) if distFromOrigin(pair[0], pair[1]) == dist]


def getCoordsAtDist(coord, dist):
	if(dist == 0):
		return [coord]
	dists = getDistVectors(dist)
	preSet = [(coord[0] + dist[0], coord[1] + dist[1]) for dist in dists]
	return preSet


def printClosest(closest, maxX, maxY, names, coords):
       mapC = "\n"
       for i in range(0, maxX):
              for j in range(0, maxY):
                     if((i, j) not in closest):
                            mapC += "0"
                     elif(closest[(i, j)] == None or closest[i, j] == ()):
                            mapC += "."
                     elif((i, j) not in coords):
                            mapC += names[closest[(i, j)]].lower()
                     else:
                            mapC += names[closest[(i, j)]]
              mapC += "\n"
       print(mapC)
       
def getTotals(closest, maxX, maxY, names, coords):
       coordTotals = defaultdict(int)
       for i in range(0, maxX):
              for j in range(0, maxY):
                     if((i, j) not in closest):
                            continue
                     elif(closest[(i, j)] == None or closest[i, j] == ()):
                            continue
                     elif((i, j) not in coords):
                            coordTotals[names[closest[(i, j)]]] += 1
                     else:
                            coordTotals[names[closest[(i, j)]]] += 1
       return coordTotals

def countClosest(coords, names):
       closest = defaultdict(tuple)
       minX = min(coords, key=lambda x: x[0])[0]
       minY = min(coords, key=lambda x: x[1])[1]
       maxX = max(coords, key=lambda x: x[0])[0]
       maxY = max(coords, key=lambda x: x[1])[1]
       edgeCoords = set([coord for coord in coords if coord[0] == minX or coord[0] == maxX or coord[1] == minY or coord[1] == maxY])
       stillGrowing = True
       growDist = 0
       growingCoords = coords
       while stillGrowing:
              #printClosest(closest, maxX, maxY, names, coords)
              stillGrowing = False
              newCoords = set()
              coordTouches = defaultdict(set)
              ties = set()
              toRemove = []
              for coord in growingCoords:
                     touches = getCoordsAtDist(coord, growDist)
                     coordTouches[coord] = [touch for touch in touches if not touch in closest or touch[0] < 0 or touch[1] < 0]
                     if(not coordTouches):
                            toRemove.append(coord)
                     ties = ties.union(newCoords.intersection({tup for tup in touches}))
                     newCoords = newCoords.union({tup for tup in touches})
                     
              growingCoords = [coord in growinCoords if coord not in toRemove]
              
              for coord in coordTouches:
                     for touch in coordTouches[coord]:
                            if(touch in ties): # tie 
                                   closest[touch] = None 
                            else: 
                                   closest[touch] = coord 
                            if coord not in edgeCoords: 
                                   stillGrowing = True

              growDist += 1
              print(growDist)
       #printClosest(closest, maxX, maxY, names, coords)
       totals = getTotals(closest, maxX, maxY, names, coords)
       return Common.maxValuePair(totals)
    
    
def part1(input):
	coords = []
	names = {}
	coordName = 'A'
	for line in input:
		numbers = Common.numbers(line)
		y = numbers[0]
		x = numbers[1]
		coords.append((x,y))
		names[(x,y)] = coordName
		coordName = chr(ord(coordName) + 1)
	return countClosest(coords, names)
            
input = Common.inputAsLines()
# input = Common.inputAsString()
# print(getDistVectors(2))
# assert(manhattanDist())
print(part1(input))
# print(part2(input))
