def roman2arabic(roman):
    """convetring roman numbers to arabic"""
    vocab = {"I": 1, "V": 5, "X": 10, "L": 50}
    arabic = vocab[roman[len(roman) - 1]]
    for d in range(len(roman) - 1):
        if vocab[roman[d]] < vocab[roman[d + 1]]:
            arabic -= vocab[roman[d]]
        else:
            arabic += vocab[roman[d]]
    return arabic


def arabic2roman(arabic):
    """convetring arabic numbers to roman"""
    vocab = {50: "L", 40: "XL", 10: "X", 9: "IX", 5: "V", 4: "IV", 1: "I"}
    roman = ''
    while arabic > 0:
        for i in list(vocab.keys()):
            while i <= arabic:
                roman += vocab[i]
                arabic -= i
    return roman


def merge(arr1, arr2):
    arr_res = []
    i1 = 0
    i2 = 0
    for _ in range(len(arr1) + len(arr2)):
        if i1 < len(arr1) and i2 < len(arr2):
            if arr1[i1] <= arr2[i2]:
                arr_res.append(arr1[i1])
                i1 += 1
            else:
                arr_res.append(arr2[i2])
                i2 += 1
        else:
            if i1 == len(arr1):
                for i2 in range(i2, len(arr2)):
                    arr_res.append(arr2[i2])
                    i2 += 1
            else:
                for i1 in range(i1, len(arr1)):
                    arr_res.append(arr1[i1])
                    i1 += 1
    return arr_res


def merge_sort(list_to_sort):
    """returns merge-sorted list"""
    if len(list_to_sort) < 2:
        return list_to_sort
    else:
        mid = len(list_to_sort) // 2
        arr1 = list_to_sort[:mid]
        arr2 = list_to_sort[mid:]
    return merge(merge_sort(arr1), merge_sort(arr2))


arr = []
n = int(input())
for i in range(n):
    arr.append((input().strip().split()))
    arr[i][1] = roman2arabic(arr[i][1])
arr_sorted = merge_sort(arr)

for i in range(len(arr)):
    arr_sorted[i][1] = arabic2roman(arr_sorted[i][1])

for row in arr_sorted:
    for elem in row:
        print(elem, end=' ')
    print()
