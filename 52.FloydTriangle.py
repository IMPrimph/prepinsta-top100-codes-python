temp = 64

for i in range(1, 6):
    for j in range(i):
        temp += 1
        print(chr(temp), end=" ")
    print()
