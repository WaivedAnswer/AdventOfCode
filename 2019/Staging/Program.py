import networkx as nx
import Common
import string


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


def get_min_traverse(pos, keys, collected_keys):
    if len(keys) == len(collected_keys):
        return 0
    possibles = []
    for key_item in keys.items():
        key_sym, key_pos = key_item
        if key_sym in collected_keys:
            continue
        try:
            path_length = get_path_length(map_graph, pos, key_pos, collected_keys)
            possibles.append((key_item, path_length))
        except nx.NetworkXNoPath:
            pass
    total_possible_steps = []

    for possible_key, path_length in possibles:
        key_sym, key_pos = possible_key
        if len(possibles) == 1:
            collected_copy = collected_keys
        else:
            collected_copy = collected_keys.copy()

        collected_copy.add(key_sym)
        total_steps = get_min_traverse(key_pos, key_locations, collected_copy) + path_length
        total_possible_steps.append(total_steps)

    return min(total_possible_steps)


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

total = get_min_traverse(curr_pos, key_locations, visited_keys)

print(total)
