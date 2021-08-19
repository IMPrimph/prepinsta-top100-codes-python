s = "PREPINSTA"
vowels = ['a', 'e', 'i', 'o', 'u']

res = ""

for char in s:
    if char.lower() in vowels:
        continue
    else:
        res += char

print(res)
