def lsd_sort(arr, lvl, m):
    """returns lsd-sorted list"""
    arr_buff = []
    for t in range(lvl):
        for j in range(27):
            for i in range(len(arr)):
                if ord(arr[i][m - t - 1]) - ord('a') == j:
                    arr_buff.append(arr[i])
        arr = arr_buff
        arr_buff = []
    return arr


def main():
    n, m, k = map(int, input().split())
    arr = []
    for i in range(n):
        arr.append(input())

    for s in lsd_sort(arr, k, m):
        print(s)


if __name__ == '__main__':
    main()
