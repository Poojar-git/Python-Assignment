from utils import probability_of_a

if __name__ == "__main__":

    n = int(input())

    letters = input().split()

    k = int(input())

    print(f"{probability_of_a(letters, k):.4f}")