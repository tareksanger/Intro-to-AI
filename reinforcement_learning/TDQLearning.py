from State import State
import csv

# Temporal Difference Learning
# Q-Function
class TDQLearning:
  
  alpha = 0.2
  gamma = 0.9

  def __init__(self, trial_filepath):
    # trial_filepath is the path to a file containing a trial through state space
    # Return nothing
    self._trials: dict[str, State] = {}
    with open(trial_filepath) as file:
      trials = list(csv.reader(file))
      for i in range(len(trials)):
        # Grab the current trial state and action
        state = trials[i][0]
        action = trials[i][1]
        
        # Grab the next state (if there is one)
        nState = trials[i+ 1][0] if i + 1 != len(trials) else None

        # Add the states to the Trials dictionary
        if state not in self._trials:
          self._trials[state] = State(state)

        if nState is not None and nState not in self._trials:
          self._trials[nState] = State(nState)

        q = self.__Q(state, action, nState)
        self._trials[state].set_q_value(action, q)

          
  
  def __Q(self, state: str, action:str, nState):
    # Private Function to calculate the Q value of the state
    # Just trying to make this more readable
    alpha = TDQLearning.alpha
    gamma = TDQLearning.gamma

    maxQ = self._trials[nState].maxQ() if nState is not None else 0

    qVal = self.qvalue(state, action)
    reward = self.r(state)

    return qVal + alpha * (reward + gamma * maxQ - qVal)


  def r(self, state: str):
    # Calculate the reward
    return -1 if state[0] == state[1] else 1


  def qvalue(self, state: str, action: str):
    if state not in self._trials:
      self._trials[state] = State(state)
    # Return the q-value for the state-action pair
    return self._trials[state].q(action)

  def policy(self, state: str):
    if state not in self._trials:
      self._trials[state] = State(state)
    # state is a string representation of a state
    # Return the optimal action under the learned policy
    return self._trials[state].policy
  