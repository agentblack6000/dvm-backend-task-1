"""
Creates a map (plots a graph with edges and nodes) using the networkx and matplotlib libraries
"""
import networkx as nx
import matplotlib.pyplot as plt
from railway_network import undergound_network

# Create an empty graph
def map_maker():
    the_underground_map = nx.MultiGraph()

    for line in undergound_network.lines:
        the_underground_map.add_edges_from(line.get_connections())

    pos = nx.spring_layout(the_underground_map)

    plt.figure(figsize=(8, 8))
    connections = undergound_network.graph_connections()

    nx.draw_networkx_nodes(the_underground_map, pos, node_color='skyblue', node_size=3000)

    weight = 5
    for line in undergound_network.lines:
        nx.draw_networkx_edges(the_underground_map, pos, edgelist=line.get_connections(), edge_color=line.color, width=weight)
        weight+=1

    nx.draw(the_underground_map, pos, with_labels=True, node_color='skyblue', font_color="black", font_size=16)
    plt.show()
