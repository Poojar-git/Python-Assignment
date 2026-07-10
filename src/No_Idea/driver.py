from utils import happiness

if __name__ == "__main__":

    n, m = map(int, input().split())

    array = list(map(int, input().split()))

    set_a = set(map(int, input().split()))

    set_b = set(map(int, input().split()))

    print(happiness(array, set_a, set_b))