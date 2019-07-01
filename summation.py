def summation(start=1, end=1, term=lambda x: x, nxt=lambda x: x+1):
    total, k = 0, start

    while k <= end:
        total, k = total + term(k), nxt(k)

    return total

def sum_squares(n):
    return summation(end=n, term=lambda x: x ** 2)

def sum_cubes(n):
    return summation(end=n, term=lambda x: x ** 3)

def sum_pi(n):
    def term(x):
        denom = x * (x + 2)
        return 8.0 / denom

    return summation(
            end=n, 
            term=term,
            nxt=lambda x: x + 4
       )

print sum_pi(100)
print sum_pi(1e6)
