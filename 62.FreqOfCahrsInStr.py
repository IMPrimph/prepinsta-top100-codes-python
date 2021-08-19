s = "prepinsta"
obj = {}

for char in s:
    if char in obj:
        obj[char] += 1
    else:
        obj[char] = 1

print(obj)
