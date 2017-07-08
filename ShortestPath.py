import matplotlib.pyplot as plt
import numpy as np
import sys
import heapq


class Node:
    def __init__(self, designation):
        self.id = designation
        self.adjacent = {}
        # all nodes have initial cost of "infinity"
        self.cost = sys.maxsize
        # all nodes are initially unvisited
        self.visited = False
        # Predecessor
        self.previous = None

    def add_neighbor(self, new_neighbor, cost=0):
        self.adjacent[new_neighbor] = cost

    def get_connections(self):
        return self.adjacent

    def get_cost(self):
        return self.cost

    def set_cost(self, new_cost):
        self.cost = new_cost

    def set_previous(self, prev):
        self.previous = prev

    def set_visited(self):
        self.visited = True

    def __str__(self):
        return str(self.id) + " is adjacent to " + str([x for x in self.adjacent])  # Must revisit the concept of "id" or "key" attribute


class Graph:
    def __init__(self):
        self.node_dict = {}
        self.num_nodes = 0

    def __iter__(self):
        return iter(self.node_dict)

# class Graph:
#     def __iter__(self):
#         return iter(self.vert_dict.items())
#
#     def add_vertex(self, node):
#         self.num_vertices += 1
#         new_vertex = Vertex(node)
#         self.vert_dict[node] = new_vertex
#         return new_vertex
#
#     def get_vertex(self, n):
#         if n in self.vert_dict:
#             return self.vert_dict[n]
#         else:
#             return None
#
#     def add_edge(self, frm, to, cost=0):
#         if frm not in self.vert_dict:
#             self.add_vertex(frm)
#         if to not in self.vert_dict:
#             self.add_vertex(to)
#
#         self.vert_dict[frm].add_neighbor(self.vert_dict[to], cost)
#         self.vert_dict[to].add_neighbor(self.vert_dict[frm], cost)
#
#     def get_vertices(self):
#         return self.vert_dict.items()
#
#
# def shortest(v, path):
#     ''' make shortest path from v.previous '''
#     if v.previous:
#         path.append(v.previous.get_id())
#         shortest(v.previous, path)
#     return
#
#
# def dijkstra(agraph, start, target):
#     print("Dijkstra's shortest path")
#     # Set the distance for the start node to zero
#     start.set_distance(0)
#
#     # Put tuple pair into priority queue
#     unvisited_queue = [(v.get_distance(), v) for v in agraph.get_vertices()]
#     heapq.heapify(unvisited_queue)
#
#     while len(unvisited_queue):
#         # Pops a vertex with the smallest distance
#         uv = heapq.heappop(unvisited_queue)
#         current = uv[1]
#         current.set_visited()
#
#         # For next in v.adjacent
#         for next in current.adjacent:
#             # if visited, skip
#             if next.visited:
#                 continue
#             new_dist = current.get_distance() + current.get_weight(next)
#
#             if new_dist < next.get_distance():
#                 next.set_distance(new_dist)
#                 next.set_previous(current)
#                 print('Updated : current = %s next = %s new_dist = %s') \
#                     % (current.get_id(), next.get_id(), next.get_distance())
#
#             else:
#                 print('Not updated: current = %s next = %s new_dist = %s') \
#                     % (current.get_id(), next.get_id(), next.get_distance())
#
#         # Rebuild heap
#         # 1. Pop every item
#         while len(unvisited_queue):
#             heapq.heappop(unvisited_queue)
#         # 2. Put all vertices not visited into the queue
#         unvisited_queue = [(v.get_distance(), v) for v in agraph if not v.visited]
#         heapq.heapify(unvisited_queue)
