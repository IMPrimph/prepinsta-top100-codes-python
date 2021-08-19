num = int(input('Enter a number: '))


def isArmstrong(num):
    givenNum = num
    genNum = 0
    while num:
        rem = num % 10
        genNum += rem ** 3
        num //= 10
    return genNum == givenNum


print(isArmstrong(num))
