arr = [5, 6, 20, 100, 4, 1]

arr2 = arr.copy()
arr3 = arr.copy()

for i in range(0, len(arr)):
    for j in range(1, len(arr)):
        if arr3[j] > arr3[j - 1]:
            arr3[j], arr3[j - 1] = arr3[j - 1], arr3[j]

for i in range(0, len(arr)):
    for j in range(1, len(arr)):
        if arr2[j] < arr2[j - 1]:
            arr2[j], arr2[j - 1] = arr2[j - 1], arr2[j]

print('Ascending', arr2)
print('Descending', arr3)
