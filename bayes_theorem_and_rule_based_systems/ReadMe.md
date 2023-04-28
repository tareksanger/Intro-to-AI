# Letter Recognition with Naive Bayes and Fuzzy Classifiers

This project aims to recognize the letters A, B, C, D, and E from black-and-white images using two different classifiers: a Naive Bayes classifier and a Fuzzy classifier.

## Project files

The project contains the following files:

- `classifiers.py`: Python script with the implementation of the two classifiers.
- `train_set.csv`: CSV file with the training set of images.
- `test_set.csv`: CSV file with the test set of images.

## Requirements

To run this project, you need Python 3 and the following Python packages installed:

- NumPy
- Pandas
- SciPy

You can install these packages using pip by running:

```
pip install numpy pandas scipy
```

## Usage

To use the classifiers, you can call the functions `naive_bayes_classifier` and `fuzzy_classifier` from the `assignment2.py` script.

```python
from assignment2 import naive_bayes_classifier, fuzzy_classifier

# Load an image from a CSV file
image_path = 'path/to/image.csv'
image = pd.read_csv(image_path, header=None)

# Classify the image with the Naive Bayes classifier
nb_class, nb_prob = naive_bayes_classifier(image_path)
print('Naive Bayes Classifier:')
print(f'Class: {nb_class}')
print(f'Probabilities: {nb_prob}')

# Classify the image with the Fuzzy classifier
fuzzy_class, fuzzy_prob = fuzzy_classifier(image_path)
print('Fuzzy Classifier:')
print(f'Class: {fuzzy_class}')
print(f'Probabilities: {fuzzy_prob}')
```

The functions `naive_bayes_classifier` and `fuzzy_classifier` take as input the full file path to a CSV file containing a matrix representation of the image. The CSV file should have "1" where the image is black and "0" where the image is white.

The `naive_bayes_classifier` function outputs two values: a string indicating the most likely class for the input image (A, B, C, D, or E) and a Python list indicating the probability the input belongs to each class.

The `fuzzy_classifier` function outputs the same two values as the `naive_bayes_classifier` function.

## Implementation

The Naive Bayes classifier assumes that the features (proportion of black pixels, top proportion, and left proportion) follow a normal distribution. The probability of a feature taking on a given value is proportional to the normal distribution. The classifier computes the probabilities for each class and chooses the class with the highest probability.

The Fuzzy classifier uses fuzzy logic to classify the images. It computes the degree of membership of the input image to each class using fuzzy sets and membership functions. The classifier computes the degrees of membership for each class and chooses the class with the highest degree of membership.
