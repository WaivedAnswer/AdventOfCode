import Common
from collections import defaultdict


def get_manhattan_dist(coord):
    return sum(abs(dim) for dim in coord)


line_input = Common.inputAsLines()

up = (0, -1)
down = (0, 1)
left = (-1, 0)
right = (1, 0)

wire_map = defaultdict(lambda: defaultdict(int))
wire_id = 0
for line in line_input:
    curr_pos = (0, 0)
    wire_instructions = line.split(",")
    path_length = 0
    for instruction in wire_instructions:
        dist = int(instruction[1:])
        if instruction[0] == "U":
            direction = up
        elif instruction[0] == "D":
            direction = down
        elif instruction[0] == "L":
            direction = left
        elif instruction[0] == "R":
            direction = right
        for i in range(1, dist + 1):
            curr_pos = (curr_pos[0] + direction[0], curr_pos[1] + direction[1])
            path_length += 1
            if curr_pos in wire_map and wire_id in wire_map[curr_pos]:
                wire_map[curr_pos][wire_id] = min(wire_map[curr_pos][wire_id], path_length)
            else:
                wire_map[curr_pos][wire_id] = path_length

    wire_id += 1

overlaps = [coord for coord, overlap_set in wire_map.items() if len(overlap_set) >= 2]
print("Part 1:", get_manhattan_dist(min(overlaps, key=lambda coord: get_manhattan_dist(coord))))

dists = [sum(wire_map[coord].values()) for coord in overlaps]
print("Part 2:", min(dists))


