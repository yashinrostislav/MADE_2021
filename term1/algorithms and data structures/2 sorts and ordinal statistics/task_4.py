def enough(arr1, arr2):
    for a, b in zip(arr1, arr2):
        if a < b:
            return False
    return True


def ord_letter(letter):
    return ord(letter) - ord('a')


def brain_explosion(string, cards):
    crd_cnt = [0] * 26
    for c in cards:
        crd_cnt[ord_letter(c)] += 1
    ans = left = right = 0
    moved_right = True
    tmp_count = [0] * 26
    while right < len(string):
        if moved_right:
            rgt = string[right]
            tmp_count[ord_letter(rgt)] += 1
        if not enough(crd_cnt, tmp_count):
            lft = string[left]
            tmp_count[ord_letter(lft)] -= 1
            left += 1
            moved_right = False
            continue
        ans += right - left + 1
        right += 1
        moved_right = True
    return ans


def main():
    n, m = map(int, input().split())
    string_ = input()
    cards_ = input()
    print(brain_explosion(string_, cards_))


if __name__ == '__main__':
    main()
