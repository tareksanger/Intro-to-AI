# Pathfinding using A\* Search Algorithm

This program implements A\* search algorithm to find the optimal path from a start state to a goal state on a grid-like environment with hazards.

## Input

The input to the program is a comma separated value (CSV) file that contains a rectangular grid with the following symbols:

- 'S' (start state)
- 'G' (goal state)
- 'X' (wall/obstacle that cannot be traversed)
- 'H' (hazard that cannot be traversed nor can any square adjacent to it be traversed)
- 'O' (regular square which can be visited provided it is not adjacent to a hazard)

## Output

The program returns three outputs:

1. A list of tuples along the optimal path from the start state to a goal state (including the start state and the goal state).
2. A list of tuples that were explored during the A\* search, in order (including the start state and the goal state).
3. The cost of the optimal path from the start state to the goal state.

## Implementation

The program contains a named `search.py` with a function named `pathfinding`, which implements the A\* search algorithm to find the optimal path from the start state to the goal state.

The function takes one input argument, which should be the full file path to the CSV file that contains the input grid.

The function returns three outputs, which are described above.

## Execution

To execute the program, call the `pathfinding` function in `search.py` and pass the full file path to the CSV file as an argument.

```python
from search import pathfinding

optimal_path, explored_nodes, optimal_cost = pathfinding('path/to/grid.csv')
```

## Example

Suppose we have the following input grid:

```
S,O,O
O,X,O
O,X,O
H,O,G
```

The program will return the following outputs:

```python
optimal_path = [(0, 0), (0, 1), (0 ,2), (1, 2), (2, 2), (3, 2)]
explored_nodes = [(0, 0), (1, 0), (0, 1), (0 ,2), (1, 2), (2, 2), (3, 2)]
optimal_cost = 5
```
