def bubble_sort(lst, n):
    """returns bubble-sorted list"""
    for i in range(n - 1):
        for j in range(n - i - 1):
            if lst[j] > lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
    return lst

    ans = ' '.join(map(str, lst))
    print(ans)


def main():
    n = int(input())
    lst = list(map(int, input().split()))
    ans = ' '.join(map(str, bubble_sort(lst, n)))
    print(ans)


if __name__ == '__main__':
    main()
