s = "hello, world"
cnt = 0

# for char in s:
#     cnt += 1

# print(cnt)

i = 0
while True:
    try:
        s[i]
        i += 1
        cnt += 1
    except IndexError:
        print(cnt)
        break
