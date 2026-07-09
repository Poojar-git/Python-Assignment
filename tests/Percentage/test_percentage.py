from src.Percentage.utils import average
def test_1():
    assert average([1,2,3])==2
def test_2():
    assert average([10,20,30])==20
def test_3():
    assert average([10.5,20.5,30.5])==20.5
def test_4():
    assert average([-10, -20, -30])==-20
def test_5():
    assert average([0,0,0])==0