from utils import determinant

if __name__ == "__main__":

    n = int(input())

    matrix = []

    for _ in range(n):
        row = list(map(float, input().split()))
        matrix.append(row)

    print(determinant(matrix))