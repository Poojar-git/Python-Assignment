import numpy as np


def min_and_max(matrix):

    array = np.array(matrix)

    min_values = np.min(array, axis=1)

    max_value = np.max(min_values)

    return max_value