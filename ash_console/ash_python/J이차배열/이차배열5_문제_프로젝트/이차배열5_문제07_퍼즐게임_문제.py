'''
    [문제]
        철수는 게임을 만들고 있다.
        game리스트는 이차원으로 되어있다.
        game리스트 안에 block리스트의 숫자를 채워 넣는 게임이다.

        리스트의 값1은 block이 차 있는 것을 의미한다.
        리스트의 값0은 block이 비어있는 것을 의미한다.
    [조건1] 
        block은 이번에 제시된 모양이다. 
        block의 모양을 game 리스트에 넣을 수 있다면 채워 넣고,
        넣을 수 없다면 "gameover"를 출력하시오.
    [조건2]
        block을 채워 넣었을 때 가로로 1이 연속 5개이거나, 
        세로로 1이 연속 5개이면 그 줄은 전부 숫자 2로 변경하시오.
    [정답]

'''
game = [
    [0,1,0,1,0],
    [1,1,0,1,1],
    [0,1,1,1,1],
    [1,1,0,1,1],
    [0,0,0,0,0]
]

block = [
    [0,1],
    [1,1]
]
'''
00 01
10 11
'''
# 0113
posY = 0
posX = 0
ck = False
for i in range(len(game)) :
    for j in range(len(game)) :
        if len(game) > i > 0 and len(game) > j > 0 :
            if game[i][j] == 0 and game[i - 1][j] == 0 and game[i][j - 1] == 0 :
                posY = i
                posX = j
                ck = True
                break

if ck == False :
    print("gameover")

print(posY,posX)

# 블럭 채우기
game[posY][posX] = 1
game[posY - 1][posX] = 1
game[posY][posX - 1] = 1

print()
tempList = []
for i in range(len(game)) :
    temp = []
    for j in range(len(game)) :
        temp.append(game[i][j])
        print(game[i][j], end = " ")
    tempList.append(temp)
    print()
print()

# 가로 검사
for i in range(len(game)) :
    cnt = 0 
    ck = False
    for j in range(len(game)) :
        if tempList[i][j] == 1 :
            cnt += 1
            tempY = i
    if cnt == 5 :
        ck = True

    if ck == True :
        for i in range(len(game)) :
            game[tempY][i] = 2


# 세로 검사
for i in range(len(game)) :
    cnt = 0 
    ck = False
    for j in range(len(game)) :
        if tempList[j][i] == 1 :
            cnt += 1
            tempX = i
    if cnt == 5 :
        ck = True

    if ck == True :
        for i in range(len(game)) :
            game[i][tempX] = 2

# 출력
for i in range(len(game)) :
    for j in range(len(game)) :
        print(game[i][j], end = " ")
    print()
print()


# # 1213
# # 조건1 
# # block에 맞는 위치를 찾고 1의 값을 넣는다.
# for i in range(len(game)) :
#     for j in range(len(game[i])) :
#         if 0 < i < len(game) - 1 and 0 < j < len(game) - 1 :
#             if game[i][j] == 0 :
#                 if game[i + 1][j] == 0 and game[i + 1][j - 1] == 0 :
#                     y = i
#                     x = j

# game[y][x] = 1 
# game[y + 1][x] = 1 
# game[y + 1][x - 1] = 1 
# # game[2][0] = 1 
# print(y, x)
# print("game : ")
# for i in range(len(game)) :
#     print(game[i])
    
# print()
# # 조건2 
# # 가로로 1이 5개이거나 세로로 1이 5개이면 숫자2로 변경

# # temp1에 복사
# # 복사를 하는 이유 : 가로나 세로가 중복이 된 위치에 있으면 먼저 검사한 가로의 값이 변경되면서 세로의 
# # 중복값에 변화가 생긴다.
# # 원본인 game의 리스트에서 검사하여 같은 위치에 temp리스트로 값을 옮긴다.
# temp1 = []
# for i in range(len(game)) :
#     temp2 = []
#     for j in range(len(game[i])) :
#         temp2.append(game[i][j])
#     temp1.append(temp2)

# print("temp : ")
# for i in range(len(temp1)) :
#     print(temp1[i])

# # 가로검사
# print()
# for i in range(len(game)) :
#     count = 0
#     for j in range(len(game[i])) :
#         if game[i][j] == 1 :
#             x = i 
#             count += 1
#     if count == 5 :
#         for k in range(5) :
#             temp1[x][k] = 2 

# # 세로로 1이 5개
# for i in range(len(game)) :
#     count = 0
#     for j in range(len(game[i])) :
#         if game[j][i] == 1 :
#             y = i
#             count += 1
#     if count == 5 :
#         for k in range(5) :
#             temp1[k][y] = 2

# print("game : ")
# for i in range(len(game)) :
#     print(game[i])

# print("reuslt : ")
# for i in range(len(temp1)) :
#     print(temp1[i])
