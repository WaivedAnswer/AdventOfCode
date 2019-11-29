import Common
import networkx as nx
import itertools
import statistics


def get_manhattan_dist(coord1, coord2):
	return sum([abs(dim1 - dim2) for dim1, dim2 in zip(coord1, coord2)])


def get_nano_count_coord(nanobots, coord):
	return sum([1 for nanobot in nanobots if nanobot.is_within_range(coord)])


class Nanobot:
	def __init__(self, coordinates, radius):
		self.coordinates = coordinates
		self.radius = radius

	def overlaps_other(self, other_nano):
		return get_manhattan_dist(self.coordinates, other_nano.coordinates) <= self.radius + other_nano.radius

	def overlaps_bounds(self, bounds):
		dist = 0
		for coord, bound in zip(self.coordinates, bounds):
			if bound[0] <= coord <= bound[1]:
				dist += 0
			else:
				min_dist_to_bound = min([abs(coord - bound[0]), abs(coord - bound[1])])
				dist += min_dist_to_bound
		return dist <= self.radius

	def is_within_range(self, coordinates):
		return get_manhattan_dist(self.coordinates, coordinates) <= self.radius

	def get_min(self, dim):
		return self.coordinates[dim] - self.radius

	def get_max(self, dim):
		return self.coordinates[dim] + self.radius


class Bounds:
	def __init__(self, bounds, dimensions):
		self.bounds = bounds
		self.nano_count = None
		self.dimensions = dimensions

	def get_min_manhattan_dist_to_origin(self, origin):
		min_coords = [min(abs(bound[0]), abs(bound[1])) for bound in self.bounds]
		return get_manhattan_dist(min_coords, origin)

	def __str__(self):
		return str(self.bounds)

	def subdivided(self):
		subdivided_bounds = []
		bound_lengths = [int((bound[1] - bound[0])) for bound in self.bounds]
		if all([length <= 2 for length in bound_lengths]):
			return None

		new_bound_options = [[(bound[0], int(statistics.mean(bound))), (int(statistics.mean(bound)) + 1, bound[1])] for bound in self.bounds]
		sub_bound_perms = itertools.product(*new_bound_options)

		for new_bounds in sub_bound_perms:
			subdivided_bound = Bounds(new_bounds, self.dimensions)
			subdivided_bounds.append(subdivided_bound)
		return subdivided_bounds

	def get_nano_count(self, nanobots):
		if self.nano_count is not None:
			return self.nano_count
		self.nano_count = sum([1 for nanobot in nanobots if nanobot.overlaps_bounds(self.bounds)])

		return self.nano_count

	def get_best_coord_within(self, nanobots, origin):
		min_index = 0
		max_index = 1

		max_coord = None
		min_dist = 999999999999
		max_count = len(nanobots)
		ranges = [list(range(bound[min_index], bound[max_index] + 1)) for bound in self.bounds]
		bounds_iterator = itertools.product(*ranges)
		print(self.bounds)
		for coord in bounds_iterator:
			nano_count = get_nano_count_coord(nanobots, coord)
			if nano_count < max_count:
				continue
			dist = get_manhattan_dist(coord, origin)
			if dist < min_dist or nano_count > max_count:
				min_dist = dist
				max_count = nano_count
				max_coord = coord
		return max_coord


def getCoordMin(nanobots, dim):
	return min(nanobots, key=lambda bot: bot.coordinates[dim]).coordinates[dim]


def getCoordMax(nanobots, dim):
	return max(nanobots, key=lambda bot: bot.coordinates[dim]).coordinates[dim]


class OverlappingNanoSystem:
	def __init__(self, nanobots, dimensions, origin):
		self.nanobots = nanobots
		self.nano_count = len(self.nanobots)
		self.dimensions = dimensions
		self.origin = origin

	def get_coord_min(self, dim):
		min_vals = [bot.get_min(dim) for bot in self.nanobots]
		return max(min_vals)

	def get_coord_max(self, dim):
		max_vals = [bot.get_max(dim) for bot in self.nanobots]
		return max(max_vals)

	def filter_max_bounds(self, bounds_list):
		bound_counts = [(bound.get_nano_count(self.nanobots), bound) for bound in bounds_list]
		return [sub_bound for count, sub_bound in bound_counts if
				count == self.nano_count]

	def get_best_coord_within_bounds(self, bounds):
		divided_bounds = bounds.subdivided()
		if not divided_bounds:
			return bounds.get_best_coord_within(self.nanobots, self.origin)
		else:
			eligible_sub_bounds = self.filter_max_bounds(divided_bounds)
			if len(eligible_sub_bounds) == 0:
				print("No eligible sub_bounds")
				return bounds.get_best_coord_within(self.nanobots, self.origin)
			min_bound = min(eligible_sub_bounds, key=lambda bound: bound.get_min_manhattan_dist_to_origin(self.origin))
			return self.get_best_coord_within_bounds(min_bound)

	def get_best_coord(self):
		max_bounds = Bounds([(self.get_coord_min(dim), self.get_coord_max(dim)) for dim in range(self.dimensions)],
							self.dimensions)
		return self.get_best_coord_within_bounds(max_bounds)


def part2(input):
	nanobots = []
	for line in input:
		numbers = Common.numbers(line)
		nanobots.append(Nanobot(tuple(numbers[:3]), numbers[3]))

	overlap_graph = nx.Graph()
	for idx, nano in enumerate(nanobots):
		overlap_graph.add_node(idx)
		for other_idx, other_nano in enumerate(nanobots):
			if idx == other_idx or nano.overlaps_other(other_nano):
				overlap_graph.add_edge(idx, other_idx)
	best_overlapping_nanos_indices = max(nx.find_cliques(overlap_graph), key=lambda clique: len(clique))

	best_overlapping_nanos = [nanobots[idx] for idx in best_overlapping_nanos_indices]
	origin = (0, 0, 0)
	overlapping_system = OverlappingNanoSystem(best_overlapping_nanos, 3, origin)
	best_coord = overlapping_system.get_best_coord()
	print(best_coord)
	return sum(best_coord)

#Nearest the big bot: 613
#The max count I found was: 981
#Best location value: 101599540
input = Common.inputAsLines()
print(part2(input))
