"""
	[좌우이동게임]
		[1] x 는 플레이어의 위치이다.
		[2] 선택지 [1.left] [2.right] 가 있고, 
  		[3] 왼쪽을 선택하면 x의 위치가 1씩 감소하고 오른쪽을 선택하면 x의 위치가 1씩 증가한다.
		[4] 랜덤숫자 (-5 ~ 5) 사이의 값을 저장하고 목적지에 도착하면 게임은 종료한다. 
	[예시]
		목적지r = 3
		현재위치x = 0
		[1.left] [2.right] 번호를 고르세요.
		여기서 2번을선택할경우 아래와 같이 변한다. 
  
		목적지r = 3
		현재위치x = 1
		[1.left] [2.right] 번호를 고르세요.
		
"""
import random

r = random.randint(-5, 5)
print(r)
positionX = 0
# r = 0
while True:
    print("[1.left] [2.right]")
    a = int(input())

    if a == 1:
        positionX -= 1
    else:
        positionX += 1

    print(positionX)
    if positionX == r:
        print("목적지 도착")
        break
