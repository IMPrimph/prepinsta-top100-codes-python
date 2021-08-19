arr = [454, 22, 1, 5665, 3321]

arr.sort(reverse=True)

for num in arr:
    if str(num) == str(num)[::-1]:
        print(num)
