"""
[문제]
    아래 배열은 11~22까지 12개의 값이 저장된배열이다.
    아래배열을 세로3 가로4 즉 3행 4열로 출력한다. 
    그후, 랜덤으로 11~22사이의 값을 하나 저장후 그값이
    몇행 몇열인지 출력하시오. 행은 세로 열은 가로를 뜻한다. 
[예시]
    11 12 13 14
    15 16 17 18
    19 20 21 22

    r = 20 => 3행 2열
    r = 17 => 2행 3열 
"""
import random 

a = [11,12,13,14,
15,16,17,18,
19,20,21,22]
# print(a)

r = random.randint(11, 22)
print("r =", r)

# 이차반복
# x = 0
# y = 0
# k = 0 
# position = 0
# for i in range(3) :
#     for j in range(4) :
#         if a[k] == r :
#             x = i
#             y = j
#             position = k
#         k += 1 

# print(x,"행", y,"열")

# 일차반복
x = 0
y = 0
position = 0

i = 0 
while i < len(a) :
    if a[i] == r :
        position = i
    i += 1 

print(position)
y = (position // 4) + 1
x = (position % 4) + 1
print(y, "행", x, "열")

print("===== 정답 =====")
# 가로 * 4, 세로 * 3 출력
# for i in range(len(a)):
#     print(a[i], end=" ")
#     if i % 4 == 3:
#         print()

# r = random.randint(11,22)
# # index 초기값 -100인 이유????
# index = -100
# for i in range(len(a)):
#     if a[i] == r:
#         index = i

# print("랜덤값 :" , r)
# print("인덱스 : " , index)

# sero = index // 4 + 1
# garo = index % 4 + 1

# print(sero ,"행",garo,"열")


