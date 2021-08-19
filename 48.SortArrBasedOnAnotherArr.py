arr1 = [26, 21, 11, 20, 50, 34, 1, 18]
arr2 = [21, 11, 26, 20]

obj = {}
res, nums = [], []

for num in arr2:
    obj[num] = 0

for num in arr1:
    if num not in obj:
        nums.append(num)
    else:
        obj[num] += 1

for key, val in obj.items():
    res.extend([key for _ in range(val)])

res.extend(sorted(nums))
print(res)
