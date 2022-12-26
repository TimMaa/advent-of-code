import re
import sys

class Graph:
  def __init__(self):
    self.graph = dict()
    self.nodes = dict()

  def add(self, room, node, flowrate):
    if not self.graph.get(room):
      self.graph[room] = []
      if flowrate > 0:
        self.nodes[room] = flowrate
    self.graph[room].append(node)

  def djikstra(self, start):
    unvisited_nodes = list(self.graph.keys())
    # We'll use this dict to save the cost of visiting each node and update it as we move along the graph
    shortest_path = {}
    # We'll use this dict to save the shortest known path to a node found so far
    previous_nodes = {}

    # We'll use max_value to initialize the "infinity" value of the unvisited nodes
    for node in unvisited_nodes:
      shortest_path[node] = sys.maxsize
    shortest_path[start] = 0

    while unvisited_nodes:
      # The code block below finds the node with the lowest score
      current_min_node = None
      for node in unvisited_nodes: # Iterate over the nodes
        if current_min_node == None:
          current_min_node = node
        elif shortest_path[node] < shortest_path[current_min_node]:
          current_min_node = node

      # The code block below retrieves the current node's neighbors and updates their distances
      neighbors = graph.graph[current_min_node]
      for neighbor in neighbors:
        tentative_value = shortest_path[current_min_node] + 1
        if tentative_value < shortest_path[neighbor]:
          shortest_path[neighbor] = tentative_value
          # We also update the best path to the current node
          previous_nodes[neighbor] = current_min_node

      # After visiting its neighbors, we mark the node as "visited"
      unvisited_nodes.remove(current_min_node)

    return shortest_path

  def find_best_path(self, time, start, unvisited_nodes: set):
    time -= 1

    if start in unvisited_nodes:
      unvisited_nodes.remove(start)
    if len(unvisited_nodes) == 0 or time <= 0:
      return (0, [start])

    paths = self.djikstra(start)
    weighted_paths = dict((k,(time-v)*self.nodes.get(k)) for k,v in paths.items() if k in unvisited_nodes and v > 0)
    path_values = []

    for node, val in weighted_paths.items():
      path_value, path = self.find_best_path(time-paths[node], node, unvisited_nodes.copy())
      path_values.append((val + path_value, [start] + path))

    return max(path_values)

graph = Graph()
time = 30
location = "AA"
release = 0

with open("./input.txt", "r") as input:
  for line in input:
    flowrate = int(re.findall("\d+", line)[0])
    nodes = re.findall("[A-Z]{2}", line)
    room = nodes.pop(0)

    for node in nodes:
      graph.add(room, node, flowrate)

print(graph.find_best_path(time, location, set(graph.nodes.keys())))