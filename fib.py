from pprint import pprint
def ifib(n):
    """ Compute the nth fibonacci number where n >= 2 """
    if n < 2:
        return n

    curr, pred = 0, 1

    k = 0
    while k < n:
        pred, curr = curr, pred + curr
        k = k + 1

    return curr


def rfib(n, mem={}):
    """ Compute the nth fibonacci number where n >= 2 """
    if n < 2:
        return n

    if not n in mem:
        mem[n] = rfib(n - 1) + rfib(n - 2)

    return mem[n]


def test_func(func, inp, expected):
    assert func(inp) == expected, func(inp)


def test_fib():
    test_data = [(0, 0), (1, 1), (2, 1), (3, 2), (4, 3), (5, 5), (6, 8), (7, 13), (50, 12586269025), (49, 7778742049)]
    for inp, exp in test_data:
        test_func(rfib, inp, exp)
