'''
	[문제]
		위 데이터는 학생 4명의 데이터이다.
		순서대로 [번호], [국어], [수학], [영어], [등수]의 데이터이다. 		
		이제 등수를 넣어야한다. 각 과목별 등수별로 점수를 매기고 
		각 점수들의 합이 가장적은 학생이 1등이다. 
		총합이 같으면 같은 등수이다. 

		1번학생은 국어 4등, 수학3등, 영어2등으로 점수는 9점이다. 
		2번학생은 국어 3등, 수학1등, 영어3등으로 점수는 7점이다.
		3번학생은 국어 2등, 수학4등, 영어1등으로 점수는 7점이다.
		4번학생은 국어 1등, 수학2등, 영어4등으로 점수는 7점이다.

		1등은 3명, 4등은 1명이다. 
	[정답]
		[1001, 20, 43, 54, 4],
		[1002, 21, 73, 44, 1],
		[1003, 65, 13, 55, 1],
		[1004, 76, 63,  4, 1]
'''
score = [
			[1001, 20, 43, 54, 0],
			[1002, 21, 73, 44, 0],
			[1003, 65, 13, 55, 0],
			[1004, 76, 63,  4, 0]
		]

# 0117 
# 과목별 일차원 리스트에 담기
# tempList = []
# for i in range(1, len(score)) :
# 	temp = []
# 	for j in range(4) :
# 		temp.append(score[j][i])

# 	tempList.append(temp)

# for i in range(len(tempList)) :
# 	print(tempList[i])

# # 과목별 석차
# scList = []
# for i in range(len(tempList)) :

# 	sc = []
# 	for j in range(4) :
# 		cnt = 0 
# 		for k in range(4) :
# 			if tempList[i][j] <= tempList[i][k] :
# 				cnt += 1
# 		sc.append(cnt)
# 	scList.append(sc)

# for i in range(len(scList)) :
# 	print(scList[i])

# # 스코어 합산
# scTot = []
# for i in range(4) :	
# 	tot = 0
# 	for j in range(len(scList)) :
# 		tot += scList[j][i]
# 	scTot.append(tot)

# print(scTot)

# # 스코어 석차
# for i in range(len(scTot)) :
# 	cnt = 1
# 	for j in range(len(scTot)) :
# 		if scTot[i] > scTot[j] :
# 			cnt += 1 
# 	score[i][-1] = cnt

# print()
# for i in range(len(score)) :
# 	print(score[i])



# 1219
# 등수구하기
# tempList = []
# for i in range(len(score)) :
# 	temp = []
# 	for j in range(1, 4) :
# 		cnt = 1 
# 		for k in range(len(score)) :
# 			if score[i][j] < score[k][j] :
# 				cnt += 1 
# 		temp.append(cnt)
# 	tempList.append(temp)
# print(tempList)

# # 등수 합산 구하기
# total = []
# for i in range(len(tempList)) :
# 	tot = 0 
# 	for j in range(len(tempList[i])) :
# 		tot += tempList[i][j]
# 	total.append(tot)
# print(total)

# # 합산으로 다시 등수 구하기
# # 등수 합산이 낮은게 등수가 더 높다
# for i in range(len(total)) :
# 	cnt = 1
# 	for j in range(len(total)) :
# 		if total[i] > total[j] :
# 			cnt += 1 
# 	score[i][-1] = cnt

# for i in range(len(score)) :
# 	print(score[i])

# 1213
# 세로비교, 각 점수별로 석차가 필요함
# rankList = []
# for i in range(len(score) - 1) :
# 	rank = []

# 	for j in range(len(score)) :
# 		cnt = 0
# 		for k in range(len(score)) :
# 			if score[j][i + 1] <= score[k][i + 1] :
# 				cnt += 1
# 		rank.append(cnt)
# 	rankList.append(rank)

# # 등수의 토탈 점수를 따로 리스트에 저장
# total = []
# for i in range(4) :
# 	tot = 0
# 	for j in range(3) :
# 		tot += rankList[j][i]
	
# 	total.append(tot)

# print("total : ", total)

# # score 인덱스에 석차 저장 및 출력
# for i in range(len(total)) :
# 	cnt = 1 
# 	for j in range(len(total)) :
# 		if total[i] > total[j] :
# 			cnt += 1 
# 	# print(cnt)
# 	score[i][4] = cnt
# 	print(score[i])

# 1차
# 1 : 각 과목별 등수
# 세로줄 석차를 구하기위해 반복문을 총 세번 중첩시켜야함 
# 아직은 잘 안 됨
# rankList = []
# i = 1 
# while i <= 3 :
# 	rank = []
# 	j = 0 
# 	while j < 4 :
# 		cnt = 0
# 		k = 0
# 		while k < 4 :
# 			if score[j][i] <= score[k][i] :
# 				print(score[k][i], end = " ")
# 				cnt += 1
# 			k += 1 
# 		rank.append(cnt)
# 		j += 1
# 	rankList.append(rank)
# 	i += 1	

# print()
# for i in range(len(rankList)) :
# 	print(rankList[i])

# tot = []
# for i in range(4) :
# 	total = 0 
# 	for j in range(len(rankList)) :
# 		total += rankList[j][i]
# 	tot.append(total)

# print(tot)

# temp = []
# for i in range(len(tot)) : 
# 	cnt = 0
# 	for j in range(len(tot)) :
# 		if tot[i] <= tot[j] :
# 			cnt += 1
# 	temp.append(cnt)
# print()
# print(temp)

# for i in range(len(score)) :
# 	score[i][len(score[i]) - 1] = temp[i]

# print()
# for i in range(len(score)) :
# 	print(score[i])


