vowels = ['a', 'e', 'i', 'o', 'u']
s = "PREPINSTA"

res = 0

for char in s:
    if char.lower() in vowels:
        res += 1

print(res)
