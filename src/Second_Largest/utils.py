def second_largest(arr):
    largest=float('-inf')
    second=float('-inf')
    for i in arr:
        if i>largest:
            second=largest
            largest=i
        elif i>second and i!=largest:
            second=i
    return second