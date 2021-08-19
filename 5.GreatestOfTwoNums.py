first = int(input('Enter first number'))
second = int(input('Enter second number'))


def retHighest(first, second):
    return first if first > second else second


print(retHighest(first, second))
