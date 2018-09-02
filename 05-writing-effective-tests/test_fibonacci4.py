import pytest

import numpy as np

from fibonacci import fib, fib_numpy, fib_3, fib_recursive


@pytest.mark.parametrize("f_fib", (fib, fib_numpy, fib_3))
def test_random_fib(f_fib):
    n = np.random.randint(1, 1000)
    a = f_fib(n)
    n2 = np.random.randint(3, n)
    assert a[n2] == a[n2-1] + a[n2-2]


def test_recursion_error():
    with pytest.raises(RecursionError):
        fib_recursive(0)
