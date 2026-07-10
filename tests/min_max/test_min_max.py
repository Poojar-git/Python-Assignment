from src.Min_and_Max.utils import min_and_max


def test_case_1():

    matrix = [
        [2, 5],
        [3, 7],
        [1, 3],
        [4, 0]
    ]

    assert min_and_max(matrix) == 3


def test_case_2():

    matrix = [
        [1, 2],
        [3, 4]
    ]

    assert min_and_max(matrix) == 3


def test_case_3():

    matrix = [
        [5]
    ]

    assert min_and_max(matrix) == 5


def test_case_4():

    matrix = [
        [9, 8, 7],
        [6, 5, 4],
        [3, 2, 1]
    ]

    assert min_and_max(matrix) == 7


def test_case_5():

    matrix = [
        [10, 20, 30],
        [40, 50, 60]
    ]

    assert min_and_max(matrix) == 40