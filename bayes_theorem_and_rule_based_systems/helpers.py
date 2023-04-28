import numpy as np

# Reads the csv file and returns the full matrix, and the top half and left of the matrix
def read_csv(file):
  full = np.loadtxt(file, dtype=np.int32, delimiter=',')
  # Get the Top half of the matrix
  top = full[:len(full)//2]
  # Get the left half of the matrix
  left = [row[:len(full[0])//2] for row in full]
  return full, top, left

# Calculates each of the proportions, prop_black, top_black & left_prop
def calculate_proportions(file):

  matrix, matrix_top, matrix_left = read_csv(file)
  
  # counts all the one black pixels (1s)
  def count_black(_matrix): 
    return sum([sum(x) for x in _matrix])

  # Count Pixels
  number_of_pixels = matrix.size
  total_number_of_black_pixels = count_black(matrix)

  # Returns the prop_black, top_prop and left_prop
  return total_number_of_black_pixels/number_of_pixels, \
    count_black(matrix_top)/total_number_of_black_pixels, \
    count_black(matrix_left)/total_number_of_black_pixels
