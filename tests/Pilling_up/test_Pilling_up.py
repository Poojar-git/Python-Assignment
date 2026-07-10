from src.Piling_Up.utils import can_stack


def test_case_1():

    assert can_stack([4, 3, 2, 1, 3, 4]) == "Yes"


def test_case_2():

    assert can_stack([1, 3, 2]) == "No"


def test_case_3():

    assert can_stack([1]) == "Yes"


def test_case_4():

    assert can_stack([5, 4, 3, 2, 1]) == "Yes"


def test_case_5():

    assert can_stack([2, 1, 2]) == "No"