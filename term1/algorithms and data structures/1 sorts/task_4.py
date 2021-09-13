import random


def quick_sort(arr):
    """quick sort"""
    if len(arr) < 2:
        return arr
    base = random.choice(arr)
    lower, equal, upper = [], [], []
    for a in arr:
        if a < base:
            lower.append(a)
        elif a == base:
            equal.append(a)
        else:
            upper.append(a)
    return quick_sort(lower) + equal + quick_sort(upper)


if __name__ == '__main__':
    _ = int(input())
    inpt_list = list(map(int, input().strip().split()))
    arr_sorted = quick_sort(inpt_list)
    ans = ' '.join(map(str, arr_sorted))
    print(ans)
