from utils import word_order

if __name__ == "__main__":

    n = int(input())

    words = []

    for _ in range(n):
        words.append(input())

    count, frequency = word_order(words)

    print(count)
    print(*frequency)