from utils import print_formatted

if __name__ == "__main__":

    number = int(input())

    result = print_formatted(number)

    for row in result:
        print(row)