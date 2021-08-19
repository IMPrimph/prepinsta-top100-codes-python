num = int(input('Enter a number: '))


def isPerfect(num):
    res = []
    for i in range(1, num):
        if num % i == 0:
            res.append(i)
    return sum(res) == num


print(isPerfect(num))
