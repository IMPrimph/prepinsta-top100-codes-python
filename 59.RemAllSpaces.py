s = "PREP          INSTA"
res = ""

for char in s:
    if char == " ":
        continue
    else:
        res += char

print(res)
