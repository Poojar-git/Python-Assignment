import numpy as np
from src.Floor_Ceil_Rint.utils import floor_ceil_rint


def test_case_1():

    floor, ceil, rint = floor_ceil_rint([1.1, 2.2, 3.3])

    assert np.array_equal(floor, np.array([1., 2., 3.]))
    assert np.array_equal(ceil, np.array([2., 3., 4.]))
    assert np.array_equal(rint, np.array([1., 2., 3.]))


def test_case_2():

    floor, ceil, rint = floor_ceil_rint([-1.1, -2.5])

    assert np.array_equal(floor, np.array([-2., -3.]))
    assert np.array_equal(ceil, np.array([-1., -2.]))
    assert np.array_equal(rint, np.array([-1., -2.]))


def test_case_3():

    floor, ceil, rint = floor_ceil_rint([5.5])

    assert np.array_equal(floor, np.array([5.]))
    assert np.array_equal(ceil, np.array([6.]))
    assert np.array_equal(rint, np.array([6.]))


def test_case_4():

    floor, ceil, rint = floor_ceil_rint([0.0])

    assert np.array_equal(floor, np.array([0.]))
    assert np.array_equal(ceil, np.array([0.]))
    assert np.array_equal(rint, np.array([0.]))


def test_case_5():

    floor, ceil, rint = floor_ceil_rint([9.9, 4.4])

    assert np.array_equal(floor, np.array([9., 4.]))
    assert np.array_equal(ceil, np.array([10., 5.]))
    assert np.array_equal(rint, np.array([10., 4.]))