# 1
# for i in range(0, 5):
#     for j in range(i + 1):
#         print("*", end=" ")
#     print("")

# # # # # # # # # # # # # # # # # # # # #  2
# for i in range(0, 5):
#     for j in range(2 * i + 1):
#         print("*", end=" ")
#     print()

# # # # # # # # # # # # # # # # # # # # #  3
# for i in range(1, 6):
#     for j in range(1, 6):
#         if j >= 6 - i:
#             print("*", end=" ")
#         else:
#             print(" ", end=" ")
#     print()

for i in range(1, 6):
    for j in range(1, 10):
        if j >= 6 - i and j <= 4 + i:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()
