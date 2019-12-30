import time
import networkx as nx

class Path:
    def __init__(self):
        self.path = None

    def has_path(self):
        return self.path is not None

    def set_path(self, path):
        self.path = path


moves = [
    (-2, 1),
    (-2, -1),
    (2, 1),
    (2, -1),
    (1, -2),
    (-1, -2),
    (1, 2),
    (-1, 2)
]


def get_new_pos(old_pos, move_vector):
    return tuple(dim + vec for dim, vec in zip(old_pos, move_vector))


def traverse(seen, curr_pos, adjacent_map):
    if full_path.has_path():
        return
    seen.append(curr_pos)
    path_length = len(seen)
    if path_length == full_length:
        full_path.set_path(seen)
        return

    if curr_pos in adjacent_map:
        adjacents = adjacent_map[curr_pos]
    else:
        adjacents = []
        for move in moves:
            adjacent = get_new_pos(curr_pos, move)
            if adjacent not in all_positions:
                continue
            adjacents.append(adjacent)

        adjacent_map[curr_pos] = adjacents

    for move_pos in adjacents:
        if move_pos in seen or (move_pos == max_possible and path_length + 1 != full_length):
            continue

        traverse(seen[:], move_pos, adjacent_map)

        if full_path.has_path():
            break

def traverse_2(all_positions, start_pos, final_pos):
    chess_graph = nx.Graph()
    for pos in all_positions:
        chess_graph.add_node(pos)
        adjacents = []
        for move in moves:
            adjacent = get_new_pos(pos, move)
            if adjacent not in all_positions:
                continue
            adjacents.append(adjacent)
        for adjacent in adjacents:
            chess_graph.add_edge(pos, adjacent)




all_positions = set()
for i in range(6):
    for j in range(6):
        all_positions.add((i, j))

max_possible = max(all_positions)
full_length = len(all_positions)

initial_pos = (0, 0)

cached_adjacents = {}
start = time.time()
full_path = Path()
traverse([], initial_pos, cached_adjacents)
end = time.time()

print(end - start)

minX = min(all_positions, key=lambda coord: coord[0])[0]
maxX = max(all_positions, key=lambda coord: coord[0])[0]
minY = min(all_positions, key=lambda coord: coord[1])[1]
maxY = max(all_positions, key=lambda coord: coord[1])[1]

board_string = ""
for idx, _ in enumerate(full_path.path):
    board_string += (str(idx) + '\n')
    path_slice = full_path.path[:idx + 1]
    for row in range(minY, maxY + 1):
        for col in range(minX, maxX + 1):
            if (col, row) not in path_slice:
                board_string += "."
            else:
                board_string += "X"
        board_string += "\n"
print(board_string)


