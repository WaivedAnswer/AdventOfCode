class Coords:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def left(self):
        return Coords(self.x - 1, self.y)

    def right(self):
        return Coords(self.x + 1, self.y)

    def up(self):
        return Coords(self.x, self.y - 1)

    def down(self):
        return Coords(self.x, self.y + 1)

    def __eq__(self, other):
        if isinstance(other, Coords):
            return self.x == other.x and self.y == other.y
        return NotImplemented

    def __hash__(self):
        return hash(tuple(sorted(self.__dict__.items())))


class TerrainNode:
    def __init__(self):
        self.erosion = None
        self.geo_index = None
        self.terrain = None


class CoordMap:
    def __init__(self, size):
        self.items = [None for i in range(size * size)]
        self.size = size

    def _get_index(self, coord):
        return coord.x * self.size + coord.y

    def has_item(self, coord):
        return self.get(coord) is not None

    def set(self, coord, item):
        self.items[self._get_index(coord)] = item

    def get(self, coord):
        return self.items[self._get_index(coord)]


origin = Coords(0, 0)


class CaveSystem:
    def __init__(self, target, depth):
        self.target = target
        self.depth = depth
        size = max(target.x, target.y) + 1

        self.erosion_map = CoordMap(size)

    def geological_index(self, coords: Coords):
        if coords == self.target or coords == origin:
            return 0
        elif coords.x == 0:
            geo_index = coords.y * 48271
        elif coords.y == 0:
            geo_index = coords.x * 16807
        else:
            geo_index = self.erosion(coords.left()) * self.erosion(coords.up())

        return geo_index

    def erosion(self, coords: Coords):
        if self.erosion_map.has_item(coords):
            return self.erosion_map.get(coords).erosion

        erosion_val = (self.geological_index(coords) + self.depth) % 20183
        node = TerrainNode()
        node.erosion = erosion_val
        self.erosion_map.set(coords, node)
        return erosion_val

    def terrain(self, coords: Coords):
        val = self.erosion(coords) % 3
        return val

    @staticmethod
    def get_terrain_symbol(terrain_val):
        if terrain_val == 0:
            return "."
        elif terrain_val == 1:
            return "="
        elif terrain_val == 2:
            return "|"
        else:
            assert 0

    def get_total_risk(self):
        risk_sum = 0
        for y in range(origin.y, self.target.y + 1):
            for x in range(origin.x, self.target.x + 1):
                coords = Coords(x, y)
                terrain_val = self.terrain(coords)
                risk_sum += terrain_val
        return risk_sum


real_target = Coords(9, 739)
real_depth = 10914
cave = CaveSystem(real_target, real_depth)
print(cave.get_total_risk())
