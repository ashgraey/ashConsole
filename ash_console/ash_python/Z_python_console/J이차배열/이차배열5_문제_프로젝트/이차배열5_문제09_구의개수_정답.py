'''
	[문제]
		mine리스트 숫자 0의 자리에 숫자를 저장하려 한다.
	 	저장할 숫자는 주변 8방향을 검사 후 9의 개수를 저장해야 한다.
		저장 후 mine리스트를 출력하시오.
			
	[정답]
		   [2,9,2],
		   [9,4,9],
		   [1,3,9]
	
	 
'''

mine = [
	[0, 9, 0],
	[9, 0, 9],
	[0, 0, 9]
]

'''
(-1 , -1 )( -1 , 0 )( -1 , 1 )
( 0 , -1 )(  0 , 0 )(  0 , 1 )
( 1 , -1 )(  1 , 0 )(  1 , 1 )

i = -1
while i <= 1:
	j = -1
	while j <= 1:
		print("(" , i , "," , j , ")", end="")
		j += 1
	i += 1
	print()
'''
'''
( 0 , 0 )( 0 , 1 )( 0 , 2 )
( 1 , 0 )( 1 , 1 )( 1 , 2 )
( 2 , 0 )( 2 , 1 )( 2 , 2 )
y = 0
while y < 3:
	x = 0
	while x < 3:
		print("(", y, ",", x, ")", end="")
		x += 1
	y += 1
	print()
'''

for y in range(3):
	for x in range(3):
		if mine[y][x] == 0:
			i = -1
			while i <= 1:
				j = -1
				while j <= 1:
					if (0 <= y + i and y + i < 3) and (0 <= x + j and x + j < 3):
						if mine[y + i][x + j] == 9:
							mine[y][x] += 1
					j += 1
				i += 1


for i in range(len(mine)):
	print(mine[i])