""" Implements newtons iterative method to find roots of mathematical functions """

TOLERANCE = 1e-8

def approx_eq(x, y, tolerance=TOLERANCE):
    return abs(x - y) <= tolerance

def approx_derivative(f, x, delta=1e-5):
    df = f(x + delta) - f(x)
    return df / delta

def newton_update(f):
    def update(x):
        return x - f(x) / approx_derivative(f, x)
    return update

def iter_improve(update, test, guess=1):
    while not test(guess):
        guess = update(guess)
    return guess

def find_root(f, initial_guess=1):
    def test(x):
        return approx_eq(f(x), 0)

    return iter_improve(update=newton_update(f), test,  initial_guess)

def square(x):
    return x * x

def square_root(a):
    return find_root(lambda x: pow(x, 2) - a)

def cube_root(a):
    return find_root(lambda x: pow(x, 3) - a)

def logarithm(a, base=2):
    return find_root(lambda x: pow(base, x) - a)

def golden_ratio():
    return find_root(lambda x: pow(x, 2) - x - 1)

print 'square root of {} is {}'.format(16, square_root(16))
print 'cube of {} is {}'.format(27, cube_root(27))
print 'logarithm of {} is {}'.format(32, logarithm(32))
print 'golden ratio is {}'.format(golden_ratio())
