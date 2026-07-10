from utils import calculate_average

if __name__ == "__main__":

    n = int(input())

    columns = input().split()

    students = []

    for _ in range(n):
        students.append(input().split())

    print(f"{calculate_average(n, columns, students):.2f}")