arr = list((map(int, input().split(" "))))

minEl = arr[0]

for i in range(1, len(arr)):
    if arr[i] < minEl:
        minEl = arr[i]

print(minEl)
