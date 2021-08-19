num = int(input('Enter a number: '))


def fibs(num):
    n1, n2 = 0, 1
    print(n1, n2, end=" ")

    for i in range(2, num):
        n3 = n2 + n1
        n1 = n2
        n2 = n3
        print(n3, end=" ")


fibs(num)
