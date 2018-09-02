import pytest

import numpy as np

from fibonacci import fib, fib_numpy


@pytest.mark.parametrize("f_fib", (fib, fib_numpy))
def test_random_fib(f_fib):
    n = np.random.randint(1, 1000)
    a = f_fib(n)
    n2 = np.random.randint(3, n)
    assert a[n2] == a[n2-1] + a[n2-2]
