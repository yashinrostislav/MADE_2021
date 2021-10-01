from sys import stdin


def lower_bound(x):
    l = -1
    r = n
    while l < r - 1:
        m = (l + r) // 2
        if x <= arr1[m]:
            r = m
        else:
            l = m
    return r


arr1 = []
arr2 = []
n = int(stdin.readline())
arr1 = [int(x) for x in stdin.readline().rstrip().split()]
k = int(stdin.readline())
for i in range(k):
    arr2.append(list(map(int, stdin.readline().rstrip().split()))[:2])
arr1.sort()
for i in range(k):
    print(lower_bound(arr2[i][1] + 1) - lower_bound(arr2[i][0]))