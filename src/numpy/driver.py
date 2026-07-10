import numpy as np
from utils import mean_var_std

if __name__ == "__main__":

    np.set_printoptions(legacy="1.13")

    n, m = map(int, input().split())

    matrix = []

    for _ in range(n):
        row = list(map(int, input().split()))
        matrix.append(row)

    mean, var, std = mean_var_std(matrix)

    print(mean)
    print(var)
    print(std)