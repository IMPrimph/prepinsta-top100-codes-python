# for i in range(5, 0, -1):
#     for j in range(1, i + 1):
#         print(j, end=" ")
#     print()

for i in range(1, 5):
    temp = 1
    for j in range(1, 8):
        if j >= 5 - i and j <= 3 + i:
            print(temp, end=" ")
            if j < 4:
                temp += 1
            else:
                temp -= 1
        else:
            print(" ", end=" ")
    print()
