num = int(input('Enter a number: '))


def reverseMe(num):
    rev = 0
    while num:
        rem = num % 10
        rev = rev * 10 + rem
        num //= 10
    return rev


print(reverseMe(num))
