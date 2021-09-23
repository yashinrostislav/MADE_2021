def count_sort(arr):
    """returns count-sotred list"""
    arr2 = []
    for i in range(0, 101):
        arr2.append(0)

    for i in arr:
        arr2[i] += 1
    arr = []

    for i in range(0, 101):
        for j in range(arr2[i]):
            arr.append(i)
    return arr


def main():
    arr = map(int, input().split())
    print(' '.join(map(str, count_sort(arr))))


if __name__ == '__main__':
    main()
