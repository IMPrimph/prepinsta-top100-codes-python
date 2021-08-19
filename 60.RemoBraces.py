s = "(a+b)=c"

res = ""
braces = ["[", "]", "(", ")", "{", "}"]

for char in s:
    if char in braces:
        continue
    else:
        res += char

print(res)
