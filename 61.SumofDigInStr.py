s = "4PREP2INSTA6"
res = 0

for char in s:
    if char >= '0' and char <= '9':
        res += ord(char) - ord('0')

print(res)
