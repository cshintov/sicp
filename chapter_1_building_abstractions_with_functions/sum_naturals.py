def sum_naturals(n):
    """ Compute the sum of n natural numbers """
    if n < 2 :
        return n

    return n + sum_naturals(n - 1)


def test_func(func, inp, expected):
    assert func(inp) == expected, func(inp)


def test(func):
    test_data = [(0, 0), (1, 1), (9, 45), (10, 55)]
    for inp, exp in test_data:
        test_func(func, inp, exp)


test(sum_naturals)
