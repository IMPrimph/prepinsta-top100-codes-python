arr = [12, 34, 56, 21, 100, 3, 1, 5]

for i in range(0, len(arr) // 2):
    for j in range(1, len(arr) // 2):
        if arr[j] < arr[j - 1]:
            arr[j], arr[j - 1] = arr[j - 1], arr[j]

for i in range(len(arr) // 2, len(arr)):
    for j in range(len(arr) // 2, len(arr)):
        if arr[j] > arr[j - 1]:
            arr[j], arr[j - 1] = arr[j - 1], arr[j]

print(arr)
