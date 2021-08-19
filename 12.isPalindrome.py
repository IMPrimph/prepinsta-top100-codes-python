num = int(input('Enter a number: '))


def isPal(num):
    givenNum = num
    rev = 0

    while num:
        rem = num % 10
        rev = rev * 10 + rem
        num //= 10
    return givenNum == rev


print(isPal(num))
