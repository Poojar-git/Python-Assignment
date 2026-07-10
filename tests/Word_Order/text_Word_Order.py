from src.Word_Order.utils import word_order


def test_case_1():

    words = [
        "bcdef",
        "abcdefg",
        "bcde",
        "bcdef"
    ]

    assert word_order(words) == (3, [2, 1, 1])


def test_case_2():

    words = [
        "apple",
        "banana",
        "apple",
        "orange",
        "banana"
    ]

    assert word_order(words) == (3, [2, 2, 1])


def test_case_3():

    words = [
        "python"
    ]

    assert word_order(words) == (1, [1])


def test_case_4():

    words = [
        "a",
        "a",
        "a",
        "a"
    ]

    assert word_order(words) == (1, [4])


def test_case_5():

    words = [
        "cat",
        "dog",
        "bird"
    ]

    assert word_order(words) == (3, [1, 1, 1])