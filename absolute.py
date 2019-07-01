def absolute(x):
    """ Returns the absolute value of x """
    return -x if x < 0 else x


assert absolute(0) == 0
assert absolute(-1) == 1
assert absolute(1) == 1
