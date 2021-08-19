num1 = int(input('Enter first number: '))
num2 = int(input('Enter second number: '))

arr = []

if num1 > num2:
    smaller = num2
else:
    smaller = num1

for i in range(1, smaller + 1):
    if num1 % i == 0 and num2 % i == 0:
        arr.append(i)

print(max(arr))
