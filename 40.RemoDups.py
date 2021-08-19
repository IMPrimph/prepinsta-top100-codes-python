arr = [1, 2, 3, 4, 4]

res = []

for num in arr:
    if num in res:
        continue
    else:
        res.append(num)

print(res)
