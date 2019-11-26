import Common
import networkx as nx
import itertools

def getManhattanDist(coord1, coord2):
	return sum([abs(dim1 - dim2) for dim1,dim2 in zip(coord1, coord2)])


class Nanobot():
	def __init__(self, coordinates, radius):
		self.coordinates = coordinates
		self.radius = radius

	def overlaps_other(self, other_nano):
		return getManhattanDist(self.coordinates, other_nano.coordinates) <= self.radius + other_nano.radius
		
	def isWithinBounds(self, bounds):
		return all([True for coord, bound in zip(self.coordinates, bounds) if (coord + self.radius >= bound[0]) and (coord - self.radius) <= bound[1]])

def getCoordMin(nanobots, dim):
	return min(nanobots, key= lambda bot: bot.coordinates[dim]).coordinates[dim]
	
def getCoordMax(nanobots, dim):
	return max(nanobots, key= lambda bot: bot.coordinates[dim]).coordinates[dim]
	
def subdividedbounds(bounds):
	subboundPerms = itertools.product(range(2), repeat=3)
	subDividedbounds = []
	newboundLengths = [int((bound[1] - bound[0])/2) for bound in bounds]
	if all([length == 0 for length in newboundLengths]):
		return None
	for topCorner in subboundPerms:
		subdividedbound = [ (bound[0] + newLength * dim, bound[0] + newLength * (dim + 1)) for bound,dim, newLength in zip(bounds, topCorner, newboundLengths)]
		subDividedbounds.append(subdividedbound)
	return subDividedbounds
	
def getMinManhattanDistToOrigin(bounds):
	minCoords = [ min(abs(bound[0]), abs(bound[1])) for bound in bounds ] 
	return getManhattanDist(minCoords, (0,0,0))
	
def getBestCoordinateDistToOrigin(bounds, nanobots):
	dividedbounds = subdividedbounds(bounds)
	print(bounds)
	if not dividedbounds:
		return sum([1 for nanobot in nanobots if nanobot.isWithinBounds(bounds)]), getMinManhattanDistToOrigin(bounds)
	maxCount = -1
	bestbounds = []
	for bound in dividedbounds:
		count = sum([1 for nanobot in nanobots if nanobot.isWithinBounds(bound)])
		if count > maxCount:
			maxCount = count
			bestbounds = [ bound ]
		elif count == maxCount:
			bestbounds.append(bound)
	best =[getBestCoordinateDistToOrigin(bound, nanobots) for bound in bestbounds]
	return best

class OverlappingNanoSystem:
	def __init__(self, nanobots):
		self.nanobots = nanobots
		self.nano_count = len(self.nanobots)

	def find_best_coord_within(self):
		nano_coords = [ nano.coordinates for nano in self.nanobots ]
		max_bounds =


def part2(input):
	nanobots = []
	for line in input:
		numbers = Common.numbers(line)
		nanobots.append(Nanobot( tuple(numbers[:3]), numbers[3]))

	overlap_graph = nx.Graph()
	for idx, nano in enumerate(nanobots):
		overlap_graph.add_node(idx)
		for other_idx, other_nano in enumerate(nanobots):
			if idx == other_idx or nano.overlaps_other(other_nano):
				overlap_graph.add_edge(idx, other_idx)
	best_overlapping_nanos_indices = max(nx.find_cliques(overlap_graph), key=lambda clique : len(clique))

	best_overlapping_nanos = [nanobots[idx] for idx in best_overlapping_nanos_indices]

	#find maximal overlapping set of nanos
	#iterate over intersection by
		#subdividing, and only keeping closest subdivision to origin that overlaps with all nanos
	#repeat
	return ""
	bounds = [ (getCoordMin(nanobots, i), getCoordMax(nanobots, i)) for i in range(3) ]
	
	return getBestCoordinateDistToOrigin(bounds, nanobots)
	
input = Common.inputAsLines()

print(part2(input))