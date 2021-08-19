arr = list(map(int, input().split(" ")))

large = arr[0]
small = arr[0]

for i in range(1, len(arr)):
    if arr[i] < small:
        small = arr[i]
    if arr[i] > large:
        large = arr[i]

print('Smallest', small, 'Largest', large)
