POSSIBLE_MOVES = {
    "W":  ["N", "D",   "R" ],
    "X":  ["N", "D",   "L" ],
    "Y":  ["N", "U",   "R" ],
    "Z":  ["N", "U",   "L"]
  }
class State(object):
  

  def __init__(self, state: str):
    self._state = state
    # Set the default Q values for each of the possible moves
    self._q_values = dict((action,0) for action in POSSIBLE_MOVES[state[0]])
    # default the policy to Do not move
    self.policy = "N"

  def set_q_value(self, action: str, value: float):
    # Check if the current policies Q value is less than the new Q Value
    if self._q_values[self.policy] < value:
      self.policy = action
    
    self._q_values[action] = value

  def q(self, action: str) -> float:
    return self._q_values[action]

  def maxQ(self) -> float:
    return max(list(self._q_values.values()))
