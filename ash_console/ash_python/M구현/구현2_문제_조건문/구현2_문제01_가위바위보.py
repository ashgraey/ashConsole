"""
[문제]
	[가위 바위 보 게임]
		1. player1 은 가위 바위 보중 하나를 입력받는다. 
		2. com 은 랜덤으로 가위 바위 보를 고른다. 
		3. 결과를 출력한다.
"""
import random

print("가위, 바위, 보 중 하나를 입력하세요.", end=" : ")
player1 = input()

# 0 가위, 1 바위, 2 보
com = random.randint(0, 2)

if com == 0:
    com = "가위"
elif com == 1:
    com = "바위"
elif com == 2:
    com = "보"

result = ""
if player1 == com:
    result = "무승부"

elif player1 == "가위" and com == "보":
    result = "p1 승리"

elif player1 == "바위" and com == "가위":
    result = "p1 승리"

elif player1 == "보" and com == "바위":
    result = "p1 승리"

else:
    result = "com 승리"

print(player1, " : ", com)
print(result)
