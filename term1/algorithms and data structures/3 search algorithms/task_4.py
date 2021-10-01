def func(length_):
    count = 0
    if length_ == 0:
        return 0
    for a in arr:
        count += a // length_
    return (count)


def bin_search(y, l, r):
    while not r - l <= 1:
        m = (l + r) // 2
        if func(m) < y:
            r = m
        else:
            l = m
    if func(l) == func(r):
        return r
    else:
        return l


arr = []

n, k = map(int, input().split())
for i in range(n):
    arr.append(int(input()))

arr.sort()
left = 0
right = arr[n - 1]

print(bin_search(k, left, right))
