num = int(input('Enter a number: '))


def returnSum(num):
    res = 0
    while num:
        res += num % 10
        num //= 10
    return res


print(returnSum(num))
