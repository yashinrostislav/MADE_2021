def time(x):
    t_p = (((1 - a) ** 2 + x ** 2) ** (1 / 2)) / v_p
    t_f = (((1 - x) ** 2 + a ** 2) ** (1 / 2)) / v_f
    t = t_p + t_f
    return t


def ternary_search(l, r):
    for i in range(100):
        m1 = (l * 2 + r) / 3
        m2 = (l + r * 2) / 3
        if time(m1) < time(m2):
            r = m2
        else:
            l = m1
    return r


v_p, v_f = map(int, input().split())
a = float(input())
print(ternary_search(0, 1))
