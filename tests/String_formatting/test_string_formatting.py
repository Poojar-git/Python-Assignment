from src.String_Formatting.utils import print_formatted


def test_case_1():
    assert print_formatted(1) == [
        "1 1 1 1"
    ]


def test_case_2():
    assert print_formatted(2) == [
        "1 1 1 1",
        "2 2 2 10"
    ]


def test_case_3():
    assert len(print_formatted(5)) == 5


def test_case_4():
    assert print_formatted(3)[2] == "3 3 3 11"


def test_case_5():
    assert print_formatted(4)[3] == "4 4 4 100"