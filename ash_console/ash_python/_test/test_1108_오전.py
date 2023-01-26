"""
    [문제]
        철수는 볼펜을 (10~30)개를 구입해야 한다. 
        
        볼펜 하나의 가격은 1200원이다. 	
        볼펜은 20개 이상 구매 시 볼펜 한 개에 100원을 할인해주고 있다. 
            
        또한, 회원 등급에 따라 할인을 추가 제공한다.
        
        회원 등급이 1이면  볼펜한개에 150원 할인 
        회원 등급이 2이면  볼펜한개에 50원 할인
        기본회원 등급은 3이고 할인을 제공하지 않는다.
        위 개수에따른 할인과 중복적용된다. 

        볼펜 수를 랜덤으로 저장한다.
        회원 등급을 랜덤으로 저장한다. 
        
        철수가 지급해야 하는 금액을 출력하시오.
        

    [예시]
        볼펜 10 , 회원등급1 => 1050 * 10
        볼펜 20 , 회원등급1 => 950 * 20
        볼펜 15 , 회원등급2 => 1150 * 15
        볼펜 20 , 회원등급2 => 1050 * 20

"""
print("---- 문제1 ----")

import random

볼펜 = random.randint(10, 30)
print("볼펜 =", 볼펜)
회원등급 = random.randint(1, 3)
print("회원등급 =", 회원등급)

볼펜가격 = 1200 
if 볼펜 >= 20 :
    볼펜가격 -= 100


if 회원등급 == 1 : 
    볼펜가격 -= 150 
if 회원등급 == 2 :
    볼펜가격 -= 50

금액 = 볼펜 * 볼펜가격
print("볼펜 금액 =", 금액)


"""
    [문제]
        50~100 사이의 랜덤값을 저장하고 그값의 약수를 전부 구하고, 
        그약수의 가운데 위치의 값만 출력한다. 
        만약에 약수의 개수가 짝수이면 가운데값 두개중 앞의 값을 출력한다. 
    [예시]
        50 => 1, 2, 5, 10, 25, 50 총 6개이므로 5 , 10 이 가운데 값들이고,  그 중 앞의 값 5를 출력한다. 
    [예시]
        51 => 1, 3, 17 총 3개 이므로 3만 출력한다. 
"""
print()
print("---- 문제2 ----")
import random 

# num = random.randint(50, 100)
num = 50
print("num =", num)


idx = 0
count = 0 
i = 1
while i <= num :
    if num % i == 0 : 
        count += 1
        print(i, end = " ")
   
    # if count % 2 == 0 :
    #     idx = count // 2 
    #     # print(i)
    i += 1 
print()
print("약수 개수 =", count)
center = 0 
if count % 2 == 0 :
    center = count // 2
if count % 2 == 1 :
    center = count // 2 + 1 

# 반복문을 한번 더 쓰는것이 핵심
# count2의 값이 center의 값과 같아지면 i(약수)를 출력
i = 1 
count2 = 0 
while i <= num :
    if num % i == 0 :
        count2 += 1 
        if count2 == center :
            print(i)
    i += 1 

# if count % 2 == 0 :

# print("--- 문제3 ---")
# count = 0

# r = random.randint(50, 100)
# print(r)

# i = 1
# mid = 0
# while i <= r:
#     # 랜덤값의 약수
#     if r % i == 0:
#         print(i, end = " ")
#         # 랜덤값의 개수
#         count += 1

#     i += 1
# print()
# print(count)

# i = 1
# # 카운트가 0이될때까지 반복
# while count >= 0:
   
#     # 카운트가 짝수일 경우
#     # 카운트 몫 - 1 => 중간 앞의 위치를 찾기
#     if count % 2 == 0:
#         count = (count // 2)

#         # 랜덤값의 약수
#         if r % i == 0:
#             count -= 1
#             mid = i
#             # print(mid)
    
#     # 카운트값이 홀수
#     if count % 2 == 1:
#         count = (count // 2) + 1
#         if r % i == 0:
#             count -= 1
#             mid = i
           
#     i += 1
# print(mid)

# print('--- 문제4 ---')

# num = random.randint(50, 100)
# print('랜덤숫자', num)

# i = 1
# count1 = 0
# while i <= num:
#     if num % i == 0:
#         print(i, end = " ")
#         count1 += 1
#     i += 1

# check = 0
# if count1 % 2 == 0:
#     check = count1 // 2
# else:
#     check = count1 

# print()
# print("약수 개수 =", check)

# i = 1
# count2 = 0
# result= 0
# while i <= num:
#     if num % i == 0:
#         count2 += 1

#     if count2 == check:
#         result = i
#         # 반복문 종료
#         i = num + 1
#     i += 1

# print(result)