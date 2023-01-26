'''
	[문제]
		철수는 두 번의 시험에서 각각 80점과 72점을 받았다.
		세 번째 시험에서 최소 몇 점 이상을 받아야 
		
		세 번의 시험성적의 평균이 82점 이상이 될 수 있을까?
		시험점수는 1점 단위로 설정된다.
	[정답]
		94
'''

score1 = 80
score2 = 72
score3 = 0

avg = 82

run = 1
while run == 1:
	if (score1 + score2 + score3) / 3 >= avg:
		print(score3)
		run = 0
	if (score1 + score2 + score3) / 3 < avg:
		score3 += 1
	

