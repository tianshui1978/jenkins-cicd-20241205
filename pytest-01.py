# test_example.py

def add(a, b):
    """Return the sum of a and b"""
    return a + b

def test_add1():
    assert add(2, 3) == 5

def test_add2():
    assert add(-1, 1) == 0

def test_add3():
    assert add(-1, -1) == -2

def test_add4():
    assert add(-3, -1) == -4
