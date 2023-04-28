from typing import List

class Feature():
  '''
    Used in the Fuzzy Classifier
  '''
  def __init__(self, low, medium, high):
    self.low = low
    self.medium = medium
    self.high = high
