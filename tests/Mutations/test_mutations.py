from src.Mutations.utils import mutate_string
def test1():
    assert mutate_string("apples", 4, "o")=="applos"
def test1():
    assert mutate_string("laptop", 1, "o")=="loptop"
def test1():
    assert mutate_string("main", 0, "o")=="oain"
