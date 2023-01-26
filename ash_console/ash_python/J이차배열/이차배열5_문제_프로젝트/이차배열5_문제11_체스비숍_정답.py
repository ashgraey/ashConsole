'''
	[문제]
		세로 가로 인덱스 두 개를 랜덤으로 저장한다. 
		그 인덱스를 기점으로 대각선 방향으로 전부 1로 채운 후 출력하시오.
		    
		[예]
			y = 2
			x = 1
		    	
			[0,0,0,1,0]
			[1,0,1,0,0]
			[0,1,0,0,0]
			[1,0,1,0,0]
			[0,0,0,1,0]
'''

import random

list = [
	[0, 0, 0, 0, 0],
	[0, 0, 0, 0, 0],
	[0, 0, 0, 0, 0],
	[0, 0, 0, 0, 0],
	[0, 0, 0, 0, 0]
]

y = random.randint(0, 4)
x = random.randint(0, 4)
list[y][x] = 1
print("y =", y, ", x =", x)

tempY = y
tempX = x
while True:
	if tempY - 1 >= 0 and tempX - 1 >= 0:
		list[tempY - 1][tempX - 1] = 1
		tempY -= 1
		tempX -= 1
	else:
		break

tempY = y
tempX = x
while True:
	if tempY - 1 >= 0 and tempX + 1 < 5:
		list[tempY - 1][tempX + 1] = 1
		tempY -= 1
		tempX += 1
	else:
		break

tempY = y
tempX = x
while True:
	if tempY + 1 < 5 and tempX - 1 >= 0:
		list[tempY + 1][tempX - 1] = 1
		tempY += 1
		tempX -= 1
	else:
		break

tempY = y
tempX = x
while True:
	if tempY + 1 < 5 and tempX + 1 < 5:
		list[tempY + 1][tempX + 1] = 1
		tempY += 1
		tempX += 1
	else:
		break

for i in range(len(list)):
	print(list[i])
