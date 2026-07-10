from utils import can_stack

if __name__ == "__main__":

    t = int(input())

    for _ in range(t):

        n = int(input())

        cubes = list(map(int, input().split()))

        print(can_stack(cubes))