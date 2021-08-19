arr = list(map(int, input().split(" ")))

first = float('inf')
second = float('inf')

for i in range(0, len(arr)):
    if arr[i] < first:
        second = first
        first = arr[i]
    if arr[i] < second and arr[i] != first:
        second = arr[i]

print(second)
