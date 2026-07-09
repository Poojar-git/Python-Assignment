from src.Lists.utils import list_command
def test1():
    assert list_command([],["insert", "0", "2"])==[2]
def test2():
    assert list_command([2],["insert", "1", "6"])==[2, 6]
def test2():
    assert list_command([2, 6],["insert", "2", "5"])==[2, 6, 5]
def test2():
    assert list_command([2, 6, 5],["remove", 6])==[2, 5]
def test2():
    assert list_command([2,5], ["pop"])==[2]