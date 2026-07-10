from src.Calendar_Module.utils import find_day
def test_case_1():
    assert find_day(8, 5, 2015) == "WEDNESDAY"
def test_case_2():
    assert find_day(1, 1, 2024) == "MONDAY"
def test_case_3():
    assert find_day(25, 12, 2023) == "MONDAY"
def test_case_4():
    assert find_day(15, 8, 1947) == "FRIDAY"
def test_case_5():
    assert find_day(31, 12, 2025) == "WEDNESDAY"