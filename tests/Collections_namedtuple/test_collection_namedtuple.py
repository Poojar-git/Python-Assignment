from src.NamedTuple.utils import calculate_average


def test_case_1():

    columns = ["ID", "MARKS", "NAME", "CLASS"]

    students = [
        ["1", "97", "Raymond", "7"],
        ["2", "50", "Steven", "4"],
        ["3", "91", "Adrian", "9"],
        ["4", "72", "Stewart", "5"],
        ["5", "80", "Peter", "6"]
    ]

    assert calculate_average(5, columns, students) == 78.0


def test_case_2():

    columns = ["ID", "MARKS", "NAME", "CLASS"]

    students = [
        ["1", "100", "A", "1"]
    ]

    assert calculate_average(1, columns, students) == 100.0


def test_case_3():

    columns = ["ID", "MARKS", "NAME", "CLASS"]

    students = [
        ["1", "60", "A", "1"],
        ["2", "80", "B", "1"]
    ]

    assert calculate_average(2, columns, students) == 70.0


def test_case_4():
    columns = ["ID", "MARKS", "NAME", "CLASS"]
    students = [
        ["1", "90", "A", "1"],
        ["2", "90", "B", "1"],
        ["3", "90", "C", "1"]
    ]

    assert calculate_average(3, columns, students) == 90.0
def test_case_5():
    columns = ["ID", "MARKS", "NAME", "CLASS"]
    students = [
        ["1", "10", "A", "1"],
        ["2", "20", "B", "1"],
        ["3", "30", "C", "1"],
        ["4", "40", "D", "1"]
    ]
    assert calculate_average(4, columns, students) == 25.0