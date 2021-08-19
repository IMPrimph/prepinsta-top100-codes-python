s = "GuDDuBHaiyA"
res = ""

for char in s:
    if char.isupper():
        char = char.lower()
        res += char
    else:
        char = char.upper()
        res += char

print(res)
