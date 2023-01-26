'''
    [문제]
        [조건1] 리스트에 랜덤 숫자(1~100) 5개를 추가한다.
        [조건2] 위 값 중에 50보다 큰 값들만 출력한다.
    [예시]
        arr = [84, 28, 5, 100, 80]
        84
        100
        80
'''

import random

# [1114]
# arr = []
# result = []
# size = 5 

# # [조건1] 리스트에 랜덤 숫자(1~100) 5개를 추가한다.
# for i in range(size) :
#     arr.append(random.randint(1, 100))

#     if arr[i] > 50 :
#         result.append(arr[i])

# print("arr =", arr)
# print("result =", result)

# [2차]
# for i in range(size) :
#     r = random.randint(1, 100)
#     # print("랜덤숫자 =",r)

#     arr.append(r)

#     if arr[i] > 50 :
#         print(arr[i], end = " ")
# print()
# print(arr)

# [1차]
# size = 5 

# for i in range(size) : 
#     r = random.randint(1, 100)
#     arr.append(r)
# print(arr)

# for i in range(size) : 
#     if arr[i] > 50 :
#         print(arr[i])
    
