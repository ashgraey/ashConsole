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

rankList = []
i = 1
while i <= 3:
	rank = []
	j = 0
	while j <= 3:
		count = 0
		k = 0
		while k <= 3:
			if score[j][i] <= score[k][i]:
				print(score[j][i], score[k][i])
				count += 1
			k += 1
		rank.append(count)
		j += 1
	rankList.append(rank)
	i += 1
print(rankList)

total = []
for i in range(4):
	tot = 0
	for j in range(3):
		tot += rankList[j][i]
	total.append(tot)
print(total)

rank = []
for i in range(len(total)):
	count = 1
	for j in range(len(total)):
		if total[i] > total[j]:
			count += 1
	rank.append(count)
print(rank)

for i in range(len(score)):
	score[i][4] = rank[i]

for i in range(len(score)):
	print(score[i])
