from utils import second_largest
if __name__ == '__main__':
    n = int(input())
    arr1 = map(int, input().split())
    print(second_largest(arr1))