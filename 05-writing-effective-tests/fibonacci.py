import numpy as np


def fib(n):
    fib = [0, 1]
    while len(fib) < n+1:
        fib.append(fib[-2] + fib[-1])
    return fib[1:]


def fib_numpy(n):
    fib = np.zeros(n+1)
    fib[1] = 1
    for i in range(2, n+1):
        fib[i] = fib[i-2] + fib[i-1]
    return fib[1:]


def fib_recursive(n):
    if n == 1 or n == 2:
        return 1
    return fib_recursive(n-1) + fib_recursive(n-2)


def fib_3(n):
    return [fib_recursive(i) for i in range(1, n)]
