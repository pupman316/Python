import matplotlib.pyplot as plt
import numpy as np
import sys
import heapq


class Node:
    def __init__(self, designation):
        self.id = designation
        self.adjacent = {}
        # all nodes have initial cost of "infinity"
        self.weight = sys.maxsize
        # all nodes are initially unvisited
        self.visited = False
        # Predecessor
        self.previous = None

    def add_neighbor(self, new_neighbor, cost=0):
        self.adjacent[new_neighbor] = cost

    def get_connections(self):
        return self.adjacent

    def get_weight(self):
        return self.weight

    def set_weight(self, new_weight):
        self.weight = new_weight

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

    def add_node(self, new_node):
        self.num_nodes += 1
        the_node = Node(new_node)
        self.node_dict[new_node] = the_node
        # return the_node

    def get_node(self, node):
        if node in self.node_dict:
            return self.node_dict[node]
        else:
            return None

    def add_edge(self, frm, to, cost=0):
        if frm not in self.node_dict:
            self.add_node(frm)
        if to not in self.node_dict:
            self.add_node(to)
        self.node_dict[frm].add_neighbor(self.node_dict[to], cost)
        self.node_dict[to].add_neighbor(self.node_dict[frm], cost)

    def get_nodes(self):
        return self.node_dict

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
