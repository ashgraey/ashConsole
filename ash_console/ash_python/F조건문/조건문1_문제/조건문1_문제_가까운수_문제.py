'''
    [문제]		  
        a는 1~9 사이의 랜덤 숫자를 저장한다.
        c는 11~20 사이의 랜덤 숫자를 저장한다. 
        a와 c 중 어떤 숫자가 b와 더 가까운지 출력하시오.

        [1] a가 b보다 가까우면 "a가 가깝다."
        [2] c가 a보다 가까우면 "c가 가깝다."
        [3] 서로 거리가 같으면 "서로 같다."
'''
# if 조건문은 조건이 True일때만 실행된다.
import random

b = 10
a = random.randint(1, 9)
c = random.randint(11, 20)
print("a =", a)
print("c =", c)

a차이 = b - a
c차이 = c - b
print("a차이 =",  a차이)
print("c차이 =",  c차이)

if a차이 < 0 :
    a차이 = -a차이
    print(a차이)
if c차이 < 0 :
    c차이 = -c차이
    print(c차이)

if a차이 > c차이 :
    print("c가 가깝다") 
if c차이 > a차이 :
    print("a가 가깝다")
if a차이 == c차이 :
    print("서로 같다")




# import random


# a = 0
# c = 0

# b = 10

# a = random.randint(1, 9)
# c = random.randint(11, 20)
# print(a, end = " ")
# print(b, end = " ")
# print(c)

# a_b = b - a 
# b_c = c - b
# if a_b > b_c : 
#     print("c가 가깝다")
# if a_b < b_c :
#     print("a가 가깝다")
# if a_b == b_c :
#     print("서로 같다.") 

# [answer]
# import random

# a = random.randint(1, 9)
# c = random.randint(11, 20)
# print("a =", a)
# print("c =", c)

# b = 10

# # 각각 차이의 값을 나타냄
# # 음수일 경우 양수로 변환
# a차이 = b - a
# if a차이 < 0:
#     a차이 = -a차이
# print(a차이)

# c차이 = b - c
# if c차이 < 0:
#     c차이 = -c차이
# print(c차이)

# # 값을 비교하여 결과를 나타냄
# if a차이 < c차이:
#     print("a가 가깝다.")
# if c차이 < a차이: 
#     print("c가 가깝다.")
# if a차이 == c차이:
#     print("서로 같다.")
