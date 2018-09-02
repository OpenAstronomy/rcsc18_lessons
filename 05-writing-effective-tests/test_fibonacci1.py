import numpy as np

from fibonacci import fib, fib_numpy


def test_fib_10():
    """Test fib(10) for correct output values and length."""
    a = fib(10)
    assert len(a) == 10
    assert a == [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]


def test_fib_numpy_10():
    """Test fib_numpy(10) for correct output values and length."""
    a = fib_numpy(10)
    assert len(a) == 10
    assert np.allclose(a, [1, 1, 2, 3, 5, 8, 13, 21, 34, 55])
