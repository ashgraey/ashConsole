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

# 0117
# tempList = []
# for i in range(5) :
# 	temp = []
# 	for j in range(5) :
# 		temp.append(0)
# 	tempList.append(temp)

# # print(tempList)
# # 8방향 검사하기 편하도록 더 큰 list안에 mine을 넣는다.
# for i in range(len(mine)) :
# 	for j in range(len(mine)) :	
# 		tempList[i + 1][j + 1] = mine[i][j]


# for i in range(1, 4) :
# 	for j in range(1, 4) :
# 		if tempList[i][j] == 0 : 
# 			y = i
# 			x = j

# 			# 8방향 검사
# 			m = 0
# 			for k in range(3) :
# 				for l in range(3) :
# 					if tempList[(k + y) - 1][(l + x) - 1] == 9 :
# 						m += 1
# 			mine[y - 1][x - 1] = m
# 			# print(m)

# # 출력
# for i in range(len(mine)) :
# 	print(mine[i])
				
# 1219
# 00 02 11 20 21 
# 00 => 01 10 11
# 02 => 01 12 11
# 11 => 00 01 02 10 12 20 21 22 
# 20 => 10 11 21 
# 21 => 10 11 12 

# # 5 * 5사이즈의 복사배열 만들기
# tempList = []
# for i in range(len(mine) + 2) :
# 	temp = []
# 	for j in range(len(mine) + 2) :
# 		temp.append(0)
# 	tempList.append(temp)

# # for i in range(len(tempList)) :
# # 	print(tempList[i])

# # 복사배열의 중앙에 mine 복사
# for i in range(1, len(tempList) - 1) :
# 	for j in range(1, len(tempList) - 1) :
# 		tempList[i][j] = mine[i - 1][j - 1]

# for i in range(len(tempList)) :
# 	print(tempList[i])

# for i in range(len(mine)) :
# 	for j in range(len(mine[i])) :
# 		if mine[i][j] == 0 :
# 			y = i 
# 			x = j 
# 			# print(x,y)
			
# 			# 가로검사
# 			# 8방향 전체 검사
# 			cnt = 0
# 			for k in range(3) :
# 				for l in range(3) :
# 					if tempList[k + y][l + x] == 9 :
# 						cnt += 1 
# 				mine[y][x] = cnt
					
# 					# print(cnt) 
# 			# # 세로 검사
# 			# cnt = 0
# 			# for k in range(3) :
# 			# 	for l in range(3) :
# 			# 		if tempList[l][k] == 9 :
# 			# 			mine[y][x] += 1

# 			# # 대각 검사 \, 00 11 22 
# 			# for k in range(3) :
# 			# 	if tempList[k][k] == 9 :
# 			# 		mine[y][x] += 1
# 			# # 대각 검사 /
# 			# for k in range(3) :
# 			# 	if tempList[k][(2 - k)] == 9 :
# 			# 		mine[y][x] += 1

# print()
# for i in range(len(mine)) :
# 	print(mine[i])
			
# 1213
# 8방향 검사를 용이하게 하기위해
# 길이가 5 * 5인 이차배열을 새로 생성
# sample = []
# for i in range(len(mine) + 2) :
# 	sample1 = []
# 	for j in range(len(mine) + 2) :
# 		sample1.append(0)
# 	sample.append(sample1)


# # sample의 중간 위치에 복사
# print()
# for i in range(len(mine)) :
# 	for j in range(len(mine[i])) :
# 		sample[i + 1][j + 1] = mine[i][j]
# 	# print(sample[i])

# # 8방향 검사
# y = 1
# while y <= 3 :
 
# 	x = 1 
# 	while x <= 3 :
# 		if sample[y][x] == 0 :
# 			cnt = 0
# 			# 좌 가로
# 			if sample[y][x - 1] == 9 :
# 				cnt += 1
# 			# 우 가로 
# 			if sample[y][x + 1] == 9 :
# 				cnt += 1 
# 			# 상 세로
# 			if sample[y - 1][x] == 9 :
# 				cnt += 1 
# 			# 하 세로
# 			if sample[y + 1][x] == 9 :
# 				cnt += 1 
# 			# 우 대각 : 11 -> 02
# 			if sample[y - 1][x + 1] == 9 :
# 				cnt += 1
# 			if sample[y + 1][x - 1] == 9 :
# 				cnt += 1  
# 			# 좌 대각 : 11 -> 00
# 			if sample[y - 1][x - 1] == 9 :
# 				cnt += 1 
# 			if sample[y + 1][x + 1] == 9 :
# 				cnt += 1 
# 			sample[y][x] = cnt
# 		x += 1 
# 	y += 1 

# # mine으로 복사
# for i in range(len(sample)) :
# 	print(sample[i])

# for i in range(len(mine)) :
# 	for j in range(len(mine[i])) :
# 		mine[i][j] = sample[i + 1][j + 1]

# # 출력
# print()
# for i in range(len(mine)) :
# 	print(mine[i])

# 1차 시도 : 모르겠당
# 값이 0인 인덱스의 위치
# mY = 0
# mX = 0
# for i in range(len(mine)) :
# 	for j in range(len(mine[i])) :
# 		if mine[i][j] == 0 :
# 			mY = i
# 			mX = j
# 			print(mY,mX)

# 			cnt = 0
# 			# 가로검사
# 			for i in range(len(mine)) :
# 				for j in range(len(mine[i])) :
# 					if mine[mY][j] != 0 :
# 						cnt += 1

# 					if mine[j][mX] != 0 : 
# 						cnt += 1 
					
# 					if mine
					
					 