'''
	[문제]
		1. 랜덤(0~4)를 하나를 선택한다. 
		2. 숫자0 을 만나면 그냥 아래로 내려간다.
		3. 숫자1 을 만나면 오른쪽으로 이동 후 내려간다.
		4. 숫자2 를 만나면 완쪽으로 이동 후 내려간다.
		5. 오늘의 메뉴를 출력하시오.
	[정답]
		r = 0, 된장찌개	
		r = 1, 돈까스
		r = 2, 떡라면
		r = 3, 짜장면
		r = 4, 쫄면
'''
import random

menu = ["떡라면", "돈까스","짜장면", "쫄면", "된장찌개"]

ladder= [
		[0,0,0,0,0],
		[1,2,0,1,2],
		[0,1,2,0,0],
		[0,0,1,2,0],
		[1,2,0,1,2],
		[0,1,2,0,0],
		[0,1,2,0,0],
		[0,0,1,2,0],
		[0,0,0,0,0]
	]

rIndex = random.randint(0, 4)
print("rIndex =", rIndex)

rY = 0
rX = rIndex
for i in range(len(ladder)):
	if rX + 1 < 5 and ladder[rY][rX] == 1:
		rX += 1
	elif rX - 1 >= 0 and ladder[rY][rX] == 2:
		rX -= 1
	rY += 1

print(menu[rX])