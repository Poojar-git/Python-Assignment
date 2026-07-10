from src.Iterables_and_Iterators.utils import probability_of_a


def test_case_1():

    letters = ['a', 'b', 'c']

    assert probability_of_a(letters, 2) == 0.6667


def test_case_2():

    letters = ['a', 'a', 'b']

    assert probability_of_a(letters, 2) == 1.0


def test_case_3():

    letters = ['b', 'c', 'd']

    assert probability_of_a(letters, 2) == 0.0


def test_case_4():

    letters = ['a', 'b', 'c', 'd']

    assert probability_of_a(letters, 1) == 0.25


def test_case_5():

    letters = ['a', 'b', 'a', 'c']

    assert probability_of_a(letters, 2) == 0.8333