first = int(input("Enter first number: "))
second = int(input("Enter last number: "))


def calclSum(first, second):
    res = 0
    for i in range(first, second + 1):
        res += i
    return res


print(calclSum(first, second))
