from src.Second_Largest.utils import second_largest
def test1():
    assert second_largest([1, 2, 3, 4, 4])==3
def test2():
    assert second_largest([0, 0, -1, 0, 0])==-1
def test3():
    assert second_largest([5, 4, 4])==4
def test4():
    assert second_largest([-1, -2, -3, -4])==-2
def test5():
    assert second_largest([1, 0, 0, 0, 1])==0