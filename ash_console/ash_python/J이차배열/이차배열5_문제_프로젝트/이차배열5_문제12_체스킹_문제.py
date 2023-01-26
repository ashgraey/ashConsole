'''
	[문제]
		세로 가로 인덱스 두개를 랜덤으로 저장한다. 
		그 인덱스를 기점으로 십자가 방향으로 전부 1로 채운후 출력하시오.
		
		[예]
			y = 1 , x = 4
			[0, 0, 0, 0, 1]
			[1, 1, 1, 1, 1]
			[0, 0, 0, 0, 1]
			[0, 0, 0, 0, 1]
			[0, 0, 0, 0, 1]
'''
'''
		 04
11 12 13 14
		 24 
		 34
		 44
가로 : (왼)y += 0, x -= 1 (오른)y y += 0, x += 1 
세로 : (아래) y += 1, x += 0, (위) y -= 1, x += 0
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

print("y : ", y, "x : ", x)

# 가로 좌
tempY = y
tempX = x
for i in range(len(list)) :
	if tempX >= 0 :
		list[tempY][tempX] = 1
		tempX -= 1 

# 가로 우
tempY = y
tempX = x
for i in range(len(list)) :
	if tempX < len(list) :
		list[tempY][tempX] = 1
		tempX += 1

# 세로 상
tempY = y
tempX = x
for i in range(len(list)) :
	if tempY >= 0 :
		list[tempY][tempX] = 1
		tempY -= 1
# 세로 하
tempY = y
tempX = x
for i in range(len(list)) :
	if tempY < len(list) :
		list[tempY][tempX] = 1
		tempY += 1

# 출력
for i in range(len(list)) :
	print(list[i])


# # 1219
# # 허탈...
# y = random.randint(0, len(list) - 1)
# x = random.randint(0, len(list) - 1)
# print("y : ", y, "x : ", x)

# tempY = y
# tempX = x
# list[tempY][tempX] = 1 

# # 가로
# tempY = y
# tempX = x
# for i in range(len(list)) :
# 	if tempX - 1 >= 0 :
# 		tempX -= 1 
# 		list[tempY][tempX] = 1 

# tempY = y
# tempX = x
# for i in range(len(list)) :
# 	if tempX + 1 < len(list) :
# 		tempX += 1 
# 		list[tempY][tempX] = 1 

# # 세로
# tempY = y
# tempX = x
# for i in range(len(list)) :
# 	if tempY - 1 >= 0 :
# 		tempY -= 1 
# 		list[tempY][tempX] = 1 

# tempY = y
# tempX = x
# for i in range(len(list)) :
# 	if tempY + 1 < len(list) :
# 		tempY += 1 
# 		list[tempY][tempX] = 1 
# for i in range(len(list)) :
# 	print(list[i])


# y = random.randint(0, len(list) - 1)
# x = random.randint(0, len(list) - 1)
# print("y : ", y, "x : ", x)
# list[y][x] = 1


# tempY = y
# tempX = x
# # 왼 가로
# while True :
# 	if 0 <= tempY < len(list) and tempX - 1 >= 0 :
# 		list[tempY][tempX - 1] = 1
# 		tempX -= 1
# 	else :
# 		break

# tempY = y
# tempX = x
# # 오른 가로
# while True :
# 	if 0 <= tempY < len(list) and tempX + 1 < len(list) :
# 		list[tempY][tempX + 1] = 1
# 		tempX += 1
# 	else :
# 		break

# tempY = y
# tempX = x
# # 아래 세로
# while True :
# 	if tempY + 1 < len(list) and 0 <= tempX < len(list) :
# 		list[tempY + 1][tempX] = 1
# 		tempY += 1
# 	else :
# 		break

# tempY = y
# tempX = x
# # 위 세로
# while True :
# 	if tempY - 1 >= 0 and 0 <= tempX < len(list) :
# 		list[tempY - 1][tempX] = 1
# 		tempY -= 1
# 	else :
# 		break

# for i in range(len(list)) :
# 	print(list[i])




