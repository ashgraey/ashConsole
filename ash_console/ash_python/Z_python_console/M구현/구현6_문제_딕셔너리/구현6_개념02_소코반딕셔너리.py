# 소코반 딕셔너리

ball = "b"
goal = "g"
player = "p"
item = "i"
wall = "w"
road = "r"

# 캐릭터의 위치
p_y = 0
p_x = 0

# 공의 위치
b_y = 0
b_x = 0

# 골의 위치
g_y = 0
g_x = 0

# 예시
# node = {"status":"r", "y":0, "x":0}
import random

nodeList = []

for i in range(7):
    temp = []
    for j in range(7):
        node = {}
        node["status"] = road
        node["y"] = i
        node["x"] = j
        temp.append(node)
    nodeList.append(temp)
# print(nodeList)

# 벽 설치
wall_count = int(input("벽을 몇 개 설치하시겠습니까?"))
while wall_count != 0:
    r_y = random.randint(0, 6)
    r_x = random.randint(0, 6)

    if nodeList[r_y][r_x]["status"] == road:
        nodeList[r_y][r_x]["status"] = wall
        wall_count -= 1

# 공 설치
while True:
    r_y = random.randint(0, 6)
    r_x = random.randint(0, 6)

    if nodeList[r_y][r_x]["status"] == road:
        nodeList[r_y][r_x]["status"] = ball
        b_y = r_y
        b_x = r_x
        break

# 골대 설치
while True:
    r_y = random.randint(0, 6)
    r_x = random.randint(0, 6)

    if nodeList[r_y][r_x]["status"] == road:
        nodeList[r_y][r_x]["status"] = goal
        g_y = r_y
        g_x = r_x
        break    

# 캐릭터 설치
while True:
    r_y = random.randint(0, 6)
    r_x = random.randint(0, 6)

    if nodeList[r_y][r_x]["status"] == road:
        nodeList[r_y][r_x]["status"] = player
        p_y = r_y
        p_x = r_x
        break 


# 게임 시작
while True:
    for i in range(7):
        # 화면 출력
        for j in range(7):
            if nodeList[i][j]["status"] == road:
                print("__", end=" ")
            elif nodeList[i][j]["status"] == wall:
                print("[]", end=" ")
            elif nodeList[i][j]["status"] == ball:
                print("○", end=" ")
            elif nodeList[i][j]["status"] == goal:
                print("◎", end=" ")
            elif nodeList[i][j]["status"] == player:
                print("옷", end=" ")
        print()
    print()

    # 공을 골대에 넣으면 게임종료
    if b_y == g_y and b_x == g_x:
        print("게임종료")
        break
    
    # 위치 입력
    move = int(input("상(1), 하(2), 좌(3), 우(4) : "))

    yy = p_y
    xx = p_x

    if move == 1:
        yy = yy - 1
    elif move == 2:
        yy = yy + 1
    elif move == 3:
        xx = xx - 1
    elif move == 4:
        xx = xx + 1

    if 7 <= yy or yy < 0:
        continue
    if 7 <= xx or xx < 0:
        continue
    if nodeList[yy][xx]["status"] != road and nodeList[yy][xx]["status"] != ball:
        continue

    # 공을 만나면
    if nodeList[yy][xx]["status"] == ball:
        yyy = b_y
        xxx = b_x

        if move == 1:
            yyy = yyy - 1
        elif move == 2:
            yyy = yyy + 1
        elif move == 3:
            xxx = xxx - 1
        elif move == 4:
            xxx = xxx + 1

        if 7 <= yyy or yyy < 0:
            continue
        if 7 <= xxx or xxx < 0:
            continue
        if nodeList[yyy][xxx]["status"] == wall:
            continue

        nodeList[b_y][b_x]["status"] = road
        b_y = yyy
        b_x = xxx
        nodeList[b_y][b_x]["status"] = ball

    nodeList[p_y][p_x]["status"] = road
    p_y = yy
    p_x = xx
    nodeList[p_y][p_x]["status"] = player