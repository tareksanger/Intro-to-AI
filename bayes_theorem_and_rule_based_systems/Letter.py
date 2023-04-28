from typing import List
import numpy as np
import math

class Letter():
  ''' 
    Used in the Naive Bayes Classifier
  '''
  def __init__(self, prior_probability:float,  value: str, features: List[float]):
    self.prior_probability = prior_probability
    self.value = value
    self.features = features
    self.probability_given_evidence = 0.0
      
  def rp_evidence(self):
    from functools import reduce
    # Multiples all feature normal distributions and the prior probability
    return reduce((lambda x, y: x * y), self.features)  * self.prior_probability

  
  def probability(self, letters: List):  
    self.probability_given_evidence = self.rp_evidence()/sum([l.rp_evidence() for l in letters])
    return self.probability_given_evidence
