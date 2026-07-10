from src.Merge_the_tools.utils import merge_the_tools


def test_case_1():
    assert merge_the_tools("AABCAAADA", 3) == {"AB", "CA", "AD"}
    
def test_case_2():
    assert merge_the_tools("abrakadabra", 3) == {"abr", "ak", "dab", "ra"}


def test_case_3():
    assert merge_the_tools("AAAAAA", 2) == {"A", "A", "A"}


def test_case_4():
    assert merge_the_tools("abcdef", 2) == {"ab", "cd", "ef"}


def test_case_5():
    assert merge_the_tools("zzzz", 1) == {"z", "z", "z", "z"}