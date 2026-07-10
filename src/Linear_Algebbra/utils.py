import numpy as np


def determinant(matrix):

    array = np.array(matrix, float)

    det = np.linalg.det(array)

    return round(det, 2)