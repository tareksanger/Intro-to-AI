import os
from classifiers import naive_bayes_classifier, fuzzy_classifier


def main():
  

  for i in range(5):
    print(f"\nNaive Bayes {i}.",'__'*10)
    most_likely_class, class_probabilities = naive_bayes_classifier(
      os.path.abspath(f"./Examples/Example{i}/input.csv"))
    
    print(f"most_likely_class: {most_likely_class}")
    print(f"class_probabilities: {class_probabilities}")
    print('\n')
    
    print(f"Fuzzy {i}.",'__'*10)
    highest_membership_class, class_memberships = fuzzy_classifier(os.path.abspath(f"./Examples/Example{i}/input.csv"))

    print(f"highest_membership_class: {highest_membership_class}")
    print(f"class_memberships: {class_memberships}")
    print('\n\n')





  





if __name__ == '__main__':
    main()