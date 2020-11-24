from os import getcwd
from json import load
from math import sqrt

# DATASET HAS
# Gender, Height, Weight, Index

# Indexes
# 0 - Extremely Weak

# 1 - Weak

# 2 - Normal

# 3 - Overweight

# 4 - Obesity

# 5 - Extreme Obesity

# Load the data set from .json file
with open(f'{getcwd()}/BMI_DATASET.json') as f:
    dataset = load(f)

# Filter out men and women

men = [person for person in dataset if person['Gender'] == 'Male']
women = [person for person in dataset if person['Gender'] == 'Female']

# Function to calculate euclidean distance
def euclidean_distance(first, second):
    height = (first['Height'] - second['Height']) ** 2
    weight = (first['Weight'] - second['Weight']) ** 2

    return sqrt(height + weight)


# This function returns nearest K neighbours of our new element
# we want to classify 
def get_neighbours(dataset, element, k):
    distances = []

    # For every trainee in dataset, we calculate the euclidean distance
    for trainee in dataset:
        distances.append([trainee, euclidean_distance(element, trainee)])

    # We sort the calculated distances
    distances.sort(key=lambda element: element[1])

    # We get the first K elements from the list

    neighbours = []
    for i in range(int(k)):
        neighbours.append(distances[i][0])

    return neighbours


def get_prediction(element, dataset):
    neighbours = get_neighbours(dataset, element, sqrt(len(dataset)))
    # We get the neighbours and determine the class

    # We find the class for our element

    # Find all the classes

    classes_only = [item['Index'] for item in neighbours]

    return max(set(classes_only), key = classes_only.count)


def printBMI(arg):
    # This functions prints different statements based on class

    if arg == 5:
        print('Extreme Obesity')

    elif arg == 4:
        print('Obesity')

    elif arg == 3:
        print('Overweight')
        
    elif arg == 2:
        print('Normal')

    elif arg == 1:
        print('Weak')
        
    elif arg == 1:
        print('Extremely Weak')
    
    else:
        print('Non existant class, range if from 0 - 5... You entered something wrong')

someone = { 'Gender': 'Male', 'Height': 183, 'Weight': 75 }
# If it's a woman put women as second argument
# If it's a man put men as second argument
prediction = get_prediction(someone, men)

printBMI(prediction)
