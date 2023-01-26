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

# 십자가
for i in range(len(list)):
	list[y][i] = 1
	list[i][x] = 1

# 대각선 \ : (행 감소, 열 감소) (행 증가, 열 증가)
# 대각선 / : (행 감소, 열 증가) (행 증가, 열 감소)
i = y
j = x
while i >= 0 and j >= 0:
	list[i][j] = 1
	i -= 1
	j -= 1

i = y
j = x
while i < len(list) and j < len(list):
	list[i][j] = 1
	i += 1
	j += 1

i = y
j = x
while i >= 0 and j < len(list):
	list[i][j] = 1
	i -= 1
	j += 1

i = y
j = x
while i < len(list) and j >= 0:
	list[i][j] = 1
	i += 1
	j -= 1

for i in range(len(list)):
	print(list[i])












	