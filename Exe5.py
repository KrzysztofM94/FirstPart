import random

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

c = []

# c = [c for i,c in enumerate(b) if b[i] in a]
# print(c)

#[1, 2, 3, 5, 8, 13]

# for i in b:
#     if b[i-1] in a:
#         c.append(b[i-1])
#
# print(c)

# for i in b:
#     if i in a:
#         c.append(i)
#
# print(c)

# 1
# num1 = random.randrange(1, 50)
# list1 = [random.randrange(1, 50) for i in range(num1)]
# num1 = random.randrange(1, 50)
# list2 = [random.randrange(1, 50) for i in range(num1)]
#
# if list1.__sizeof__() > list2.__sizeof__():
#
#     for j,i in enumerate(list1):
#         if list1[j - 1] in list2:
#             c.append(list1[j - 1])
# else:
#     for j,i in enumerate(list1):
#         if list2[j - 1] in list1:
#             c.append(list2[j - 1])
#
# print(c)
