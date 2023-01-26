'''
    [문제]
        [조건1] 리스트에 랜덤 숫자(1~100) 20개를 추가한다.
        [조건2] 위 값 중 50보다 크면서 7의 배수만 출력하시오.
    [예시]
        arr = [18, 64, 54, 91, 2, 56, 18, 18, 16, 71, 17, 15, 35, 73, 34, 22, 50, 55, 35, 93]
        91
        56
'''

import random

arr = []
size = 20

# [1114] 
# for i in range(size) :
#     arr.append(random.randint(1, 100))
    
#     if arr[i] > 50 and arr[i] % 7 == 0 :
#         print(arr[i], end = " ")

# print()
# print("arr =", arr)

# [2차]
# i = 0
# while i < size :
#     arr.append(random.randint(1,100))

#     if arr[i] > 50 and arr[i] % 7 == 0 :
#         print(arr[i])
#     i += 1 
    
# print(arr)

# [1차]
# for i in range(size) : 
#     arr.append(random.randint(1, 100))
#     if arr[i] > 50 and arr[i] % 7 == 0 :
#         result = arr[i]

# print(arr)
# print(result)

# for i in range(size) :
#     if arr[i] > 50 and arr[i] % 7 ==0 : 
#         print(arr[i])


