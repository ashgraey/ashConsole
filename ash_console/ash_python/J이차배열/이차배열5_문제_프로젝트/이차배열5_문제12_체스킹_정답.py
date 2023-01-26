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

'''
	세로 : 열이 정해진 것
	가로 : 행이 정해진 것
'''
for i in range(len(list)):
	list[i][x] = 1
	list[y][i] = 1

for i in range(len(list)):
	print(list[i])


