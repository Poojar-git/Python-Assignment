import numpy as np


def floor_ceil_rint(arr):

    array = np.array(arr, float)

    floor = np.floor(array)
    ceil = np.ceil(array)
    rint = np.rint(array)

    return floor, ceil, rint