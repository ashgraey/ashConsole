# 1 to 50 딕셔너리

import random

nodeList = []

for i in range(25):
    node = {}
    node["front"] = i + 1
    node["back"] = i + 26

    nodeList.append(node)
# print(nodeList)

# 셔플(shuffle)
for i in range(100):
    r = random.randint(0, 24)

    temp = nodeList[0]["front"]
    nodeList[0]["front"] = nodeList[r]["front"]
    nodeList[r]["front"] = temp

for i in range(100):
    r = random.randint(0, 24)

    temp = nodeList[0]["back"]
    nodeList[0]["back"] = nodeList[r]["back"]
    nodeList[r]["back"] = temp

game_num = 1
while True:
    # 화면 출력
    for i in range(25):
        if nodeList[i]["front"] == 0:
            print("\t", end="")
        else:
            print(nodeList[i]["front"], end="\t")
        if i % 5 == 4:
            print()

    if game_num == 51:
        print("게임 종료")
        break
    
    # 위치 선택
    idx = int(input("%d의 위치 선택 : " % game_num))
    if game_num == nodeList[idx]["front"]:
        if 1 <= game_num and game_num <= 25:
            nodeList[idx]["front"] = nodeList[idx]["back"]
        else:
            nodeList[idx]["front"] = 0
        game_num += 1# 1 to 50 딕셔너리

import random

nodeList = []

for i in range(25):
    node = {}
    node["front"] = i + 1
    node["back"] = i + 26

    nodeList.append(node)
# print(nodeList)

# 셔플(shuffle)
for i in range(100):
    r = random.randint(0, 24)

    temp = nodeList[0]["front"]
    nodeList[0]["front"] = nodeList[r]["front"]
    nodeList[r]["front"] = temp

for i in range(100):
    r = random.randint(0, 24)

    temp = nodeList[0]["back"]
    nodeList[0]["back"] = nodeList[r]["back"]
    nodeList[r]["back"] = temp

game_num = 1
while True:
    # 화면 출력
    for i in range(25):
        if nodeList[i]["front"] == 0:
            print("\t", end="")
        else:
            print(nodeList[i]["front"], end="\t")
        if i % 5 == 4:
            print()

    if game_num == 51:
        print("게임 종료")
        break
    
    # 위치 선택
    idx = int(input("%d의 위치 선택 : " % game_num))
    if game_num == nodeList[idx]["front"]:
        if 1 <= game_num and game_num <= 25:
            nodeList[idx]["front"] = nodeList[idx]["back"]
        else:
            nodeList[idx]["front"] = 0
        game_num += 1