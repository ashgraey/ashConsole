'''
	[문제]
		3과목의 평균이 60점 이상이면 합격이다.
		단, 평균이 합격일지라도, 어느 한 과목이 50점 미만이면 불합격이다.
		아래 시험점수는 합격인지 구하시오.
	[정답]
		False
'''

kor = 100
eng = 87
math = 49

avg = (kor + eng + math) / 3
print(avg >= 60 and kor >= 50 and eng >= 50 and math >= 50)