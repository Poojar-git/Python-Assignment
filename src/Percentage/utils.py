def average(marks):
    sum=0
    for i in range(len(marks)):
        sum+=marks[i]
    avg=sum/len(marks)
    return avg