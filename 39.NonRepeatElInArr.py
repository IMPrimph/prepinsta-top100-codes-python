arr = [1, 2, 5, 2, 6, 7, 5]

obj = {}
res = 0

for num in arr:
    if num in obj:
        obj[num] += 1
    else:
        obj[num] = 1

for val in obj:
    if obj[val] == 1:
        print(val)
