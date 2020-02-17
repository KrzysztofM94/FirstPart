#Basic
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

# for i in a:
#     if(i < 5):
#         print(i)

# 1
# newList = []
# for i in a:
#     if(i < 5):
#         newList.insert(i)
# print(newList)

# 2
number = []
number=[number for number in a if number<5]
print(number)
# 3

# num = int(input("Give me a number: "))
# newList3 = []
# for i in a:
#     if(i < num):
#         newList3.append(i)
# print(newList3)