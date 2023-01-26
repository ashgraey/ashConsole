"""
[문제]
    아래 리스트에 랜덤숫자 (1~30) 을  10개 저장한다. 
    단, 홀수만 저장하고 , 중복숫자는 없어야 한다. 
[예시]
    a = [29, 1, 5, 9 , 21, 25, 7, 3, 13, 15]

"""
import random

# [1118]
# a = []

# # count = 0
# i = 0
# while True : 
#     if i == 10 :
#         break
    
#     r = random.randint(1, 30)
#     print(r, end = " ")

#     if r % 2 == 1 :
#         a.append(r)
#         i += 1 
# print()
# print(a)

# # 중복검사부분을 못품
# idx = 1
# for i in range(len(a) - 1) :
#     if a[i] == a[idx] :
#         a[i] += 2
#     idx += 1 
# print(a)

# [정답]
# # b배열을 생성 
# # 1 ~ 30중 홀수만 b배열에 저장
# # b배열 셔플
# # b배열에서 a에 10개만 저장
# a = []
# b = []
# i = 1
# while i <= 30:
#     if i % 2 == 1:
#         b.append(i)
#     i += 1
# print(b)

# i = 0
# while i < 10000:
#     r = random.randint(0, 14)
#     temp = b[0]
#     b[0] = b[r]
#     b[r] = temp
#     i += 1
# print(b)

# for i in range(10):
#     a.append(b[i])
# print(a)
