if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    largest=float('-inf')
    second=float('-inf')
    for i in arr:
        if i>largest:
            second=largest
            largest=i
        elif i>second and i!=largest:
            second=i
    print(second)
        
