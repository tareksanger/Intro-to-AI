import os
from TDQLearning import TDQLearning
import numpy as np

def main():

  for i in range(4):
    print(f"{i}. Example _________________")
    example_path = os.path.abspath(f"./Examples/Example{i}")
    trail_filepath = os.path.join(example_path, "trial.csv")
    qvalue_test_path = os.path.join(example_path, "qvalue_tests.csv")
    policy_test_path = os.path.join(example_path, "policy_tests.csv")

    test = TDQLearning(trail_filepath)

    qvalue_test_values = np.loadtxt(qvalue_test_path, dtype=str, delimiter=',')

    print("Q Value Test ______")
    for qvalue_test in qvalue_test_values:
      state = qvalue_test[0]
      action = qvalue_test[1]

      value = float(qvalue_test[2])
      my_value =  float(test.qvalue(state, action))
      print(f"State: {state} Action: {action}")
      print(f"Value: {my_value}, \t TRUE: {value}")
      if my_value != value:
        print("FAIL ________ ")


    print("\n\nPolicy Test ______")
    policy_test_values = np.loadtxt(policy_test_path, dtype=str, delimiter=',')

    for p_test in policy_test_values:
      pState = p_test[0]
      pValue = p_test[1]

      p = test.policy(pState)
      print(f"State: {pState}")
      print(f"Value: {p}, \t TRUE: {pValue}")

      if p != pValue:
        print("FAIL ________ ")
    print('\n\n')

if __name__ == "__main__":
  main()