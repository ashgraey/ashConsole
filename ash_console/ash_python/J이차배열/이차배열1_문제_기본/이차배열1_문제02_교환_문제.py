'''
    [문제]
        [1] a이차리스트에 랜덤 값(1~100)을 9개 저장 후 출력하시오.
        [2] 랜덤으로 값 두 개를 선택 후 두 개의 위치를 교환 후 출력하시오.
    [예시]
    값 교체 전 >>>
    [46, 62, 75]
    [36, 18, 100]
    [26, 11, 39]

    r1 = 11
    r2 = 36
    
    값 교체 후 >>>
    [46, 62, 75]
    [11, 18, 100]
    [26, 36, 39]
'''
import random

a = [[0,0,0], [0,0,0], [0,0,0]]

# 1125
# for i in range(len(a)) :
#     for j in range(len(a[i])) :
#         a[i][j] = random.randint(1, 100)
# print(a)

# ri1 = random.randint(0, 2)
# ri2 = random.randint(0, 2)
# r1 = a[ri1][ri2]
# print("r1 =", r1)

# ry1 = random.randint(0, 2)
# ry2 = random.randint(0, 2)
# r2 = a[ry1][ry2]
# print("r2 =", r2)

# # temp = r1 
# a[ri1][ri2] = r2 
# a[ry1][ry2] = r1
# print(a) 

