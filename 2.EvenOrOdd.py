num = int(input("Enter a number: "))


def check(num):
    return "Even" if num % 2 == 0 else 'Odd'


print(check(num))
