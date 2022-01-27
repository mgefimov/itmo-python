def fib(n):
    if n < 2:
        return n
    return fib(n - 1) + fib(n - 2)


if __name__ == '__main__':
    assert fib(0) == 0
    assert fib(1) == 1
    assert fib(2) == 1
    assert fib(10) == 55
