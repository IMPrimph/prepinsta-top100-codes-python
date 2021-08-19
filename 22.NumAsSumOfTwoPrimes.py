def isPrime(num):
    for i in range(2, num // 2):
        if num % i == 0:
            return False
    return True


def calc(num):
    for i in range(2, num):
        if isPrime(i) and isPrime(num - i):
            print(i, num - i)


calc(30)
