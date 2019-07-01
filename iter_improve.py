""" implements iterative improvement algorithm """
TOLERANCE = 1e-8

def square(x):
    return x ** 2

def successor(x):
    return x + 1

def const(num):
    return lambda x: num

def near(x, f, g):
    return approx_eq(f(x), g(x))

def approx_eq(x, y, tolerance=TOLERANCE):
    return abs(x - y) <= tolerance

def iter_improve(update, test, guess=1):
    while not test(guess):
        guess = update(guess)

    return guess

def square_root(num):
    return iter_improve(
            update=lambda x: (x / 2.0) + (num / (2.0 * x)),
            test=lambda x: near(x, f=square, g=const(num))
        )

def golden_ratio():
    def golden_update(guess):
        return 1.0 / guess + 1

    def golden_test(guess):
        return near(guess, square, successor)

    return iter_improve(golden_update, golden_test)

print('%.20f' % golden_ratio()) 

def test_square_root():
    assert square_root(4) - 2 < TOLERANCE
    assert square_root(9) - 3 < TOLERANCE
    assert square_root(16) - 4 < TOLERANCE
    assert square_root(100) - 10 < TOLERANCE
    assert square_root(1000) - 31.6227766017 < TOLERANCE

test_square_root()

# mathematical function composition
def compose(f, g):
    return lambda *args, **kwargs: f(g(*args, **kwargs))

add_one_and_square = compose(square, successor)
print add_one_and_square(12)
square_and_add_one= compose(successor, square)
print square_and_add_one(12)
