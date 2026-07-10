import numpy as np


def mean_var_std(matrix):

    array = np.array(matrix)

    mean = np.mean(array, axis=1)

    var = np.var(array, axis=0)

    std = np.std(array)

    return mean, var, round(std, 11)