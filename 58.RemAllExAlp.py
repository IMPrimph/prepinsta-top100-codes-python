s = "*1prep_insta*"

res = ""

for char in s:
    if ord(char) > 64 and ord(char) < 90 or ord(char) > 96 and ord(char) < 123:
        res += char

print(res)
