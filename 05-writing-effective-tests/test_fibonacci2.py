import numpy as np


def test_fib_10(f_fib):
    "Test a Fibonacci function f_fib for correct values given a random input"
    n = np.random.randint(1, 1000)
    a = f_fib(n)
    n2 = np.random.randint(3, n)
    assert a[n2] == a[n2-1] + a[n2-2]
