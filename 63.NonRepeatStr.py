s = "prepinsta"

obj = {}

for char in s:
    if char in obj:
        obj[char] += 1
    else:
        obj[char] = 1


for k, val in obj.items():
    if obj[k] == 1:
        print(k, end="")
