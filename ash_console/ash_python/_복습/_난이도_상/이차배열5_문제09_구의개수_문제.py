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

# 값이 0인 인덱스의 위치
mY = 0
mX = 0
for i in range(len(mine)) :
	for j in range(len(mine[i])) :
		if mine[i][j] == 0 :
			mY = i
			mX = j
			print(mY,mX)		