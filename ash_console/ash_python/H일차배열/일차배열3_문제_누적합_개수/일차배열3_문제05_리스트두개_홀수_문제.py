'''
    [문제]
        a리스트와 b리스트에 랜덤 숫자(1~100)를 다섯 개씩 저장하고,
        a리스트의 전체 합과 b리스트의 값들 중 홀수의 합만 출력하시오. 
        a리스트의 홀수 합과 b리스트의 홀수 합을 비교해서 더 큰 값을 출력하시오.
        서로 같으면 둘 다 출력하시오.
    [예시]
        a = [28, 79, 47, 70, 36]
        b = [63, 4, 45, 54, 87]
        total1 = 126
        total2 = 195
        195    
'''
'''
조건1 : a,b 5개씨 랜덤 숫자(1,100)값을 저장
조건2 : a,b 리스트의 합의 값 중 홀수만 출력
조건3 : a,b 홀수 합을 비교 더 큰 값을 출력
조건4 : 같으면 둘다 출력
'''
import random

a = []
b = []

# [1114]
# a홀수 = []
# b홀수 = []

# total_a = 0 
# total_b = 0 

# for i in range(5) :
#     a.append(random.randint(1, 100))
#     b.append(random.randint(1, 100))
#     # a.append(5)
#     # b.append(5)

#     if a[i] % 2 == 1 :
#         a홀수.append(a[i])
#         total_a += a[i]
#     if b[i] % 2 == 1 :
#         b홀수.append(b[i])
#         total_b += b[i]

# print("a =", a)
# print("b =", b)
# print("a홀수 =", a홀수)
# print("b홀수 =", b홀수)
# print("total_a =", total_a)
# print("total_b =", total_b)

# if total_a > total_b :
#     print("a가 크다 =", total_a)
# elif total_a < total_b :
#     print("b가 크다 =", total_b)
# else :
#     print("서로같다", "a =", total_a, "b =", total_b)

# [2차]
# size = 5 
# a_total = 0
# b_total = 0
# result = 0

# for i in range(size) :
#     a.append(random.randint(1, 100))
#     b.append(random.randint(1, 100))
#     # a.append(7)
#     # b.append(7)
#     if a[i] % 2 == 1 :
#         a_total += a[i]
#     if b[i] % 2 == 1 :
#         b_total += b[i]

# if a_total > b_total :
#     result = a_total
# elif b_total > a_total :
#     result = b_total
# elif a_total == b_total :
#     result = "서로같다."

# print("a =",a)
# print("b =",b)
# print("a_total =",a_total)
# print("b_total =",b_total)
# print("result =", result)

# [1차]
# size = 5 
# a홀수 = []
# b홀수 = []
# a홀수합 = 0 
# b홀수합 = 0 

# for i in range(size) : 
#     a.append(random.randint(1,100))
#     b.append(random.randint(1,100))
#     if a[i] % 2 == 1 : 
#         a홀수.append(a[i])
#         a홀수합 += a[i]

#     elif b[i] % 2 == 1 : 
#         b홀수.append(b[i])
#         b홀수합 += b[i]
# print(a)
# print(b)
# print("a홀수 =", a홀수)
# print("b홀수 =",b홀수)
# print("a홀수합 =", a홀수합 )
# print("b홀수합 =",b홀수합 )

# if a홀수합 > b홀수합 : 
#     print("a홀수합이 크다:", a홀수합)
# elif a홀수합 < b홀수합 : 
#     print("b홀수합이 크다 :", b홀수합)
# elif a홀수합 == b홀수합 :
#     print("a와b의 홀수합 :", a홀수합, b홀수합)

