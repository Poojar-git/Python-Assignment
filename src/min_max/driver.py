from utils import min_and_max

if __name__ == "__main__":

    n, m = map(int, input().split())

    matrix = []

    for _ in range(n):
        row = list(map(int, input().split()))
        matrix.append(row)

    print(min_and_max(matrix))