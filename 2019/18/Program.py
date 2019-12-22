import networkx as nx
import Common
import string
import itertools


def get_new_pos(old_pos, move_vector):
    return tuple(dim + move for dim, move in zip(old_pos, move_vector))


def is_door(symbol):
    return symbol in string.ascii_uppercase


def is_key(symbol):
    return symbol in string.ascii_lowercase


def get_door(key):
    return key.upper()


def get_key(door):
    return door.lower()


def add_adjacent_connections(pos, tiles, graph):
    for move in directions:
        adjacent_pos = get_new_pos(pos, move)
        if adjacent_pos not in tiles:
            continue

        adjacent = tiles[adjacent_pos]
        current = tiles[pos]

        required_keys = []
        if is_door(adjacent):
            required_keys.append(get_key(adjacent))
        if is_door(current):
            required_keys.append(get_key(current))

        if adjacent != WALL:
            graph.add_edge(pos, adjacent_pos, required_keys=required_keys)


def get_path_length(graph, start_pos, dest_pos, collected_keys):
    return nx.shortest_path_length(graph, start_pos, dest_pos,
                                   weight=lambda u, v, d:
                                   1 if all(required in collected_keys for required in d['required_keys'])
                                   else None)

def get_dist_to_closest_uncollected(graph, all_keys, collected_keys, pos):
    closest_path = 9999999
    uncollected = [key_item for key_item in all_keys.items() if key_item[0] not in collected_keys]
    if len(uncollected) == 0:
        return 0
    for key_sym, key_pos in uncollected:
        try:
            path_length = get_path_length(graph, pos, key_pos, collected_keys)
            closest_path = min(closest_path, path_length)
        except nx.NetworkXNoPath:
            pass
    return closest_path


def get_first_node_to_visit(graph, all_keys, possible_keys, collected_keys, initial_pos):
    assert possible_keys
    if len(possible_keys) == 1:
        return possible_keys[0]
    fully_traversed_keys = collected_keys.copy()

    for key_sym, _ in possible_keys:
        fully_traversed_keys.add(key_sym)

    min_cycle = 9999999
    min_ordering = None

    for key_ordering in itertools.permutations(possible_keys, len(possible_keys)):
        cycle_length = 0
        pos = initial_pos
        for key_sym, key_pos in key_ordering:
            cycle_length += get_path_length(graph, pos, key_pos, fully_traversed_keys)
            pos = key_pos
        cycle_length += get_dist_to_closest_uncollected(graph, all_keys, fully_traversed_keys, pos)

        if cycle_length < min_cycle:
            min_cycle = cycle_length
            min_ordering = key_ordering
    return min_ordering[0]


def get_min_traverse(graph, pos, keys, collected_keys):
    if len(keys) == len(collected_keys):
        return 0
    possibles = []
    for key_item in keys.items():
        key_sym, key_pos = key_item
        if key_sym in collected_keys:
            continue
        try:
            _ = get_path_length(graph, pos, key_pos, collected_keys)
            possibles.append(key_item)
        except nx.NetworkXNoPath:
            pass

    key_sym, key_pos = get_first_node_to_visit(graph, keys, possibles, collected_keys, pos)
    print(key_sym)
    path_length = get_path_length(graph, pos, key_pos, collected_keys)
    collected_keys.add(key_sym)

    return get_min_traverse(graph, key_pos, key_locations, collected_keys) + path_length


NORTH = (0, -1)
SOUTH = (0, 1)
EAST = (1, 0)
WEST = (-1, 0)

directions = [
    NORTH,
    SOUTH,
    WEST,
    EAST
]

WALL = '#'  # impassable
ENTRANCE = '@'  # passable
OPEN = '.'  # passable
# DOOR = uppercase #impassable until removed
# KEY = lowercase #passable

lines = Common.inputAsLines()

tile_map = {}
key_locations = {}
door_locations = {}
map_graph = nx.Graph()
entrance_pos = None

for row, line in enumerate(lines):
    for col, c in enumerate(line):
        curr_pos = (row, col)
        tile_map[curr_pos] = c
        if c == WALL:
            continue
        elif is_key(c):
            key_locations[c] = curr_pos
        elif is_door(c):
            door_locations[c] = curr_pos
        elif c == ENTRANCE:
            entrance_pos = curr_pos
        elif c == OPEN:
            pass
        else:
            assert 0

        map_graph.add_node(curr_pos)

        add_adjacent_connections(curr_pos, tile_map, map_graph)

print(door_locations)

curr_pos = entrance_pos
visited_keys = set()

total = get_min_traverse(map_graph, curr_pos, key_locations, visited_keys)

print(total)
