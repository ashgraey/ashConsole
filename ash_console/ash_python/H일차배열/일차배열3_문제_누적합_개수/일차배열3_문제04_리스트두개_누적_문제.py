'''
    [문제]
        a리스트와 b리스트에 랜덤 숫자(1~100)를 다섯 개씩 저장하고,
        a리스트의 전체 합과 b리스트의 전체 합 중 더 큰 값을 출력하시오.
        서로 같으면 둘 다 출력하시오.
    [예시]
        a = [93, 100, 41, 74, 45]
        b = [84, 80, 25, 19, 27]
        total1 = 353
        total2 = 235
        353
'''
'''
조건 1 : a,b리스트에 랜덤숫자(1,100) 다섯개 저장
조건 2 : a리스트 전체합과 b리스트 전체합 중 더 큰 값을 출력 
조건 3 : == 둘다 출력 
'''
import random

a = []
b = []
size = 5 

# [1114]
# a_total = 0 
# b_total = 0 

# for i in range(size) :
#     # a.append(1)
#     # b.append(1)
#     a.append(random.randint(1, 100))
#     a_total += a[i]
#     b.append(random.randint(1, 100))
#     b_total += b[i]

# if a_total > b_total :
#     print("a_total =", a_total)
# elif b_total > a_total :
#     print("b_total =", b_total)
# else :
#     print("서로 같다", a_total, b_total)

# print("a =", a, a_total)
# print("b =", b, b_total)
    
# [1차]
# a_total = 0
# b_total = 0
# result = 0 

# for i in range(size) :
#     a.append(random.randint(1,100))
#     b.append(random.randint(1,100))
#     # a.append(1)
#     # b.append(1)

#     a_total += a[i]
#     b_total += b[i]

#     if a_total > b_total :
#         result = a_total
#     elif b_total > a_total :
#         result = b_total
#     else :
#         result = "서로같다"

# print(a, a_total)        
# print(b, b_total)        
# print(result)        



