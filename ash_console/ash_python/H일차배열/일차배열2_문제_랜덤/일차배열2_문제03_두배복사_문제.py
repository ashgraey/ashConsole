'''
    [문제]
        랜덤 숫자(1~10) 다섯 개를 arr에 추가하고
        그 두 배를 total에 저장 후 출력하시오.
    [예시]
        arr   = [10, 3, 4, 2, 6]
        total = [20, 6, 8, 4, 12]
'''
import random
arr = []
total = []
# 너무 꼬아서 생각하지말자

# [1114]
# for i in range(5) :
#     arr.append(random.randint(1, 10))
#     total.append(arr[i] * 2)

# print("arr =", arr)
# print("total =", total)

# [2차]
# i = 0
# while i < 5 :
#     num = random.randint(1, 10)
#     arr.append(num)
#     total.append(num * 2)

#     i += 1 
# print(arr)
# print(total)

# [1차]
# size = 5 

# for i in range(size) :
#     arr.append(random.randint(1, 10))
#     total.append(arr[i] * 2)

# print(arr)
# print(total)

