'''
    [문제]
        철수는 빙고 게임을 만들고 있다.
        빙고 조건은 가로 1이 3개 또는 세로 1이 3개 또는 대각선으로 1이 3개이면 빙고이다.
        빙고는 중첩될 수 있다.
        반복적으로 랜덤 위치에 1을 저장한다. 
        단, 한번 1이 저장된 곳은 또 다시 저장할 수 없다.
        3빙고가 성립되면 종료한다. 
'''
import random

bingo = [
    [0,0,0],
    [0,0,0],
    [0,0,0]
]

mark = 0

while True:

    for i in range(3):
        for j in range(3):
            print(bingo[i][j], end=" ")
        print()
    print()

    if mark >= 3:
        print("3빙고! 게임을 종료합니다.")
        break

    rY = random.randint(0, 2)
    rX = random.randint(0, 2)
    print("랜덤 인덱스 =", rY, rX)

    if bingo[rY][rX] != 0:
        continue

    bingo[rY][rX] = 1

    mark = 0

    # 가로 검사
    for i in range(3):
        count = 0
        for j in range(3):
            if bingo[i][j] == 1:
                count += 1
        if count == 3:
            mark += 1

    # 세로 검사
    for i in range(3):
        count = 0
        for j in range(3):
            if bingo[j][i] == 1:
                count += 1
        if count == 3:
            mark += 1

    # 대각선 \ 검사
    count = 0
    for i in range(3):
        if bingo[i][i] == 1:
            count += 1
    if count == 3:
        mark += 1

    # 대각선 / 검사
    count = 0
    for i in range(3):
        if bingo[i][2-i] == 1:
            count += 1
    if count == 3:
        mark += 1
