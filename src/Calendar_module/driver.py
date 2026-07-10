from utils import find_day

if __name__ == "__main__":

    month, day, year = map(int, input().split())

    print(find_day(month, day, year))   