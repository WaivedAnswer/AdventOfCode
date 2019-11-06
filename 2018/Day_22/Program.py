class Coords:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def left(self):
        return Coords(self.x - 1, self.y)

    def up(self):
        return Coords(self.x, self.y - 1)

    def __eq__(self, other):
        if isinstance(other, Coords):
            return self.x == other.x and self.y == other.y
        return NotImplemented

    def __hash__(self):
        return hash(tuple(sorted(self.__dict__.items())))


cave_depth = 10914
target_coords = Coords(9, 739)
origin = Coords(0, 0)
erosion_map = {}


def geological_index(coords: Coords):
    if coords == target_coords or coords == origin:
        return 0
    elif coords.x == 0:
        geo_index = coords.y * 48271
    elif coords.y == 0:
        geo_index = coords.x * 16807
    else:
        geo_index = erosion(coords.left()) * erosion(coords.up())

    return geo_index


def erosion(coords: Coords):
    if coords in erosion_map:
        return erosion_map[coords]

    erosion_val = geological_index(coords) + cave_depth % 20183
    erosion_map[coords] = erosion_val
    return erosion_val


def terrain(coords: Coords):
    val = erosion(coords) % 3
    return val


def get_total_risk():
    risk_sum = 0
    for y in range(origin.y, target_coords.y):
        terrain_line = ""
        for x in range(origin.x, target_coords.x):
            coords = Coords(x, y)
            terrain_val = terrain(coords)
            terrain_line += str(terrain_val)
            risk_sum += terrain_val
        print(terrain_line)
    return risk_sum


print(get_total_risk())
