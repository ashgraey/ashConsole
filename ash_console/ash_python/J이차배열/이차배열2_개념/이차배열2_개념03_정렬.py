'''
    [문제]
         a이차리스트에 값(1~100)을 9개 저장 후
         내림차순 정렬하시오.
    [예시]
        정렬 전 >>>
        [72, 23, 40]
        [67, 62, 88]
        [57, 54, 48]

        b = [72, 23, 40, 67, 62, 88, 57, 54, 48] 
        b :  [88, 72, 67, 62, 57, 54, 48, 40, 23]
        
        정렬 후 >>>
        [88, 72, 67]
        [62, 57, 54]
        [48, 40, 23]
'''
import random

a = [
        [0,0,0],
        [0,0,0],
        [0,0,0]
    ]
# 정답 
# for i in range(len(a)):
#     for j in range(len(a[i])):
#         a[i][j] = random.randint(1,100)
        
# print("정렬 전 >>>")
# for i in range(len(a)):
#     print(a[i])

# b = []
# for i in range(len(a)):
#     for j in range(len(a[i])):
#         b.append(a[i][j])
# print("b =", b)

# i = 0
# while i < len(b):
#     max = b[i]
#     maxIndex = i

#     j = i
#     while j < len(b):
#         if max < b[j]:
#             max = b[j]
#             maxIndex = j
#         j += 1
    
#     temp = b[i]
#     b[i] = b[maxIndex]
#     b[maxIndex] = temp

#     i += 1
# print("b : " , b)

# index = 0
# for i in range(len(a)):
#     for j in range(len(a[i])):
#         a[i][j] = b[index]
#         index += 1
# print("정렬 후 >>>")
# for i in range(len(a)):
#     print(a[i])

# 1125
# for i in range(len(a)) :
#     for j in range(len(a[i])) :
#         a[i][j] = random.randint(1, 100)

# for i in range(len(a)) :
#     print(a[i])

# # 이차원 배열의 값을 일차원 배열로 옮긴다.
# b = []
# for i in range(len(a)) :
#     for j in range(len(a[i])) :
#         b.append(a[i][j])
# print(b)

# for i in range(len(b)) :

#     max = b[i]
#     maxIdx = i

#     j = i 
#     while j < len(b) :
#         if max < b[j] :
#             max = b[j]
#             maxIdx = j
#         j += 1 
    
#     temp = b[i]
#     b[i] = b[maxIdx]
#     b[maxIdx] = temp 
# print(b)

# # 일차원 배열의 값을 이차원 배열로 다시 옮긴다. 
# idx = 0
# for i in range(len(a)) :
#     for j in range(len(a[i])) :
#         a[i][j] = b[idx]
#         idx += 1 
# print(a)

# print("내림차순 정렬 ==>")
# for i in range(len(a)) :
#     print(a[i])

