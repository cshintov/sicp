def percent_diff(x, y):
    """ Returns the difference as a percentage of the first """
    diff = abs(x - y)
    return 100 * diff / x


print percent_diff(7.5, 10)
print percent_diff(7.5, 12)
print percent_diff(7.5, 15)
print percent_diff(7.5, 18)
print percent_diff(7.5, 22.5)
