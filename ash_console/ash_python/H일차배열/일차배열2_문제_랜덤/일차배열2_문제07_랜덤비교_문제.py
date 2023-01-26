'''
    [문제]
        [조건1] a, b 리스트 두 개에 1~100 사이의 랜덤 값 다섯 개를 저장한다.
        [조건2] base 변수에 랜덤으로 1~100 사이의 숫자를 저장한다. 
        base 변수값보다 큰 값들을 전부 출력하시오.
    [예시]
'''
import random

# [1114]
# a = []
# b = []
# size = 5

# base = random.randint(1, 100)
# print("base =", base)

# for i in range(size) :
#     a.append(random.randint(1, 100))
#     b.append(random.randint(1, 100))

#     if a[i] > base :
#         print("a : ",a[i])
#     if b[i] > base : 
#         print("b : ", b[i])

# print("a =", a)
# print("b =", b)
    
# [2차]
# base = random.randint(1, 100)
# print("base =", base)

# i = 0 
# while i < size :
#     a.append(random.randint(1, 100))
#     b.append(random.randint(1, 100))
    
#     if base < a[i] :
#         print(a[i])
    
#     if base < b[i] :
#         print(b[i])

#     i += 1 
# print()
# print(a)
# print(b)

# [1차]
# base = random.randint(1, 100)
# print("base =", base)

# size = 5 

# for i in range(size) : 
#     a.append(random.randint(1,100))
#     b.append(random.randint(1,100))

# print(a)
# print(b)

# for i in range(size) :
#     if base < a[i] :
#         print("a = ", a[i])
#     if base < b[i] :
#         print("b = ", b[i])
    
    # elif base < b[i] :
    #     print("b = ", b[i])

