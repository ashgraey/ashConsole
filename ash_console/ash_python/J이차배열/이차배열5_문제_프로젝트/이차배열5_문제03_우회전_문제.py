'''
    [문제]
        랜덤(1~4)를 저장한다. 랜덤숫자는 회전 횟수이다. 
        회전 횟수만큼 block의 숫자들을 90도로 우회전시키시오.
        
    [예시]
        rNum = 4
        1 2 3       00 01 02 
        4 5 6       10 11 12
        7 8 9       20 21 22

        7 4 1       20 10 00
        8 5 2       21 11 01
        9 6 3       22 12 02

        9 8 7 
        6 5 4 
        3 2 1 

        3 6 9 
        2 5 8 
        1 4 7 
'''
'''
00 01 02 
2회전 = 00 01 02 => 02 12 22 
3회전 = 02 12 22 => 22 21 20
4회전 = 22 21 20 => 20 10 00  
'''
import random

block = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
# 0113
rNum = random.randint(1,4)
print(rNum)

for i in range(0, rNum) :

    # 출력
    for j in range(0, len(block)) :
        for k in range(0, len(block)) :
            print(block[j][k], end = " ")
        print()
    print()

    # 복사
    tempList = []
    for i in range(len(block)) :
        temp = []
        for j in range(len(block)) :
            temp.append(block[i][j])
        tempList.append(temp)
    # print(tempList)

    # 90도 회전식
    for j in range(0, len(block)) :
        for k in range(0, len(block)) :
            block[k][2 - j] = tempList[j][k]

# # 1213
# turn = random.randint(1,4)
# print("turn : ", turn)

# for i in range(turn) :

#     temp = []
#     for j in range(len(block)) :
#         temp.append([0, 0, 0])
    
#     if i == 0 :
#         for j in range(len(block)) :
#             for k in range(len(block[i])) :
#                 temp[j][k] = block[j][k]
    
#     elif i == 1 :
#         for j in range(len(block)) :
#             for k in range(len(block[j])) :
#             # print(block[j][k], end = " ")
#                 temp[k][2 - j] = block[j][k]

#     elif i == 2 :
#         for j in range(len(block)) :
#             for k in range(len(block[j])) :
#             # print(block[j][k], end = " ")
#                 temp[2 - j][2 - k] = block[j][k]

#     elif i == 3 :
#         for j in range(len(block)) :
#             for k in range(len(block)) :
#                 temp[2 - k][j] = block[j][k] 
    
#     # print()
#     for j in range(len(temp)) :
#         for k in range(len(temp[j])) :
#             print(temp[j][k], end = " ")
#         print()
#     print() 

# 1213 - 1차식
# temp = []
# for i in range(len(block)) :
#     temp.append([0, 0, 0])

# if turn == 1 :
#     for i in range(len(block)) :
#         print(block[i])

# elif turn == 2 :
# # num = 2
#     for j in range(len(block)) :
#         for k in range(len(block[j])) :
#             # print(block[j][k], end = " ")
#             temp[k][2 - j] = block[j][k]

# elif turn == 3 :
#     for j in range(len(block)) :
#         for k in range(len(block[j])) :
#             # print(block[j][k], end = " ")
#             temp[2 - j][2 - k] = block[j][k]

# else : 
#     for j in range(len(block)) :
#         for k in range(len(block)) :
#             temp[2 - k][j] = block[j][k] 

# for i in range(len(temp)) :
#     print(temp[i]) 




        



