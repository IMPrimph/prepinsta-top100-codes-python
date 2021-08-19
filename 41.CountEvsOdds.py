arr = [1, 2, 3, 4, 5]

odds = 0
evens = 0

for num in arr:
    if num % 2 == 0:
        evens += 1
    else:
        odds += 1

print('Evens', evens, 'Odds', odds)
