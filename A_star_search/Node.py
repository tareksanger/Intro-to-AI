from typing import List

START     = 'S'
GOAL      = 'G'
OBSTACLE  = 'X'
HAZARD    = 'H'
REGULAR   = 'O'
class Node:
  def __init__(self, type, x, y):
    self.type = type
    self.x = x
    self.y = y

    self.parent = None
    self.heuristic = float("inf")
    self.path_cost = float("inf")
    self.neighbors: set[Node] = None

  @property
  def pos(self) -> tuple:
    """
    Position of the Node, but the x, y. 
    The notation is backwards as requested by assignment specifications.
    Returns (y, x)
    """
    return (self.y, self.x)

  @property
  def f(self):
    """ The Priority Function """
    return self.path_cost + self.heuristic

  def isStart(self) -> bool:
    return self.type == START
  
  def isGoal(self) -> bool:
    return self.type == GOAL

  def isHazard(self) -> bool:
    return self.type == HAZARD
  
  def isObstacle(self) -> bool:
    return self.type == OBSTACLE
  
  def isRegular(self) -> bool:
    return self.type == REGULAR

  def isSafe(self, grid) -> bool:
    return  not self.isHazard()             and \
            not self.isObstacle()           and \
            not (self.isRegular()           and \
            (self.x < len(grid[self.y])-1   and grid[self.y][self.x + 1].isHazard()) or \
            (self.x > 0                     and grid[self.y][self.x - 1].isHazard()) or \
            (self.y < len(grid) - 1         and grid[self.y + 1][self.x].isHazard()) or \
            (self.y > 0                     and grid[self.y -1][self.x].isHazard()))

  def optimalPath(self) -> list[tuple]:
    """
      Returns the optimal path to the node. 

    """
    def _optimalPath(node, pathArr):
      if node is None:
        return pathArr
      return _optimalPath(node.parent, [node.pos, *pathArr])
    return _optimalPath(self, [])


  def getNeighbors(self, grid):
    """
      Finds all Neighbors that can be visited safely.
    """
    if self.neighbors:
      return self.neighbors
    
    neighbors = set()
    if self.y < len(grid) -1            and grid[self.y+1][self.x].isSafe(grid):    neighbors.add(grid[self.y+1][self.x])
    if self.y > 0                       and grid[self.y-1][self.x].isSafe(grid):    neighbors.add(grid[self.y-1][self.x])
    if self.x < len(grid[self.y]) - 1   and grid[self.y][self.x + 1].isSafe(grid):  neighbors.add(grid[self.y][self.x + 1])
    if self.x > 0                       and grid[self.y][self.x - 1].isSafe(grid):  neighbors.add(grid[self.y][self.x - 1])

    self.neighbors = neighbors
    return neighbors

  def explore(self, heuristic: float, path_cost: float, parent):
    """
      Function simply prepares the node to be added to the frontiers priority queue. 
      By setting the heuristic, path_cost and parent so that the nodes priority function and be properly calculated. 
    """
    self.heuristic = heuristic
    self.path_cost = path_cost
    self.parent    = parent
    return self

  def __hash__(self):
        return hash(self.pos)

  def __lt__(self, other):
    """ 
      Using the priority function to determine 
      if one node is greater than the other  
    """
    return self.f < other.f

  def __eq__(self, other):
    return self.pos == other.pos
  
  def __ne__(self, other):
    return self.pos != other.pos

  def __repr__(self):
    return f'pos: {self.pos}, f: {self.f}, path_cost: {self.path_cost}, h: {self.heuristic}'


