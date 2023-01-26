'''
    [문제]
        1~10 사이의 랜덤 숫자 3개 저장하고
        그 숫자의 합이 무조건 20이 되도록 출력해보자.
'''
'''
반복의 횟수를 모르기때문에 무한반복 

'''
# [3차-1111]
# import random

# total = 0

# while True :
#     r1 = random.randint(1, 10)
#     r2 = random.randint(1, 10)
#     r3 = random.randint(1, 10)
#     total = r1 + r2 + r3
    
#     if total == 20 :
#         print(r1, r2, r3, " =", total)
#         break

# [2차]
# import random
# x = 0
# y = 0
# z = 0

# run = 1 
# while run == 1 :
#     x = random.randint(1, 10)
#     y = random.randint(1, 10)
#     z = random.randint(1, 10)
#     # print("x =", x)
#     # print("y =", y)
#     # print("z =", z)

#     total = x + y + z
#     if total == 20 :
#         run = 0

# print()
# print(x, y, z, " =", total)    

# [1차]
# import random

# total = 0
# i = 0
# while i < 3 :
#     num = random.randint(1, 10)
#     print(num, end = " ")
#     total += num

#     if total == 20 :
#          print("합은 20 =", total)
    
#     i += 1

