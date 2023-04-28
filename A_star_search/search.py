import numpy as np 
from heapq import heappop, heappush
from Node import Node

'''
A* Search Path Finding algorithm. 
'''
def pathFinding(input_filepath):

  start, goal, grid = parseGridFile(input_filepath)

  explored = []
  frontier = []
  heappush(frontier, start.explore(h(start.pos, goal.pos), path_cost=0, parent=None))

  while True:

    # Heapify and pop the smallest element
    current = heappop(frontier)
    explored.append(current.pos) 

    if current.isGoal():
      return current.optimalPath(), explored, current.path_cost

    # Grab the current nodes neighbors to add to the frontier
    for neighbor in current.getNeighbors(grid): 
      # Make sure the neighbor has not been explored
      if not neighbor.pos in explored:
        heuristic = h(neighbor.pos, goal.pos)
        path_cost = current.path_cost + 1

        # check if the neighbor is in the queue already
        if neighbor in frontier:
          # if it is check if the priority function would improve.
          if(path_cost < neighbor.path_cost):
            neighbor.explore(heuristic, path_cost, current)

        else:
          # add the Node to the frontier and 'explore'
          heappush(frontier, neighbor.explore(heuristic, path_cost, current))
    
    # if the frontier is empty then there is no safe path to the goal
    # Based on the  assignment Specs this should never happen
    if not frontier:
      return None, explored, None

def parseGridFile(file):
  """
    Simple function that parses a comma seperated file create a grid of nodes and locate the start and goal nodes.
  """
  # parse the comma seperated file into a numpy 2d string array
  _grid = np.loadtxt(file, dtype=str, delimiter=',')

  start = None
  goal = None
  grid = []

  # build new grid of nodes
  for y in range(len(_grid)):
    grid.append([])
    for x in range(len(_grid[y])):
      col = _grid[y][x]
      node = Node(col, x, y)

      # Find the start and goal Nodes
      if node.isStart():
        start = node
      elif node.isGoal():
        goal = node

      grid[y].append(node)
  
  return start, goal, grid

def h(pos1, pos2):
  """
    Calculates the heuristic.
  """
  y1, x1 = pos1
  y2, x2 = pos2
  return abs(x1 - x2) + abs(y1 - y2)