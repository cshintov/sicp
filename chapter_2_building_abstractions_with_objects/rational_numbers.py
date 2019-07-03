""" 
Chapter 2: Building abstractions with objects

http://www-inst.eecs.berkeley.edu/~cs61a/sp12/book/objects.html#id6
"""

from operator import getitem
from fractions import gcd

def add_rat(x, y):
    nx, dx = numer(x), denom(x)
    ny, dy = numer(y), denom(y)
    return make_rat(nx * dy + dx * ny, dx * dy)

def mul_rat(x, y):
    nx, dx = numer(x), denom(x)
    ny, dy = numer(y), denom(y)
    return make_rat(nx * ny, dx * dy)

def eq_rat(x, y):
    nx, dx = numer(x), denom(x)
    ny, dy = numer(y), denom(y)
    return nx * dy == dx * ny

def make_rat(n, d):
    g = gcd(n, d)
    return (n / g, d / g)

def numer(x):
    return getitem(x, 0)

def denom(x):
    return getitem(x, 1)

def str_rat(x):
    """Return a string 'n/d' for numerator n and denominator d."""
    return '{0}/{1}'.format(numer(x), denom(x))
