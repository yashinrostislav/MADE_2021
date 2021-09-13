def merge(lst_1, lst_2):
    lst_res = []
    i1 = 0
    i2 = 0
    for i in range(len(lst_1) + len(lst_2)):
        if i1 < len(lst_1) and i2 < len(lst_2):
            if lst_1[i1] <= lst_2[i2]:
                lst_res.append(lst_1[i1])
                i1 += 1
            else:
                lst_res.append(lst_2[i2])
                i2 += 1
        else:
            if i1 == len(lst_1):
                for i2 in range(i2, len(lst_2)):
                    lst_res.append(lst_2[i2])
                    i2 += 1
            else:
                for i1 in range(i1, len(lst_1)):
                    lst_res.append(lst_1[i1])
                    i1 += 1
    return lst_res


def merge_sort(lst):
    if len(lst) < 2:
        return lst
    else:
        mid = len(lst) // 2
        lst_1 = lst[:mid]
        lst_2 = lst[mid:]
    return merge(merge_sort(lst_1), merge_sort(lst_2))


def main():
    """merge sort"""
    _ = int(input())
    input_lst = list(map(int, input().strip().split()))
    arr_sorted = merge_sort(input_lst)
    ans = ' '.join(map(str, arr_sorted))
    print(ans)


if __name__ == '__main__':
    main()
