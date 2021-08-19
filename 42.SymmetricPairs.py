arr = [[11, 20], [30, 40], [5, 10], [40, 30], [10, 5]]

for [a, b] in arr:
    if [b, a] in arr:
        print([a, b])
