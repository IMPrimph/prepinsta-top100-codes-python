def binToDec(bin):
    decimal = 0
    base = 1

    while bin:
        res = bin % 10
        decimal = decimal + base * res
        bin //= 10
        base *= 2
    return decimal


print(binToDec(10101001))
