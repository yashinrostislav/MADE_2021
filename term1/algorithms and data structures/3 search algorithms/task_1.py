def nearest(lowbound, x, n, arr1):
    if lowbound > n - 1:
        return arr1[lowbound - 1]
    elif abs(arr1[lowbound - 1] - x) <= abs(arr1[lowbound] - x):
        return arr1[lowbound - 1]
    else:
        return arr1[lowbound]


def lower_bound(x, n, arr1):
    l = -1
    r = n
    while l < r - 1:
        m = (l + r) // 2
        if x <= arr1[m]:
            r = m
        else:
            l = m
    return r


def main():
    n, k = map(int, input().split())
    arr1 = list(map(int, input().strip().split()))[:n]
    arr2 = list(map(int, input().strip().split()))[:k]
    for num in arr2:
        print(nearest(lower_bound(num, n, arr1), num, n, arr1))


if __name__ == '__main__':
    main()
