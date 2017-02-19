#!/usr/bin/env python3
# Pollard's rho algorithm

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def pollard_rho(n, s = 2, f = (lambda x, m: (x**2 - 1) % m)):
    x = y = s
    d = 1
    while d == 1:
        x = f(x, n)
        y = f(f(y, n), n)
        d = gcd(abs(y - x), n)
    return d

if __name__ == "__main__":
    import sys

    n = 312598451
    if len(sys.argv) > 1:
        n = int(sys.argv[1])

    print(pollard_rho(n))

