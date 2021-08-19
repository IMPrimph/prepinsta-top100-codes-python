first = int(input('Enter first number: '))
second = int(input('Enter second number: '))
third = int(input('Enter third number: '))


def retHighest(first, second, third):
    if first > second and first > third:
        return first
    elif second > third:
        return second
    return third


print(retHighest(first, second, third))
