# Temporal Difference Q-Learning Implementation for Mouse and Cat Game

This implementation aims to solve the problem of a cat and a mouse in a room with four squares using Temporal Difference Q-learning.

## Problem Description

Consider a cat and a mouse in a room with four squares, as illustrated below. If the cat and mouse occupy the same square, the mouse receives negative reward. If the cat and mouse occupy different squares, the mouse receives positive reward. In this assignment, we will use temporal difference Q-learning to learn the optimal policy for the mouse to achieve as much reward as possible.

```
Square W  Square X
Square Y  Square Z
```

The mouse agent can take the following actions: do not move or move to a horizontally or vertically adjacent square. Assume that this is a fully observable environment. That is, the mouse knows for all times its position and the cat’s position. Assume that this is a discrete time environment. At each time, the mouse agent may take one action. Furthermore, at each time, with some probability, the cat may move to a horizontally or vertically adjacent square.

Use the following string representations for states: `MC`

- Where `M` is the square the mouse is in
- Where `C` is the square the cat is in

Use the following string representations for actions: `"N"`, `"L"`, `"R"`, `"U"`, `"D"`

- `"N"`: do not move
- `"L"`: move left
- `"R"`: move right
- `"U"`: move up
- `"D"`: move down

The reward `r` associated with a state `s` is:

- `r(s) = -1` if `M == C`
- `r(s) = +1` if `M != C`

Use the following parameters:

- `Gamma = 0.9` (discount factor)
- `Alpha = 0.2` (learning rate)

Initially estimate the Q-function as:

- `Q(s, a) = 0`

## Implementation Details

This implementation contains a file named `TDQLearning.py` with a class named `TDQLearning`.

The `TDQLearning` class has three member functions: `__init__`, `qvalue`, and `policy`.

The function `__init__` is a constructor that takes one input argument (in addition to `self`). The input argument is the full path to a CSV file containing a trial through the state space. The CSV file contains two columns, the first with a string representation of the state and the second with a string representation of the action taken in that state. The ith row of the CSV file indicates the state-action pair at time i. You may assume only valid actions are taken in each state in the trial.

The function `qvalue` takes two input arguments (in addition to `self`). The first input argument is a string representation of a state. The second input argument is the string representation of an action. The function returns the Q-value associated with that state-action pair (according to the Q-function learned from the trial in the file passed to the `__init__` function).

The function `policy` takes one input argument (in addition to `self`). The input argument is a string representation of a state. The function returns the optimal action (according to the Q-function learned from the trial in the file passed to the `__init__` function). In the case of a tie (i.e. multiple actions are equally optimal), the function may return any one of the equally optimal actions.
