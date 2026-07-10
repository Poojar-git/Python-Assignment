from src.Linear_Algebra.utils import determinant


def test_case_1():

    matrix = [
        [1.1, 1.1],
        [1.1, 1.1]
    ]

    assert determinant(matrix) == 0.0


def test_case_2():

    matrix = [
        [1, 2],
        [3, 4]
    ]

    assert determinant(matrix) == -2.0


def test_case_3():

    matrix = [
        [2, 0],
        [0, 2]
    ]

    assert determinant(matrix) == 4.0


def test_case_4():

    matrix = [
        [5]
    ]

    assert determinant(matrix) == 5.0


def test_case_5():

    matrix = [
        [3, 1],
        [2, 2]
    ]

    assert determinant(matrix) == 4.0