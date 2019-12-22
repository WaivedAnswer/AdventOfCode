import networkx as nx
import Common
import string
from collections import defaultdict


def get_new_pos(old_pos, move_vector):
    return tuple(dim + move for dim, move in zip(old_pos, move_vector))


def is_label(symbol):
    return symbol in string.ascii_uppercase


def add_adjacent_connections(pos, tiles, graph):
    for move in directions:
        adjacent_pos = get_new_pos(pos, move)
        if adjacent_pos not in tiles:
            continue

        adjacent = tiles[adjacent_pos]

        if adjacent == OPEN:
            graph.add_edge(pos, adjacent_pos)


def create_label_map(labels, tiles):
    full_label_map = defaultdict(list)

    opposite_directions = {
        NORTH : SOUTH,
        SOUTH : NORTH,
        EAST : WEST,
        WEST : EAST
    }

    for label_pos, label_sym in labels.items():
        for move in directions:
            adjacent_pos = get_new_pos(label_pos, move)
            if adjacent_pos not in tiles:
                continue

            adjacent = tiles[adjacent_pos]

            if adjacent == OPEN:
                label_adjacent = adjacent_pos
                opposite_pos = get_new_pos(label_pos, opposite_directions[move])
                opposite_sym = tiles[opposite_pos]
                if move == EAST or move == SOUTH:
                    full_label = opposite_sym + label_sym
                else:
                    full_label = label_sym + opposite_sym

                full_label_map[full_label].append(label_adjacent)

    return full_label_map


def add_portal_connections(full_labels, graph):
    for full_label, portals in full_labels.items():
        if len(portals) == 1:
            continue
        elif len(portals) == 2:
            graph.add_edge(portals[0], portals[1])
        else:
            assert 0


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
OPEN = '.'  # passable
# LABEL = uppercase #impassable until removed

lines = Common.inputAsLines()

tile_map = {}
label_locations = {}
map_graph = nx.Graph()
entrance_pos = None
exit_pos = None

for row, line in enumerate(lines):
    for col, c in enumerate(line):
        curr_pos = (row, col)
        tile_map[curr_pos] = c
        if c == WALL:
            continue
        elif is_label(c):
            label_locations[curr_pos] = c
        elif c == OPEN:
            pass
        elif c == " ":
            continue
        else:
            print(c)
            assert 0

        map_graph.add_node(curr_pos)

        add_adjacent_connections(curr_pos, tile_map, map_graph)

label_map = create_label_map(label_locations, tile_map)
add_portal_connections(label_map, map_graph)

start_pos = label_map["AA"][0]
end_pos = label_map["ZZ"][0]

print(nx.shortest_path_length(map_graph, start_pos, end_pos))
