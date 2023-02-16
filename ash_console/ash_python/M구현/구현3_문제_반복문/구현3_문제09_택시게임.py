"""
	[택시게임]
		1. 손님을 태워 목적지까지 이동하는 게임이다.
		2. 플레이어는 y와 x를 가지고있다. 
		3. -10 ~ 10 사이의 랜덤 숫자 2개를 저장해 목적지로 설정한다.
		4. x축과 y축이 있기때문에 방향을 설정한다. 시작방향은 동쪽 이다.
		5. 메뉴는 아래와 같다.	 		
	 		1) 방향설정 : 동(1)서(2)남(3)북(4)
	 		2) 이동하기 : 속도(1~3)을 입력받고 설정된 방향으로 설정된 속도만큼 이동
		6. 거리 1칸 당 50원씩 추가되어 도착시 요금도 출력한다.
		7. 도착하면 다시 -10 ~ 10 사이의 랜덤 목적지가 설정된다.		
	[예시]
		목적지 : rx = -4 , ry = 5
		현재위치 : x = 0 , y = 0
		현재방향 : "동"
		요금 : 0
  		[1.방향설정][2.이동하기][0.영업종료]
		1을 선택한경우 : [1.동][2.서][3.남][4.북] 메뉴를 보여주며, 1~4를 선택할수있다.
		2를 선택한경우 : [1.한칸이동][2.두칸이동][3.세칸이동] 메뉴를 보여주며, 1~3을 선택할수있다.
"""
import random
x = 0
y = 0
dir = "동"
price = 0
rx = 0
ry = 0
speed = 0
pay = 0

rx = random.randint(-10, 10)
ry = random.randint(-10, 10)
print("x : ", rx, "y : ", ry)

ch = 0
while True:
    print("x : ", x, "y : ", y, "pay : ", pay)
    print("[1.방향설정하기] [2.이동하기] [0.영업종료]")
    ch = int(input())

    if dir == "동":
        x += speed
    elif dir == "서":
        x -= speed
    elif dir == "남":
        y -= speed
    else:
        y += speed

    if x == rx and y == ry:
        break

    if ch == 0:
        print("영업종료")
        break

    elif ch == 1:
        print("[1.방향설정하기]")
        print("[1.동] [2.서] [3.남] [4.북]")
        ch = int(input())
        dir = ch
        if dir == 1:
            dir = "동"
        elif dir == 2:
            dir = "서"
        elif dir == 3:
            dir = "남"
        else:
            dir = "북"
        continue

    elif ch == 2:
        print("[2.이동하기]")
        print("[1.한칸이동] [2.두칸이동] [3.세칸이동]")
        ch = int(input())
        speed = ch
        pay += 50 * speed
        continue

print(x, y, pay)
