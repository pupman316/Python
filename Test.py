# import plotly.plotly as plotLib
# import plotly.graph_objs as graphLib
from ShortestPath import Graph
from ShortestPath import Node
# from ShortestPath import dijkstra
# from ShortestPath import shortest

# from DijkstraK import dijkstra
# from DijkstraK import Graph

import matplotlib.pyplot as plt
import numpy as np

#plt.interactive(False)  # Recommended from Stack Exchange

#testing for another day!!!
# print("Hello World", "\n")
#
# # Random number generation is handled here
# N = 50
# x = np.linspace(0.0, 1.0, N)
# y = np.random.randn(N)
#
# colors = np.random.rand(N)
# area = np.pi * (15 * np.random.rand(N))**2  # 0 to 15 point radii
#
# plt.scatter(x, y, s=area, c=colors, alpha=0.5)
# plt.show()
#
# # # Create random data with numpy
# # N = 500
# # random_x = np.linspace(0, 1, N)
# # random_y = np.random.randn(N)
# #
# # # Create a trace
# # trace = graphLib.Scatter(
# #     x = random_x,
# #     y = random_y
# # )
# #
# # data = [trace]
# #
# # plotLib.iplot(data, filename='basic')
#
#
#
#
#
#
# # test = [1, 2, 3, 4, 5]
# # for x in test:
# #     print(x)
#
# print("\n", "Goodbye World!")

print("SHORTEST PATH! Oh Yeah!\n")

g = Graph()

g.add_node("a")
g.add_node("b")
g.add_node("c")
g.add_node("d")
g.add_node("e")
g.add_node("f")

g.add_edge('a', 'b', 7)
g.add_edge('a', 'c', 9)
g.add_edge('a', 'f', 14)
g.add_edge('b', 'c', 10)
g.add_edge('b', 'd', 15)
g.add_edge('c', 'd', 11)
g.add_edge('c', 'f', 2)
g.add_edge('d', 'e', 6)
g.add_edge('e', 'f', 9)

print("Graph data:")
# print(str(g.get_node("b").get_connections()))  # Testing

print(str(g.get_nodes().id))

# for n in g.node_dict:
#     print(str(n.get_connections()))
    # for w in n.get_connections():
    #     print("Found it! \" Test \"")

# print(str(g.get_node("a")))
# print(str(g.get_node("c")))


# g = Graph()
#

#
# print("Graph data:")
# for v in g.vert_dict.items():
#     for w in v.get_connections():
#         vid = v.get_id()
#         wid = w.get_id()
#         print('( %s , %s, %3d)') % (vid, wid, v.get_weight(w))
#
# dijkstra(g, g.get_vertex('a'), g.get_vertex('e'))
#
# target = g.get_vertex('e')
# path = [target.get_id()]
# shortest(target, path)
# print('The shortest path : %s') % (path[::-1])
