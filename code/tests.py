# tests.py
from fib import fib, fibr

def test_fib_output():
    assert fib(0) == 0
    assert fib(1) == 1
    assert fib(2) == 1
    assert fib(3) == 2
    assert fib(4) == 3
    assert fib(5) == 5

def test_fibr_output():
    assert fibr(0) == 0
    assert fibr(1) == 1
    assert fibr(2) == 1
    assert fibr(3) == 2
    assert fibr(4) == 3
    assert fibr(5) == 5

def test_fib_negative_number_raises_error():
    try:
        fib(-1)
        assert False # should never happen!
    except Exception:
        pass

def test_fibr_negative_number_raises_error():
    try:
        fibr(-1)
        assert False # should never happen!
    except Exception:
        pass

def test_fibr_large_numbers():
    assert fib(1000) > 0 # who even knows the 1000th Fibonacci number?!