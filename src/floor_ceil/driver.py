import numpy as np
from utils import floor_ceil_rint

if __name__ == "__main__":

    np.set_printoptions(legacy='1.13')

    arr = list(map(float, input().split()))

    floor, ceil, rint = floor_ceil_rint(arr)

    print(floor)
    print(ceil)
    print(rint)