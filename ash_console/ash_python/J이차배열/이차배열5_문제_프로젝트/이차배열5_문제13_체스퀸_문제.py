'''
	[문제]
		세로 가로 인덱스 두개를 랜덤으로 저장한다. 
		그 인덱스를 기점으로 대각선 + 십자가 방향으로 전부 1로 채운후 출력하시오.
		
		[예]
			y = 3 , x = 0
			
			[1, 0, 0, 1, 0]
			[1, 0, 1, 0, 0]
			[1, 1, 0, 0, 0]
			[1, 1, 1, 1, 1]
			[1, 1, 0, 0, 0]
'''
'''
대각(우상) : x += 1, y -= 1
대각(우하) : x += 1, y += 1 
대각(좌상) : x -= 1, y -= 1 
대각(좌하) : x -= 1, y += 1

0 0 			0 4 
	1 1		1 3
		2 2
	3 1 	3 3 
4 0 			4 4 
'''
import random 

list = [
	[0, 0, 0, 0, 0],
	[0, 0, 0, 0, 0],
	[0, 0, 0, 0, 0],
	[0, 0, 0, 0, 0],
	[0, 0, 0, 0, 0]
]
# # 0118
y = random.randint(0, len(list) - 1)
x = random.randint(0, len(list) - 1)
# y = 2 
# x = 2
print("y : ", y, "x : ", x)
# list[y][x] = 1 

# 체스킹(십자가)
tempY = y
tempX = x
for i in range(len(list)) :
	list[tempY][i] = 1
	list[i][tempX] = 1

# 대각(상) \ 
tempY = y
tempX = x
for i in range(len(list)) :
	tempY -= 1 
	tempX -= 1 

	if tempY < 0 or tempX < 0 or tempY >= len(list) or tempX >= len(list) :
		break 

	list[tempY][tempX] = 1

# 대각(하) \ 
tempY = y
tempX = x
for i in range(len(list)) :
	tempY += 1 
	tempX += 1 

	if tempY < 0 or tempX < 0 or tempY >= len(list) or tempX >= len(list) :
		break 

	list[tempY][tempX] = 1

# 대각(상) /
tempY = y
tempX = x
for i in range(len(list)) :
	tempY -= 1 
	tempX += 1 

	if tempY < 0 or tempX < 0 or tempY >= len(list) or tempX >= len(list) :
		break 

	list[tempY][tempX] = 1

# 대각(하) /
tempY = y
tempX = x
for i in range(len(list)) :
	tempY += 1 
	tempX -= 1 

	if tempY < 0 or tempX < 0 or tempY >= len(list) or tempX >= len(list) :
		break 

	list[tempY][tempX] = 1
   
# 출력
for i in range(len(list)) :
	print(list[i]) 

# 1219
# y = random.randint(0, len(list) - 1)
# x = random.randint(0, len(list) - 1)
# print("y : ", y, "x : ", x) 
# # y = 2 
# # x = 2
# tempY = y 
# tempX = x
# # 가로 / 세로
# for i in range(len(list)) :
# 	list[tempY][i] = 1 
# 	list[i][tempX] = 1 

# # \ 좌대각 상 
# tempY = y 
# tempX = x
# while True :
# 	if tempY - 1 >= 0 and tempX - 1 >= 0 :
# 		tempY -= 1
# 		tempX -= 1 
# 		list[tempY][tempX] = 1 
# 	else :
# 		break

# # 좌대각 하
# tempY = y 
# tempX = x
# while True :
# 	if tempY - 1 >= 0 and tempX + 1 < len(list) :
# 		tempY -= 1
# 		tempX += 1 
# 		list[tempY][tempX] = 1 
# 	else :
# 		break

# # 우대각 상 
# tempY = y 
# tempX = x
# while True :
# 	if tempY + 1 < len(list) and tempX - 1 >= 0 :
# 		tempY += 1
# 		tempX -= 1 
# 		list[tempY][tempX] = 1 
# 	else :
# 		break

# # 우대각 하
# tempY = y 
# tempX = x
# while True :
# 	if tempY + 1 < len(list) and tempX + 1 < len(list) :
# 		tempY += 1
# 		tempX += 1 
# 		list[tempY][tempX] = 1 
# 	else :
# 		break
 
# for i in range(len(list)) :
# 	print(list[i])
 
# 1차
# y = random.randint(0, len(list) - 1)
# x = random.randint(0, len(list) - 1)
# print("y : ", y, "x : ", x)

# # 십자
# for i in range(len(list)) :
# 	list[y][i] = 1
# 	list[i][x] = 1

# size = len(list)
# # 대각(우상) 
# tempY = y
# tempX = x
# for i in range(len(list)) :
# 	if 0 <= tempX - 1 and tempY + 1 < size :
# 		list[tempY + 1][tempX - 1] = 1
# 		tempY += 1 
# 		tempX -= 1
# 	else :
# 		break 

# # 대각(우하)
# tempY = y
# tempX = x
# for i in range(len(list)) :
# 	if tempX + 1 < size and tempY + 1 < size :
# 		list[tempY + 1][tempX + 1] = 1
# 		tempY += 1 
# 		tempX += 1
# 	else :
# 		break 

# # 대각(좌상)
# tempY = y
# tempX = x
# for i in range(len(list)) :
# 	if 0 <= tempX - 1 and 0 <= tempY - 1 :
# 		list[tempY - 1][tempX - 1] = 1
# 		tempY -= 1 
# 		tempX -= 1
# 	else :
# 		break 

# # 대각(좌하)
# tempY = y
# tempX = x
# for i in range(len(list)) :
# 	if tempX + 1 < size  and 0 <= tempY - 1  :
# 		list[tempY - 1][tempX + 1] = 1
# 		tempY -= 1 
# 		tempX += 1
# 	else :
# 		break 

# for i in range(len(list)) :
# 	print(list[i])















	