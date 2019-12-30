import Common
import copy

def get_new_pos(old_pos, move_vector):
  return tuple(dim + move for dim, move in zip(old_pos, move_vector))

def calc_biodiversity_point(coord, tile_val, row_size):
    if tile_val != BUG:
        return 0
    column, rw = coord
    return pow(2, rw * row_size + column)


def calc_total_biodiversity(tile_map, row_size):
    return sum(calc_biodiversity_point(val[0], val[1], row_size) for val in tile_map.items())

def get_morphed_value(coord, tile_map):
    adjacent_bug_count = 0
    for move in directions:
        adjacent_pos = get_new_pos(coord, move)
        if adjacent_pos not in tile_map:
            continue
        adjacent = tile_map[adjacent_pos]
        if adjacent == BUG:
            adjacent_bug_count += 1
    current = tile_map[coord]
    if current == BUG and adjacent_bug_count == 1:
        return BUG
    elif current == OPEN and adjacent_bug_count in set([1,2]):
        return BUG
    else:
        return OPEN





NORTH = ( 0, -1)
SOUTH = ( 0,  1)
EAST =  ( 1,  0)
WEST =  (-1,  0)

directions = [
  NORTH,
  SOUTH,
  WEST,
  EAST
]


OPEN = '.'
BUG = '#'

lines = Common.inputAsLines()
bug_map = {}
width = 0

for row, line in enumerate(lines):
    for col, tile in enumerate(line):
        bug_map[(col, row)] = tile

maxX, maxY = max(bug_map)
print(maxX, maxY)
width = maxX + 1
height = maxY + 1

biodiversities = set()
while True:
    changed_tiles = {}
    for bug_coord in bug_map:
        curr_value = bug_map[bug_coord]
        morphed_value = get_morphed_value(bug_coord, bug_map)
        if curr_value != morphed_value:
            changed_tiles[bug_coord] = morphed_value
    for morphed_coord, morphed_value in changed_tiles.items():
        bug_map[morphed_coord] = morphed_value
    curr_biodiversity = calc_total_biodiversity(bug_map, width)
    if curr_biodiversity in biodiversities:
        print(curr_biodiversity)
        break
    biodiversities.add(curr_biodiversity)


