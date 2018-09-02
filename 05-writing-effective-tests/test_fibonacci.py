import pytest

import numpy as np

from fibonacci import fib, fib_numpy


def test_fib_10():
    a = fib(10)
    assert len(a) == 10
    assert a == [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]


def test_fib_numpy_10():
    a = fib_numpy(10)
    assert len(a) == 10
    assert np.allclose(a, [1, 1, 2, 3, 5, 8, 13, 21, 34, 55])


@pytest.mark.parametrize("f_fib", (fib, fib_numpy))
def test_random_fib(f_fib):
    n = np.random.randint(1, 1000)
    a = f_fib(n)
    n2 = np.random.randint(3, n)
    assert a[n2] == a[n2-1] + a[n2-2]
