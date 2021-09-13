def main():
    """bubble sort"""
    n = int(input())
    lst = list(map(int, input().strip().split()))[:n]
    for i in range(n - 1):
        for j in range(n - i - 1):
            if lst[j] > lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
    ans = ' '.join(map(str, lst))
    print(ans)


if __name__ == '__main__':
    main()
