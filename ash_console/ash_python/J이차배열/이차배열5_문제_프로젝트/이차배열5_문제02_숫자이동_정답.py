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

order = [1,3,3,3,4,3,3,4,2]

# 캐릭터의 위치
pY = 0
pX = 0
for i in range(len(game)):
    for j in range(len(game[i])):
        if game[i][j] == 8:
            pY = i
            pX = j
            break
print("캐릭터의 현재 위치 =", pY, ",", pX)

for i in range(len(order)):

    for j in range(len(game)):
        for k in range(len(game[j])):
            print(game[j][k], end=" ")
        print()
    print()

    tempY = pY
    tempX = pX

    if order[i] == 1:           # 북
        tempY -= 1
        print("북")
    elif order[i] == 2:         # 동
        tempX += 1
        print("동")
    elif order[i] == 3:         # 남
        tempY += 1
        print("남")
    elif order[i] == 4:         # 서
        tempX -= 1        
        print("서")
    
    if 5 <= tempY or tempY < 0:
        print("이동 불가")
        continue
    if 5 <= tempX or tempX < 0:
        print("이동 불가")
        continue

    game[pY][pX] = 0
    pY = tempY
    pX = tempX
    game[pY][pX] = 8

for j in range(len(game)):
    for k in range(len(game[j])):
        print(game[j][k], end=" ")
    print()