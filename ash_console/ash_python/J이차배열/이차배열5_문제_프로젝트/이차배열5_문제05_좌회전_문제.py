'''
    [문제]
        랜덤(1~4)를 저장한다. 랜덤숫자는 회전 횟수이다. 
        회전 횟수만큼 block의 숫자들을 90도로 좌회전시키시오.
    [예시]
        rNum = 4
        1 2 3 
        4 5 6 
        7 8 9 

        3 6 9 
        2 5 8 
        1 4 7 

        9 8 7 
        6 5 4 
        3 2 1 

        7 4 1 
        8 5 2 
        9 6 3 
'''
'''
2회전 : 20 10 00 
'''
import random

block = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
# 0113

r = random.randint(1, 4)
print("r : ", r)

turn = r 

for i in range(turn) :

    # 출력
    for j in range(len(block)) :
        for k in range(len(block)) :
            print(block[j][k], end =" ")
        print()
    print()

    # 복사
    tempList = []
    for j in range(len(block)) :
        temp = []
        for k in range(len(block)) :
            temp.append(block[j][k])
        tempList.append(temp)
    # print(tempList)

    # 좌회전 로직
    for j in range(len(block)) :
        for k in range(len(block)) :
            block[2 - k][j] = tempList[j][k]

# # 1213
# turn = random.randint(1,4)
# print("turn : ", turn)

# for i in range(turn) :
#     for j in range(len(block)) :
#         for k in range(len(block[j])) :
#             print(block[j][k], end = " ")
#         print()
#     print() 

#     # temp로 복사
#     temp1 = []
#     for j in range(len(block)) :
#         temp2 = []
#         for k in range(len(block[j])) :
#             temp2.append(block[j][k])
#         temp1.append(temp2)
    
#     # print(temp1)

#     # 회전 조건
#     for j in range(len(block)) :
#         for k in range(len(block[j])) :
#             block[2 - k][j] = temp1[j][k]
    

    