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
        closest_coords = bounds.get_closest_coords_to(self.coordinates)
        return self.is_within_range(closest_coords)

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
        min_coords = self.get_closest_coords_to(origin)
        return get_manhattan_dist(min_coords, origin)

    def get_closest_coords_to(self, coordinates):
        closest_coords = []
        for coord, bound in zip(coordinates, self.bounds):
            if bound[0] <= coord <= bound[1]:
                closest_coords.append(coord)
            else:
                closest_coords.append(min(bound, key=lambda end_point: abs(coord - end_point)))
        return tuple(closest_coords)

    def __str__(self):
        return str(self.bounds)

    def subdivided(self):
        subdivided_bounds = []
        bound_lengths = [int((bound[1] - bound[0])) for bound in self.bounds]
        if all([length <= 2 for length in bound_lengths]):
            return None

        new_bound_options = [[(bound[0], int(statistics.mean(bound))), (int(statistics.mean(bound)) + 1, bound[1])] for
                             bound in self.bounds]
        sub_bound_perms = itertools.product(*new_bound_options)

        for new_bounds in sub_bound_perms:
            subdivided_bound = Bounds(new_bounds, self.dimensions)
            subdivided_bounds.append(subdivided_bound)
        return subdivided_bounds

    def get_nano_count(self, nanobots):
        if self.nano_count is not None:
            return self.nano_count
        self.nano_count = sum([1 for nanobot in nanobots if nanobot.overlaps_bounds(self)])

        return self.nano_count

    def get_best_coord_within(self, nanobots, origin):
        min_index = 0
        max_index = 1

        max_coord = None
        min_dist = 999999999999
        max_count = len(nanobots)
        ranges = [list(range(bound[min_index], bound[max_index] + 1)) for bound in self.bounds]
        bounds_iterator = itertools.product(*ranges)
        for coord in bounds_iterator:
            nano_count = get_nano_count_coord(nanobots, coord)
            if nano_count < max_count:
                continue
            dist = get_manhattan_dist(coord, origin)
            if dist < min_dist:
                min_dist = dist
                max_coord = coord
        return max_coord


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
                return None
            eligible_sub_bounds.sort(key=lambda bound: bound.get_min_manhattan_dist_to_origin(self.origin))
            for sub_bound in eligible_sub_bounds:
                best_coord = self.get_best_coord_within_bounds(sub_bound)
                if best_coord is not None:
                    return best_coord
            return None

    def get_best_coord(self):
        max_bounds = Bounds([(self.get_coord_min(dim), self.get_coord_max(dim)) for dim in range(self.dimensions)],
                            self.dimensions)
        return self.get_best_coord_within_bounds(max_bounds)


def part2(lines):
    nanobots = []
    for line in lines:
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


input_lines = Common.inputAsLines()
print(part2(input_lines))
