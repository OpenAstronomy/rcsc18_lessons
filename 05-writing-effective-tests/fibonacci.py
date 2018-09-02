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
