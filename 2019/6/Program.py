import Common
import networkx as nx

input_lines = Common.inputAsLines()
orbit_graph = nx.Graph()

orbiting_items = []

for line in input_lines:
    stationary, orbiting = line.split(")")
    orbiting_items.append(orbiting)
    orbit_graph.add_node(stationary)
    orbit_graph.add_node(orbiting)
    orbit_graph.add_edge(orbiting, stationary)

print(sum(nx.shortest_path_length(orbit_graph, orbiting, "COM") for orbiting in orbiting_items))
print(nx.shortest_path_length(orbit_graph, "YOU", "SAN") - 2)