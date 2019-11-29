import networkx


class Coords:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return "(" + str(self.x) + "," + str(self.y) + ")"

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
        return hash((self.x, self.y))


class CoordMap:
    def __init__(self):
        self.items = {}

    @staticmethod
    def valid_coords(coord):
        return coord.x >= 0 and coord.y >= 0

    def has_item(self, coord):
        return coord in self.items

    def set(self, coord, item):
        self.items[coord] = item

    def get(self, coord):
        return self.items[coord]


origin = Coords(0, 0)

TOOL_NEITHER = 0
TOOL_TORCH = 1
TOOL_CLIMBING_GEAR = 2

TERRAIN_ROCKY = 0
TERRAIN_WET = 1
TERRAIN_NARROW = 2

allowed_tools = {
    TERRAIN_ROCKY: [TOOL_TORCH, TOOL_CLIMBING_GEAR],
    TERRAIN_WET: [TOOL_NEITHER, TOOL_CLIMBING_GEAR],
    TERRAIN_NARROW: [TOOL_NEITHER, TOOL_TORCH]
}

allowed_terrain = {
    TOOL_TORCH: [TERRAIN_ROCKY, TERRAIN_NARROW],
    TOOL_NEITHER: [TERRAIN_NARROW, TERRAIN_WET],
    TOOL_CLIMBING_GEAR: [TERRAIN_ROCKY, TERRAIN_WET]
}


class State:
    def __init__(self, coords, tool, time, cave_system):
        self.coords = coords
        self.tool = tool
        self.time = time
        self.cave_system = cave_system

    def get_terrain(self):
        return self.cave_system.terrain(self.coords)

    def is_valid(self):
        return self.tool in allowed_tools[self.get_terrain()]

    def switch_tool(self):
        tools = allowed_tools[self.get_terrain()]
        for tool in tools:
            if self.tool != tool:
                new_tool = tool
        return State(self.coords, new_tool, self.time + 7, self.cave_system)

    def move_up(self):
        return State(self.coords.up(), self.tool, self.time + 1, self.cave_system)

    def move_down(self):
        return State(self.coords.down(), self.tool, self.time + 1, self.cave_system)

    def move_right(self):
        return State(self.coords.right(), self.tool, self.time + 1, self.cave_system)

    def move_left(self):
        return State(self.coords.left(), self.tool, self.time + 1, self.cave_system)


def are_coords_valid(coords):
    return coords.x >= 0 and coords.y >= 0


class CaveSystem:
    def __init__(self, target, depth):
        self.target = target
        self.depth = depth
        self.terrain_map = CoordMap()
        self.generate_terrains()

    def geological_index(self, coords: Coords):
        assert(self.terrain_map.has_item(coords))
        return self.terrain_map.get(coords)[0]

    def erosion(self, coords: Coords):
        assert(self.terrain_map.has_item(coords))
        return self.terrain_map.get(coords)[1]

    def terrain(self, coords: Coords):
        assert(self.terrain_map.has_item(coords))
        return self.terrain_map.get(coords)[2]

    def get_total_risk(self):
        risk_sum = 0
        for y in range(origin.y, self.target.y + 1):
            for x in range(origin.x, self.target.x + 1):
                coords = Coords(x, y)
                terrain_val = self.terrain(coords)
                risk_sum += terrain_val
        return risk_sum

    def shortest_path_to_target(self):
        terrain_graph = networkx.Graph()
        for y in range(origin.y, self.target.y + 100):
            for x in range(origin.x, self.target.x + 100):
                coords = Coords(x, y)
                connected_coords = [coords.up(), coords.left()]

                terrain_val = self.terrain(coords)
                tools = allowed_tools[terrain_val]
                for tool in tools:
                    node = (coords, tool)
                    terrain_graph.add_node(node)
                    for connected in connected_coords:
                        if not are_coords_valid(connected):
                            continue
                        connected_terrain = self.terrain(connected)
                        if tool in allowed_tools[connected_terrain]:
                            connected_node = (connected, tool)
                            terrain_graph.add_edge(connected_node, node, weight=1)

                terrain_graph.add_edge((coords, tools[0]), (coords, tools[1]), weight=7)

        return networkx.dijkstra_path_length(terrain_graph, (origin, TOOL_TORCH), (self.target, TOOL_TORCH))

    def generate_terrains(self):
        for y in range(origin.y, self.target.y + 100):
            for x in range(origin.x, self.target.x + 100):
                coords = Coords(x, y)

                if coords == self.target or coords == origin:
                    geo_index = 0
                elif coords.x == 0:
                    geo_index = coords.y * 48271
                elif coords.y == 0:
                    geo_index = coords.x * 16807
                else:
                    geo_index = self.terrain_map.get(coords.left())[1] * self.terrain_map.get(coords.up())[1]

                erosion = (geo_index + self.depth) % 20183
                terrain = erosion % 3

                self.terrain_map.set(coords, (geo_index, erosion, terrain))


real_target = Coords(9, 739)
real_depth = 10914
cave = CaveSystem(real_target, real_depth)
print(cave.get_total_risk())

subject = CaveSystem(real_target, real_depth)
print(subject.shortest_path_to_target())

