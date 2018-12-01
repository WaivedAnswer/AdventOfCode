import Common

class destination:
	def __init__(self, source):
		self.source = source
		self.destinations = []
		
	def add_destination(self, destination, distance):
		self.destinations.append((destination, distance))
		
	def get_destinations(self):
		return self.destinations

def get_shortest_route_from(source, visitedLocations, dist_map):
	newVisitedLocations = dict(visitedLocations)
	newVisitedLocations[source.source] = True
	minTraverse = 100000000000000
	
	for destination, dist in source.get_destinations():
		if(destination in newVisitedLocations):
			continue
		minTraverse = min(dist + get_shortest_route_from(dist_map[destination], newVisitedLocations, dist_map), minTraverse)
		
	return minTraverse if minTraverse != 100000000000000 else 0
	
def get_longest_route_from(source, visitedLocations, dist_map):
	newVisitedLocations = dict(visitedLocations)
	newVisitedLocations[source.source] = True
	maxTraverse = 0
	
	for destination, dist in source.get_destinations():
		if(destination in newVisitedLocations):
			continue
		maxTraverse = max(dist + get_longest_route_from(dist_map[destination], newVisitedLocations, dist_map), maxTraverse)
		
	return maxTraverse

def parse_line(line):
	values = line.split(" = ")
	dist = int(values[1])
	first, second = values[0].split(" to ")
	return first,second,dist

def get_shortest_route(input):
	dist_map = {}
	for line in input:
		first,second,dist = parse_line(line)
		if not first in dist_map:
			dist_map[first] = destination(first)
		if not second in dist_map:
			dist_map[second] = destination(second)
		source1 = dist_map[first]
		source1.add_destination(second, dist)
		source2 = dist_map[second]
		source2.add_destination(first, dist)
		
	minTraverse = 100000000000000
	visitedLocations = {}
	for source in dist_map.values():
		minTraverse = min(get_shortest_route_from(dist_map[source.source], visitedLocations, dist_map), minTraverse)
		
	return minTraverse
		
def get_longest_route(input):
	dist_map = {}
	for line in input:
		first,second,dist = parse_line(line)
		if not first in dist_map:
			dist_map[first] = destination(first)
		if not second in dist_map:
			dist_map[second] = destination(second)
		source1 = dist_map[first]
		source1.add_destination(second, dist)
		source2 = dist_map[second]
		source2.add_destination(first, dist)
		
	maxTraverse = 0
	visitedLocations = {}
	for source in dist_map.values():
		maxTraverse = max(get_longest_route_from(dist_map[source.source], visitedLocations, dist_map), maxTraverse)
	print(visitedLocations)
	return maxTraverse		


assert(get_shortest_route(["London to Dublin = 464", "London to Belfast = 518", "Dublin to Belfast = 141"]) == 605)
print("Test passed")

input = Common.inputAsLines()
print(get_shortest_route(input))

assert(get_longest_route([]) == 0)
assert(get_longest_route(["London to Dublin = 464", "London to Belfast = 518", "Dublin to Belfast = 141"]) == 982)
print("second test passed")

print(get_longest_route(input))