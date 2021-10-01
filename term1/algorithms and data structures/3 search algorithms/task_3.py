n = float(input())
R_ = 10.0 ** 10
L_ = 1.0
EPS = 10 ** -6


def func(x):
    return x ** 2 + x ** (1 / 2)


def bin_search(y, l, r):
    for i in range(100):
        m = (l + r) / 2
        if func(m) < y:
            l = m
        else:
            r = m
    return r


print(bin_search(n, L_, R_))
