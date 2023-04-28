from typing import List
import numpy as np
import math

from Letter import Letter
from Feature import Feature
from helpers import *

def naive_bayes_classifier(input_filepath):
  
  # read the input file and calculate the proportions
  prop_black, top_prop, left_prop = calculate_proportions(input_filepath)

  # Letter set up based on Assignment specifications
  A = Letter(
    value='A', 
    prior_probability= 0.28, 
    features=[
      normal_distribution(x=prop_black,   mean=0.38,  standard_deviation=0.06),
      normal_distribution(x=top_prop,     mean=0.46,  standard_deviation=0.12),
      normal_distribution(x=left_prop,    mean=0.5,   standard_deviation=0.09)
    ])
  B = Letter(
    value=  'B', 
    prior_probability=  0.05, 
    features=[
      normal_distribution(x=prop_black,   mean=0.51, standard_deviation=0.06),
      normal_distribution(x=top_prop,     mean=0.49, standard_deviation=0.12),
      normal_distribution(x=left_prop,    mean=0.57, standard_deviation=0.09)
    ])
  C = Letter(
    value='C', 
    prior_probability= 0.10, 
    features=[
      normal_distribution(x=prop_black,   mean=0.31, standard_deviation=0.06),
      normal_distribution(x=top_prop,     mean=0.37, standard_deviation=0.09),
      normal_distribution(x=left_prop,    mean=0.64, standard_deviation=0.06)
    ])
  D = Letter(
    value='D', 
    prior_probability= 0.15,
    features=[
      normal_distribution(x=prop_black, mean=0.39, standard_deviation=0.06),
      normal_distribution(x=top_prop,   mean=0.47, standard_deviation=0.09),
      normal_distribution(x=left_prop,  mean=0.57, standard_deviation=0.03)
    ])
  E = Letter(
    value='E', 
    prior_probability= 0.42, 
    features=[
      normal_distribution(x=prop_black,   mean=0.43, standard_deviation=0.12),
      normal_distribution(x=top_prop,     mean=0.45, standard_deviation=0.15),
      normal_distribution(x=left_prop,    mean=0.65, standard_deviation=0.09)
    ])

  # List of all letters
  LETTERS = [A, B, C, D, E]

  # most_likely_class is a string indicating the most likely class, either "A", "B", "C", "D", or "E"
  most_likely_class = max(LETTERS, key=lambda item: item.probability(LETTERS)).value
  # class_probabilities is a five element list indicating the probability of each class in the order [A probability, B probability, C probability, D probability, E probability]
  class_probabilities = [letter.probability_given_evidence for letter in LETTERS]

  
  return most_likely_class, class_probabilities

def fuzzy_classifier(input_filepath):

  # read the input file and calculate the proportions 
  # pd = prop_black, tp = top_prop, lb = left_prop
  pb, tp, lp = calculate_proportions(input_filepath)


  prop_black = Feature(
    low=    trapezoidal(a=0,    b=0,    c=0.3,  d=0.4,  x=pb),
    medium= trapezoidal(a=0.3,  b=0.4,  c=0.4,  d=0.5,  x=pb),
    high=   trapezoidal(a=0.4,  b=0.5,  c=1,    d=1,    x=pb)
    )

  top_prop = Feature(
    low=      trapezoidal(a=0,    b=0,    c=0.3,  d=0.4,  x=tp),
    medium=   trapezoidal(a=0.3,  b=0.4,  c=0.5,  d=0.6,  x=tp),
    high=     trapezoidal(a=0.5,  b=0.6,  c=1,    d=1,    x=tp)
  )

  left_prop = Feature(
    low=      trapezoidal(a=0,    b=0,    c=0.3,  d=0.4,  x=lp),
    medium=   trapezoidal(a=0.3,  b=0.4,  c=0.6,  d=0.7,  x=lp),
    high=     trapezoidal(a=0.6,  b=0.7,  c=1,    d=1,    x=lp)
  )   

  results = {
    # IF PropBlack is Medium AND (TopProp is Medium OR LeftProp is Medium) THEN class A
    'A': min(prop_black.medium, max(top_prop.medium, left_prop.medium)),
    # IF PropBlack is High AND TopProp is Medium AND LeftProp is Medium THEN class B.
    'B': min([prop_black.high, top_prop.medium, left_prop.medium]),
    # IF (PropBlack is Low AND TopProp is Medium) OR LeftProp is High THEN class C.
    'C': max(min(prop_black.low, top_prop.medium), left_prop.high),
    # IF PropBlack is Medium AND TopProp is Medium AND LeftProp is High THEN class D.
    'D': min([prop_black.medium, top_prop.medium, left_prop.high]),
    # IF PropBlack is High AND TopProp is Medium AND LeftProp is High THEN class E.
    'E': min([prop_black.high, top_prop.medium, left_prop.high])
  }

  # highest_membership_class is a string indicating the highest membership class, either "A", "B", "C", "D", or "E"
  class_memberships = list(results.values())
  # class_memberships is a four element list indicating the membership in each class in the order [A value, B value, C value, D value, E value]
  highest_membership_class =  max(results, key=results.get)

  return highest_membership_class, class_memberships

# Used to calculate the Features Normal Distribution
def normal_distribution(standard_deviation: float, mean: float, x: float):
  return (1.0/math.sqrt(2.0 * math.pi * standard_deviation**2.0))*(math.e **(-0.5* ((x - mean)/standard_deviation)**2.0))

def trapezoidal( a: float, b:float, c:float, d: float, x):
  if(x <= a):
    return 0
  
  elif a < x and x < b:
    return (x-a)/(b-a)
  
  elif b <= x and x <=c:
    return 1
  
  elif c < x and x < d:
    return (d-x)/(d-c)

  elif d <= x:
    return 0