arr = list(map(int, input().split(" ")))

res = 0

for i in range(0, len(arr)):
    res += arr[i]

print(res)