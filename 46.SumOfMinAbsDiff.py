arr = [2, 3, 9, 5, 6]

median = sorted(arr)[len(arr) // 2]

res = 0

for num in arr:
    res += abs(median - num)

print(res)
