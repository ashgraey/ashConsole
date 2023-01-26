'''
    [문제]
        철수는 빙고 게임을 만들고 있다.
        빙고 조건은 가로 1이 3개 또는 세로 1이 3개 또는 대각선으로 1이 3개이면 빙고이다.
        빙고는 중첩될 수 있다.
        반복적으로 랜덤 위치에 1을 저장한다. 
        단, 한번 1이 저장된 곳은 또 다시 저장할 수 없다.
        3빙고가 성립되면 종료한다. 
'''
'''
오대각 : 00 11 22 
왼대각 : 02 11 20

'''
import random
bingo = [
    [0,0,0],
    [0,0,0],
    [0,0,0]
]
# 0113

while True : 
    x  = random.randint(0, len(bingo) - 1)
    y = random.randint(0, len(bingo) - 1)
    print(x, y)

    result = 0
    if(bingo[y][x] == 0) :
        bingo[y][x] = 1
    elif(bingo[y][x] == 1) :
        continue

    # 출력
    for i in range(len(bingo)) :
        print(bingo[i])

    # 가로검사
    cnt = 0
    for i in range(0, len(bingo)) :
        cnt = 0
        for j in range(0, len(bingo)) :
            if bingo[i][j] == 1 :
                cnt += 1
                if cnt == 3 :
                    result += 1

    # 세로검사
    cnt = 0
    for i in range(0, len(bingo)) :
        cnt = 0 
        for j in range(0, len(bingo)) : 
            if bingo[j][i] == 1 : 
                cnt += 1
                if cnt == 3 :
                    result += 1

    # 대각검사 \
    if(bingo[0][0] == 1 and bingo[1][1] == 1 and bingo[2][2] == 1) :
        result += 1
    # 대각검사 /
    if(bingo[0][2] == 1 and bingo[1][1] == 1 and bingo[2][0] == 1) :
        result += 1

    print("result : ", result)
    if result >= 3 :
         # 출력
        # for i in range(len(bingo)) :
        #     print(bingo[i])
        break

         
# 1212
# cnt = 0
# win = 0
# while True :

#     y = random.randint(0, 2)
#     x = random.randint(0, 2)
#     print("y : ", y, "x : ", x)

#     # 한번 저장된곳에 저장할수없다
#     if bingo[y][x] == 0 :
#         bingo[y][x] = 1
#         # cnt += 1 
#     else :
#         continue

#     for i in range(len(bingo)) :
#         print(bingo[i])
    
#     print(cnt, win)
#     if win >= 3 :
#         # print(win)
#         break

#     # 가로 확인
#     for i in range(len(bingo)) :
#         cnt = 0 
#         for j in range(len(bingo[i])) :
#             if bingo[i][j] == 1 :
#                 cnt += 1 
                
#         if cnt == 3 :
#             win += 1

#     # print(cnt)
    
#     # 세로 확인
#     for i in range(len(bingo)) :
#         cnt = 0
#         for j in range(len(bingo[i])) :
#             if bingo[j][i] == 1 :
#                cnt += 1

#         if cnt == 3 :
#             win += 1 

#     # 오른 대각 확인 
#     cnt = 0 
#     for i in range(len(bingo)) :
#         if bingo[i][i] == 1 :
#             cnt += 1 
#     if cnt == 3 :
#         win += 1
    

#     # 왼쪽 대각 확인
#     num = 2
#     cnt = 0 
#     for i in range(len(bingo)) :
#         if bingo[i][num] == 1 :
#             cnt += 1
#             num -= 1
#     if cnt == 3 :
#         win += 1
        
# 1차
# tot = 0 

# while(True) :
    
#     if tot >= 3 :
#         break
# # 랜덤값 받기
#     y = random.randint(0,2)
#     x = random.randint(0,2)
#     print("y = ", y, "x = ",x)

# # 랜덤위치 값 검사
#     if(bingo[y][x] == 0) :
#         bingo[y][x] = 1
#     else :
#         continue

#     for i in range(len(bingo)) :
#         print(bingo[i])
#     print()
#     print()
# # 빙고 검사 및 종료
#     # 초기화 위치의 중요성! 이것땜에 계속 헤메고 있었음ㅜㅜ
#     garo = 0 
#     sero = 0
#     opp = 0

#     # 가로검사
#     for i in range(len(bingo)) :
#         count = 0
#         for j in range(3) :
#             if bingo[i][j] != 0 :
#                 count += 1
#         if count == 3 :
#             garo += 1

#     # 세로검사
#     for i in range(len(bingo)) :
#         count = 0
#         for j in range(3) :
#             if bingo[j][i] != 0 :
#                 count += 1 
#         if count == 3 :
#             sero += 1 
    
#     # 대각검사 \
#     count = 0
#     for i in range(len(bingo)) :
#         if bingo[i][i] != 0 :
#             count += 1 
#     if count == 3 :
#         opp += 1

#     # 대각검사 /
#     count = 0
#     for i in range(len(bingo)) :
#         if bingo[i][2 - i] != 0 :
#             count += 1
#     if count == 3 :
#         opp += 1  
    
#     tot = garo + sero + opp

# print(garo, sero, opp, tot)
# # for i in range(len(bingo)) :
# #     print(bingo[i])





