base = int(input('Enter base number: '))
power = int(input('Enter power of the number: '))

res = 1

for i in range(0, power):
    res = res * base

print(res)
