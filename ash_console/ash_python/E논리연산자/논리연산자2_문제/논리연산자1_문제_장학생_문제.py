'''
	[문제] 
		국어점수가 100점이거나 수학 점수가 100점이면 장학생이다.
		아래는 철수의 점수이다.
		철수가 장학생이면 True 출력하시오.
	[정답]
		False
'''
국어 = 99
수학 = 99

장학생 = 국어 == 100 or 수학 == 100
print(장학생)