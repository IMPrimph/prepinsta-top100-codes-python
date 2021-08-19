# multiply by wither 2 or 3, check whether array can be made same

arr = [50, 75, 100]

for i in range(0, len(arr)):
    while arr[i] % 2 == 0:
        arr[i] /= 2

    while arr[i] % 3 == 0:
        arr[i] /= 3

print(arr)
