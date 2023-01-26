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
    [1,1,0,1,0],
    [0,0,0,0,0]
]

block = [
    [0,1],
    [1,1]
]

y = 0
x = 0
for i in range(len(game) - 1):
    for j in range(len(game[i]) - 1):
        count = 0
        if game[i][j + 1] == 0:
            count += 1
        if game[i + 1][j] == 0:
            count += 1
        if game[i + 1][j + 1] == 0:
            count += 1

        if count == 3:
            y = i
            x = j
            break
print(y, x)   

game[y][x + 1] = block[0][1]
game[y + 1][x] = block[1][0]
game[y + 1][x + 1] = block[1][1]
print()

for i in range(len(game)):
    print(game[i])
print()

temp = []
for i in range(len(game)):
    unit = []
    for j in range(len(game[i])):
        unit.append(game[i][j])
    temp.append(unit)

# 가로검사
for i in range(len(game)):
    count = 0
    for j in range(len(game)):
        if game[i][j] == 1:
            count += 1
    if count == 5:
        for j in range(len(game)):
            temp[i][j] = 2

# 세로검사
for i in range(len(game)):
    count = 0
    for j in range(len(game)):
        if game[j][i] == 1:
            count += 1
    if count == 5:
       for j in range(len(game)):
            temp[j][i] = 2

for i in range(len(game)):
    print(game[i])
print()

for i in range(len(temp)):
    print(temp[i])
print()
