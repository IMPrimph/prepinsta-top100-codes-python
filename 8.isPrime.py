num = int(input('Enter a number: '))


def isPrime(num):
    for i in range(2, num // 2):
        if num % i == 0:
            return False
    return True


print(isPrime(num))
