def num(time, n_rem):
    n_rem -= time // fast + time // slow
    if n_rem <= 0:
        return True
    return False


def bin_search(n_copys, left, right):
    if n_copys == 0:
        return 0
    else:
        while not right - left <= 1:
            mid = (right + left) // 2
            if num(mid, n_copys):
                right = mid
            else:
                left = mid
        return right


n, x, y = map(int, input().split())
fast = min(x, y)
slow = max(x, y)

time_max = (n * slow)
time_0 = fast

print(bin_search(n - 1, 0, time_max) + time_0)
