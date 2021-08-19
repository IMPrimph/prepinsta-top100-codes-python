arr = [4, -3, 0, 2, -7, 1, 5]

res = sum(arr)
leftSum = 0

for i in range(0, len(arr)):
    right = res - leftSum - arr[i]
    if leftSum == right:
        print(i)
    else:
        leftSum += arr[i]
