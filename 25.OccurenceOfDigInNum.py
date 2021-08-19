
def cnt(num, dig):
    res = 0
    while num:
        k = num % 10
        num //= 10
        if k == dig:
            res += 1
    return res


print(cnt(89998, 9))
