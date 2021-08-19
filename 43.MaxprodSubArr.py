arr = [-1, -3, -10, 60, 0]

currMax = 1
currMin = 1
res = max(arr)

for num in arr:
    if num == 0:
        currMax = 1
        currMin = 1
    else:
        temp = num * currMax
        currMax = max(temp, num * currMin, num)
        currMin = min(temp, num * currMin, num)
        res = max(res, currMax)

print(res)
