import random
def nambers_0():
    nabers = [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
    nabers_1 = random.choice(nabers)
    return nabers_1
nabers_1 = nambers_0()
print(nabers_1)
# # Работа с рандомным числом готова
#
# count = 1
# del_ = []
# while count < nabers_1:
#     if nabers_1 % count == 0:
#         del_.append(count)
#     count += 1
# del_.append(nabers_1)
# print(del_)
# # целые делители
#
# result = []
# for k in del_:
#     for i in range(1, 20):
#         for j in range(1, 20):
#             if i == j:
#                 continue
#             if i + j == k:
#                 result += [i, j]
# print(result)


password = ''
for i in range(1, nabers_1 + 1):
    for j in range (i+1,nabers_1 + 1):
        if nabers_1 % (i + j) == 0:
            password += str(i)
            password += str(j)
print(password)