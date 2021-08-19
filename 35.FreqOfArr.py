res = {}
arr = [4, 33, 199, 9, 33, 199]

for num in arr:
    if num in res:
        res[num] += 1
    else:
        res[num] = 1

print(res)
