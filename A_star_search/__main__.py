import os

from search import pathFinding

def main():
  for i in range(4):
    optimal_path, explored, path_cost = pathFinding(os.path.abspath(f"./Examples/Example{i}/input.txt"))
    print(f'Example {i}', '_' * 20)
    print("Optimal Path: ", optimal_path)
    print("Explored: ", explored)
    print("Path Cost: ", path_cost)
    print('_' * 40,'\n')


if __name__ == '__main__':
    main()