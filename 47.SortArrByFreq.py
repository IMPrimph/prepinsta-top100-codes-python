arr = [2, 3, 2, 5, 6, 2, 3, 9, 5, 6]

obj = {}


for num in arr:
    if num in obj:
        obj[num] += 1
    else:
        obj[num] = 1

arr.sort(key=lambda x: (obj[x], -x))
print(arr)
