import sys

grid: list[list] = list()

class Graph:
  def __init__(self):
    self.graph = dict()

  def add_node(self, node):
    self.graph[node] = set()

  def add_neighbor(self, node1, node2):
    self.graph[node1].add(node2)

  def djikstra(self, start):
    unvisited_nodes = list(graph.graph.keys())
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

    return previous_nodes, shortest_path

grid: list[list] = list()
start = ()
goal = ()
graph = Graph()

def try_step(dir: list(), cur_pos: list()):
  new_pos = [pos+dir for pos, dir in zip(cur_pos, dir)]
  if new_pos[0] > -1 and new_pos[1] > -1 and new_pos[0] < len(grid) and new_pos[1] < len(grid[0]):
    height_diff = grid[cur_pos[0]][cur_pos[1]] - grid[new_pos[0]][new_pos[1]]
    return height_diff <= 1
  else:
    return False

with open("./input.txt", "r") as input:
  for h, line in enumerate(input):
    row = list()
    for w, square in enumerate(line.strip()):
      if square == "S":
        row.append(1)
        start = (h, w)
      elif square == "E":
        row.append(26)
        goal = (h, w)
      else:
        row.append(ord(square)-96)
    grid.append(row)

  for h in range(0, len(grid)):
    for w in range(0, len(grid[0])):
      graph.add_node((h,w))
      for step in [[1,0], [-1,0], [0,1], [0,-1]]:
        if try_step(step, (h,w)):
          graph.add_neighbor((h,w), (h+step[0], w+step[1]))

  prevnode, sh_path = graph.djikstra(goal)

  # Part 1
  print(sh_path[start])

  best_hike = sys.maxsize
  for h, row in enumerate(grid):
    for w, spot in enumerate(row):
      if spot == 1 and sh_path[(h, w)] < best_hike:
        best_hike = sh_path[(h, w)]

  # Part 2
  print(best_hike)