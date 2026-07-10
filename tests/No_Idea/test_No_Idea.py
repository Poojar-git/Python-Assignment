from src.No_Idea.utils import happiness


def test_case_1():

    array = [1, 5, 3]
    set_a = {3, 1}
    set_b = {5, 7}

    assert happiness(array, set_a, set_b) == 1


def test_case_2():

    array = [1, 2, 3, 4]
    set_a = {1, 2}
    set_b = {3, 4}

    assert happiness(array, set_a, set_b) == 0


def test_case_3():

    array = [1, 1, 1]
    set_a = {1}
    set_b = {2}

    assert happiness(array, set_a, set_b) == 3


def test_case_4():

    array = [5, 6, 7]
    set_a = {1, 2}
    set_b = {5, 6}

    assert happiness(array, set_a, set_b) == -2


def test_case_5():

    array = [10, 20, 30]
    set_a = {40}
    set_b = {50}

    assert happiness(array, set_a, set_b) == 0