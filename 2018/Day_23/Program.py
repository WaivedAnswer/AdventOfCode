import Common
from collections import defaultdict
import itertools

def getManhattanDist(coord1, coord2):
	return sum([abs(dim1 - dim2) for dim1,dim2 in zip(coord1, coord2)])

class Nanobot():
	def __init__(self, coordinates, radius):
		self.coordinates = coordinates
		self.radius = radius
		
	def isWithinBounds(self, ranges):
		return all([True for coord,range in zip(self.coordinates, ranges) if (coord + self.radius >= range[0]) and (coord - self.radius) <= range[1]])

def getCoordMin(nanobots, dim):
	return min(nanobots, key= lambda bot: bot.coordinates[dim]).coordinates[dim]
	
def getCoordMax(nanobots, dim):
	return max(nanobots, key= lambda bot: bot.coordinates[dim]).coordinates[dim]
	
def subdividedRanges(ranges):
	subRangePerms = itertools.product(range(2), repeat=3)
	subDividedRanges = []
	newRangeLengths = [int((range[1] - range[0])/2) for range in ranges]
	if all([length == 0 for length in newRangeLengths]):
		return None
	for topCorner in subRangePerms:
		subdividedRange = [ (range[0] + newLength * dim, range[0] + newLength * (dim + 1)) for range,dim, newLength in zip(ranges, topCorner, newRangeLengths)]
		subDividedRanges.append(subdividedRange)
	return subDividedRanges
	
def getMinManhattanDistToOrigin(ranges):
	minCoords = [ min(abs(range[0]), abs(range[1])) for range in ranges ] 
	return getManhattanDist(minCoords, (0,0,0))
	
def getBestCoordinateDistToOrigin(ranges, nanobots):
	dividedRanges = subdividedRanges(ranges)
	print(ranges)
	if not dividedRanges:
		return sum([1 for nanobot in nanobots if nanobot.isWithinBounds(ranges)]), getMinManhattanDistToOrigin(ranges)
	maxCount = -1
	bestRanges = []
	for range in dividedRanges:
		count = sum([1 for nanobot in nanobots if nanobot.isWithinBounds(range)])
		if count > maxCount:
			maxCount = count
			bestRanges = [ range ]
		elif count == maxCount:
			bestRanges.append(range)
	best =[getBestCoordinateDistToOrigin(range, nanobots) for range in bestRanges]
	return best
	

def part2(input):
	nanobots = []
	for line in input:
		numbers = Common.numbers(line)
		nanobots.append(Nanobot(tuple(numbers[:3]), numbers[3]))
		
	ranges = [ (getCoordMin(nanobots, i), getCoordMax(nanobots, i)) for i in range(3) ]
	
	return getBestCoordinateDistToOrigin(ranges, nanobots)
	
input = Common.inputAsLines()

print(part2(input))