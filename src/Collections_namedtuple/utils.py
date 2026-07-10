from collections import namedtuple
def calculate_average(n, columns, students):

    Student = namedtuple("Student", columns)

    total_marks = 0

    for student in students:
        data = Student(*student)
        total_marks += int(data.MARKS)

    average = total_marks / n

    return round(average, 2)