num1 = int(input('Enter a starting number: '))
num2 = int(input('Enter a ending number: '))


def isPrime(num):
    for i in range(2, num // 2):
        if num % i == 0:
            return False
    return True


def retCount(num1, num2):
    res = 0
    for num in range(num1, num2 + 1):
        if isPrime(num):
            res += 1
    return res


print(retCount(num1, num2))
