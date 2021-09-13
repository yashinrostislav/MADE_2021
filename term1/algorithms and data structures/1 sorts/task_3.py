def merge(lst_1, lst_2):
    lst_res = []
    i1 = 0
    i2 = 0
    count = 0
    for i in range(len(lst_1) + len(lst_2)):
        if i1 < len(lst_1) and i2 < len(lst_2):
            if lst_1[i1] <= lst_2[i2]:
                lst_res.append(lst_1[i1])
                i1 += 1
            else:
                lst_res.append(lst_2[i2])
                i2 += 1
                count += len(lst_1) - i1
        else:
            if i1 == len(lst_1):
                for i2 in range(i2, len(lst_2)):
                    lst_res.append(lst_2[i2])
                    i2 += 1
            else:
                for i1 in range(i1, len(lst_1)):
                    lst_res.append(lst_1[i1])
                    i1 += 1
    return lst_res, count


def merge_sort(lst):
    if len(lst) < 2:
        return lst, 0
    else:
        mid = len(lst) // 2
        lst_1, a = merge_sort(lst[:mid])
        lst_2, b = merge_sort(lst[mid:])
        result, c = merge(lst_1, lst_2)
    return result, a + b + c


def main():
    """merge sort"""
    _ = int(input())
    input_lst = list(map(int, input().strip().split()))
    print(merge_sort(input_lst)[1])


if __name__ == '__main__':
    main()
