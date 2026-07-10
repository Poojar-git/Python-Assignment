import numpy as np
from src.Mean_Var_Std.utils import mean_var_std


def test_case_1():

    matrix = [
        [1, 2],
        [3, 4]
    ]

    mean, var, std = mean_var_std(matrix)

    assert np.array_equal(mean, np.array([1.5, 3.5]))
    assert np.array_equal(var, np.array([1., 1.]))
    assert std == round(np.std(np.array(matrix)), 11)


def test_case_2():

    matrix = [
        [1, 2, 3],
        [4, 5, 6]
    ]

    mean, var, std = mean_var_std(matrix)

    assert np.array_equal(mean, np.array([2., 5.]))
    assert np.array_equal(var, np.array([2.25, 2.25, 2.25]))
    assert std == round(np.std(np.array(matrix)), 11)


def test_case_3():

    matrix = [
        [5]
    ]

    mean, var, std = mean_var_std(matrix)

    assert np.array_equal(mean, np.array([5.]))
    assert np.array_equal(var, np.array([0.]))
    assert std == 0.0


def test_case_4():

    matrix = [
        [2, 2],
        [2, 2]
    ]

    mean, var, std = mean_var_std(matrix)

    assert np.array_equal(mean, np.array([2., 2.]))
    assert np.array_equal(var, np.array([0., 0.]))
    assert std == 0.0


def test_case_5():

    matrix = [
        [10, 20],
        [30, 40]
    ]

    mean, var, std = mean_var_std(matrix)

    assert np.array_equal(mean, np.array([15., 35.]))
    assert np.array_equal(var, np.array([100., 100.]))
    assert std == round(np.std(np.array(matrix)), 11)