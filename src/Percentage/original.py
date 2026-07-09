n=intput()
student={}
for i in range(n):
    data=input().split()
    name=data[0]
    marks=list(map(dat[1:]))
    student[name]=marks
query_name=input()
overall_marks=student[query_name]
sum=0
for i in range(len(overall_marks)):
    sum+=overall_marks
avg=sum/len(overall_marks)
print(f"{avg:.2f}")