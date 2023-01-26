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
'''
idx = 2 1
			0 3 
1 0		1 2 
	2 1
3 0 	3 2 
			4 3 

왼 대각(위) : y -= 1, x -= 1
왼 대각(아래) : y += 1, x += 1

오른 대각(위) : y -= 1, x += 1 
오른 대각(아래) : y += 1, x-= 1 
'''
import random

list = [
	[0, 0, 0, 0, 0],
	[0, 0, 0, 0, 0],
	[0, 0, 0, 0, 0],
	[0, 0, 0, 0, 0],
	[0, 0, 0, 0, 0]
]
# 0118
y = random.randint(0, len(list) - 1)
x = random.randint(0, len(list) - 1)
# x = 2 
# y = 2
print("y : ", y, "x : ", x)

tempY = y
tempX = x

list[tempY][tempX] = 1

# 왼 대각(상) \ 
while True : 
	tempY -= 1
	tempX -= 1 
		
	if tempY > len(list) - 1 or tempY < 0 or tempX > len(list) - 1 or tempX < 0 :
		break

	list[tempY][tempX] = 1

# 왼 대각(하) \ 
tempY = y
tempX = x
while True : 
	tempY += 1
	tempX += 1 
		
	if tempY > len(list) - 1 or tempY < 0 or tempX > len(list) - 1 or tempX < 0 :
		break

	list[tempY][tempX] = 1

# 우 대각(상) / 
tempY = y
tempX = x
while True : 
	tempY -= 1
	tempX += 1 
		
	if tempY > len(list) - 1 or tempY < 0 or tempX > len(list) - 1 or tempX < 0 :
		break

	list[tempY][tempX] = 1

# 우 대각(하) /
tempY = y
tempX = x
while True : 
	tempY += 1
	tempX -= 1 
		
	if tempY > len(list) - 1 or tempY < 0 or tempX > len(list) - 1 or tempX < 0 :
		break

	list[tempY][tempX] = 1


# 출력
for i in range(len(list)) :
	print(list[i])
		
# 1219
# 이차반복으로 풀어도 결과가 나오긴한다.
# y = random.randint(0, len(list) - 1)
# x = random.randint(0, len(list) - 1)
# print("y : ", y, "x : ", x)

# tempY = y
# tempX = x

# list[tempY][tempX] = 1

# # 왼대각 위 \
# for i in range(len(list)) :
# 	for j in range(len(list[i])) :
# 		if tempY - 1 >= 0 and tempX - 1 >= 0 :
# 			tempY -= 1 
# 			tempX -= 1
# 			list[tempY][tempX] = 1 
# # 왼대각 아래 \
# tempY = y
# tempX = x
# for i in range(len(list)) :
# 	for j in range(len(list[i])) :
# 		if tempY + 1 < len(list) and tempX + 1 < len(list) :
# 			tempY += 1 
# 			tempX += 1
# 			list[tempY][tempX] = 1 
# # 오른대각 위 /
# tempY = y
# tempX = x
# for i in range(len(list)) :
# 	for j in range(len(list[i])) :
# 		if tempY - 1 >= 0 and tempX + 1 < len(list) :
# 			tempY -= 1 
# 			tempX += 1
# 			list[tempY][tempX] = 1
# # 오른대각 아래 /
# tempY = y
# tempX = x
# for i in range(len(list)) :
# 	for j in range(len(list[i])) :
# 		if tempY + 1 < len(list) and tempX - 1 >= 0 :
# 			tempY += 1 
# 			tempX -= 1
# 			list[tempY][tempX] = 1

# for i in range(len(list)) :
# 	print(list[i])

# 2차
# lastIdx = len(list) - 1
# size = len(list)
# y = random.randint(0, lastIdx)
# x = random.randint(0, lastIdx)
# print("y : ", y, "x : ", x)

# tY = y 
# tX = x
# list[tY][tX] = 1 

# # 왼 대각(위)
# while True :
# 	if tY - 1 >= 0 and tX - 1 >= 0 :
# 		list[tY - 1][tX - 1] = 1 
# 		tY -= 1 
# 		tX -= 1
# 	else : 
# 		break
	
# 1차
# 원리는 풀었지만 
# 코드로 구현하지 못함 ㅜㅜ
# y = random.randint(0, len(list) - 1)
# x = random.randint(0, len(list) - 1)
# list[y][x] = 1
# print("y : ", y, "x : ", x)


# tempY = y
# tempX = x
# # 왼대각(위)
# while True :
# 	if tempY - 1 >= 0 and tempX - 1 >= 0 :
# 		list[tempY - 1][tempX - 1] = 1
# 		tempY -= 1
# 		tempX -= 1
# 	else :
# 		break  

# tempY = y
# tempX = x
# size = len(list) - 1
# # 왼대각(아래)
# while True :
# 	if tempY + 1 <= size and tempX + 1 <= size :
# 		list[tempY + 1][tempX + 1] = 1
# 		tempY += 1
# 		tempX += 1
# 	else :
# 		break  

# tempY = y
# tempX = x
# size = len(list) - 1
# # 오른 대각(위)
# while True :
# 	if tempY - 1 >= 0 and tempX + 1 <= size :
# 		list[tempY - 1][tempX + 1] = 1
# 		tempY -= 1
# 		tempX += 1
# 	else :
# 		break  

# tempY = y
# tempX = x
# size = len(list) - 1
# # 오른 대각(아래)
# while True :
# 	if tempY + 1 <= size and tempX - 1 >= 0 :
# 		list[tempY + 1][tempX - 1] = 1
# 		tempY += 1
# 		tempX -= 1
# 	else :
# 		break  


# for i in range(len(list)) :
# 	print(list[i])
