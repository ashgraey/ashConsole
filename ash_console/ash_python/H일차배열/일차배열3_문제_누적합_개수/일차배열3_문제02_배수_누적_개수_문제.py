'''
    [문제]
        [조건1] 배열에 랜덤숫자(1~100) 5개를 추가하고,
        [조건2] 짝수만 출력하시오.
        [조건3] 짝수의 누적 합을 저장 후 출력하시오.
        [조건4] 짝수의 개수를 출력하시오.
    
    [예시]
        arr = [68, 81, 84, 72, 81]
        68
        84
        72

        개수 = 3
        합 = 224
'''
import random

# [1114]
# arr = []
# result = []

# total = 0
# count = 0

# for i in range(5) :
#     arr.append(random.randint(1, 100))

#     if arr[i] % 2 == 0 :
#         result.append(arr[i])
#         total += arr[i]
#         count += 1 

# print("arr =", arr)
# print("result =", result)
# print("total =", total)
# print("count =", count)

# [1차]
# arr = []
# size = 5
# total = 0
# count = 0 
# 짝수 = []

# for i in range(size) :
#     arr.append(random.randint(1, 100))
    
#     if arr[i] % 2 == 0 :
#         짝수.append(arr[i])
#         total += arr[i]
#         count += 1

# print(arr)
# print(짝수)
# print(count)
# print(total)
