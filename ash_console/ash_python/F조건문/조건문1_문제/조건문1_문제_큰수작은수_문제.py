'''
    [문제]
        1부터 10 사이의 랜덤 숫자 두 개를 출력한다.
        하나는 반드시 1~5 사이의 숫자이어야 하고,
        나머지 하나는 반드시 6~10 사이의 숫자이어야 한다.
        출력순서도 랜덤으로 출력되어야 한다. 

        [예1]
            3, 6
        [예2]
            8, 1
'''
'''
문제 이해를 잘 못한 유형
위치를 지정해주면 해결됨
'''

import random

num1 = random.randint(1, 5)
num2 = random.randint(6, 10)
# print("num1 =", num1)
# print("num2 =", num2)

# 랜덤 수치를 바꿨으므로 이 조건은 필요없음
# if num1 >= 1 and num1 <= 5 :
#     print("num1 =", num1)

# if num2 >= 6 and num2 <= 10 :
#     print("num2 =", num2)

position = random.randint(0,1)
print("랜덤 위치 =", position)
if position == 0 :
    print(num1, num2)
if position == 1 :
    print(num2, num1)







# num1 = random.randint(1, 5)
# num2 = random.randint(6, 10)
# print(num1, num2)

# # if num1 <= 5 :
# #     print(num1)
# #     if num2 <= 5 : 
# #         print(num2)

# # if num1 > 5 :
# #     print(num1)
# #     if num2 > 5 :
# #         print(num2)

# position = random.randint(1, 2)
# print(position)

# if position == 1:
#     print(num1, num2)
# if position == 2:
#     print(num2, num1)

# [answer]
# import random

# num1 = random.randint(1, 5)
# num2 = random.randint(6, 10)

# position = random.randint(1, 2)
# print(position)

# if position == 1:
#     print(num1, num2)
# if position == 2:
#     print(num2, num1)


