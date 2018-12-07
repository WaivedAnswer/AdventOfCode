#!/usr/bin/env python#
import Common
import re
from collections import defaultdict
from collections import OrderedDict
import itertools


def distFromOrigin(x,y):
	return manhattanDist(x,y,0,0)
	
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
	
def getDistVectors(dist):
	possibles = range(-dist, dist + 1)
	return [ pair for pair in itertools.permutations(possibles, 2) if distFromOrigin(pair[0], pair[1]) == dist]
	
    
def getCoordsAtDist(coord, dist):
	if(dist == 0):
		return [coord]
	dists = getDistVectors(dist)
	preSet = [(coord[0] + dist[0], coord[1] + dist[1]) for dist in dists]
	return preSet
    
def countClosest(coords, names):
	closest = defaultdict(tuple)
	minX = min(coords, key = lambda x:x[0])[0]
	minY = min(coords, key = lambda x:x[1])[1]
	maxX = max(coords, key = lambda x:x[0])[0]
	maxY = max(coords, key = lambda x:x[1])[1]
	edgeCoords = set([coord for coord in coords if coord[0] == minX or coord[0] == maxX or coord[1] == minY or coord[1] == maxY])
	#print(minX, minY, maxX, maxY, edgeCoords)
	stillGrowing = True
	growDist = 0
	coordTotals = defaultdict(int)
	while stillGrowing:
		stillGrowing = False
		newCoords = set()
		coordTouches = defaultdict(set)
		for coord in coords:
			touches = getCoordsAtDist(coord, growDist)
			coordTouches[coord] = touches
			newCoords = newCoords.union({tup for tup in coordTouches[coord] if tup not in newCoords})
		for coord in coordTouches:
			for touch in coordTouches[coord]:
				if(touch in closest or touch[0] < 0 or touch[1] < 0): # already has closest
					continue
				elif(touch not in newCoords): #tie
					closest[touch] = None
				else:
					closest[touch] = coord
				if(coord not in edgeCoords):
					stillGrowing = True
		growDist += 1
		
	for i in range(0, maxX + 1):
		for j in range(0, maxY + 2):
			if(closest[(i,j)] == None or closest[i,j] == ()):
				print(".", end = "")
			elif((i,j) not in coords):
				print(names[closest[(i,j)]].lower(), end = "")
			else:
				print(names[closest[(i,j)]], end = "")
		print("")
	
	#print (coordTotals)
	return Common.maxValuePair(coordTotals)
    
    
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
#input = Common.inputAsString()

#assert(manhattanDist())
print(part1(input))
#print(part2(input))




