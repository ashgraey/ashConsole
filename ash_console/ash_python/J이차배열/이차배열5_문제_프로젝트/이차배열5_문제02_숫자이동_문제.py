'''
    [문제]
        철수는 게임을 만들고 있다.
        game리스트는 이차원으로 되어있다.
        숫자8은 플레이어 위치를 뜻한다.
        숫자0은 플레이어가 움직일 수 있는 위치이다.
        
        order리스트는 플레이어가 움직이게 하는 명령어이다.
        1,2,3,4는 차례대로 북, 동, 남, 서를 뜻한다. 

        order의 이동대로 플레이어를 이동시키고 출력하시오.
        플레이어가 벽에 붙어서,
        더 이상 원하는 방향으로 이동할 수 없을 때는 "이동 불가"를 출력한다.
    [정답]        
        캐릭터의 현재 위치 = 2 , 2
        0 0 0 0 0
        0 0 0 0 0
        0 0 8 0 0
        0 0 0 0 0
        0 0 0 0 0 

        북
        0 0 0 0 0
        0 0 8 0 0
        0 0 0 0 0
        0 0 0 0 0
        0 0 0 0 0

        남
        0 0 0 0 0
        0 0 0 0 0
        0 0 8 0 0
        0 0 0 0 0
        0 0 0 0 0

        남
        0 0 0 0 0
        0 0 0 0 0
        0 0 0 0 0
        0 0 8 0 0
        0 0 0 0 0

        남
        0 0 0 0 0
        0 0 0 0 0
        0 0 0 0 0
        0 0 0 0 0
        0 0 8 0 0

        서
        0 0 0 0 0
        0 0 0 0 0
        0 0 0 0 0
        0 0 0 0 0
        0 8 0 0 0

        남
        이동 불가
        0 0 0 0 0
        0 0 0 0 0
        0 0 0 0 0
        0 0 0 0 0
        0 8 0 0 0

        남
        이동 불가
        0 0 0 0 0
        0 0 0 0 0
        0 0 0 0 0
        0 0 0 0 0
        0 8 0 0 0

        서
        0 0 0 0 0
        0 0 0 0 0
        0 0 0 0 0
        0 0 0 0 0
        8 0 0 0 0

        동
        0 0 0 0 0
        0 0 0 0 0
        0 0 0 0 0
        0 0 0 0 0
        0 8 0 0 0
'''

game = [
    [0,0,0,0,0],
    [0,0,0,0,0],
    [0,0,8,0,0],
    [0,0,0,0,0],
    [0,0,0,0,0],
]
# 1 북, 2 동, 3 남, 4 서
order = [1,3,3,3,4,3,3,4,2]
# 0113
for i in range(len(order)) :   
    positionX = 0
    positionY = 0
    for y in range(len(game)) :
        for x in range(len(game)) :
            print(game[y][x], end = " ")
            if game[y][x] == 8 :
                positionY = y
                positionX = x
        print()
    print()

    print(positionY, positionX)

    tempY = positionY
    tempX = positionX
    
    # 북
    if order[i] == 1 :
        print("북")
        tempY -= 1
    
    # 동
    elif order[i] == 2 :
        print("동")
        tempX += 1
    # 남
    elif order[i] == 3 :
        print("남")
        tempY += 1
    # 서
    elif order[i] == 4 :
        print("서")
        tempX -= 1

    print("temp : ", tempY, tempX)
    if (tempY >= 0 and tempY < len(game)) and (tempX >= 0 and tempX < len(game)) :
            game[positionY][positionX] = 0
            game[tempY][tempX] = 8
    else :
        print("이동불가")


for i in range(len(game)) :
    for j in range(len(game)) :
        print(game[i][j], end = " ") 
    print()
            

# 1213
# 조건문과 반복문의 디테일이 부족한 느낌
# 전체적인 그림은 대충은 볼수있는 느낌
# 현재위치 : position
# position = 0 
# for i in range(len(game)) :
#     for j in range(len(game[i])) :
#         if game[i][j] != 0 :
#             y = i
#             x = j
#             break
# position = game[y][x]
# print(position, y,x)

# # 북1, 동2, 남3, 서4
# for i in range(len(order)) :
#     for j in range(len(game)) :
#         print(game[j])

#     gY = y
#     gX = x

#     if order[i] == 1 :
#         gY -= 1
      
#     elif order[i] == 2 :
#         gX += 1
      
#     elif order[i] == 3 :
#         gY += 1
        
#     elif order[i] == 4 :
#         gX -= 1

#     if (gY < 0 or gY > 4) :
#         print("이동불가")
#         continue
#     if (gX < 0 or gX > 4) :
#         print("이동불가")
#         continue
    
#     game[y][x] = 0
#     y = gY
#     x = gX
#     game[gY][gX] = 8

#     print("y = ", y, "x =", x)

# for i in range(len(game)) :
#     print(game[i])

# 1212
# 시작 위치값
# for i in range(len(game)) :
#     for j in range(len(game[i])) :
#         if game[i][j] == 8 :
#             y = i
#             x = j 
#             break
# print("y = ", y, "x = ", x)
# # position = game[y][x]

# for i in range(len(order)) :
#     # 1234 북동남서
#     for j in range(len(game)) :
#         print(game[j])
    
#     tempX = x
#     tempY = y 
    
#     if order[i] == 1 :
#         tempY -= move
    
#     elif order[i] == 2 :
#         tempX += move 
    
#     elif order[i] == 3 :
#         tempY += move
    
#     else :
#         tempX -= move


#     if len(game[0]) <= tempY or tempX < 0 :
#         print("이동불가")
#         continue
#     if len(game) <= tempY or tempX < 0 :
#         print("이동불가")
#         continue
    
#     # 이동하려는 결과를 변수에 담아 모든 조건이 실행된 후 마지막에 값교체를 시킨다.
#     # 중간에 교체식 썼다가 오류 엄청 남
#     game[y][x] = 0 
#     x = tempX
#     y = tempY
#     game[y][x] = 8
    
#     # print(position)

#     print("y = ", tempY, "x = ", tempX)

# # 마지막 조건 출력하기위해 반복문 밖에 출력문을 하나 더 써준다
# for i in range(len(game)) :
#     print(game[i])
  