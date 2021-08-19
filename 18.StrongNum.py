num = int(input("Enter a number: "))


def fact(num):
    res = 1
    for i in range(1, num + 1):
        res = res * i
    return res


def isStrongNum(num):
    res = 0
    givenNum = num
    while num:
        rem = num % 10
        temp = fact(rem)
        res += temp
        num //= 10
    print(res)
    return


isStrongNum(num)
