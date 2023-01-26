'''
	[문제]
		(1) 현재 인덱스의 값이  나머지 값들을 검사한다.
		(2) 제일 큰 값을 찾아서 현재의 값과 교환한다.
		(3) 인덱스 1증가한다.
		(4) (1~3)을 끝까지 반복한다.

		10, 50, 30, 40, 80, 19   ==> 80을 찾아내고 교환한다.
		80, 50, 30, 40, 10, 19   ==> 50은 나머지 중 이미 제일크다.
		80, 50, 30, 40, 10, 19   ==> 40을 찾아내고 교환한다.
		80, 50, 40, 30, 10, 19   ==> 30은 나머지 중 이미 제일크다.
		80, 50, 40, 30, 10, 19   ==> 19을 찾아내고 교환한다.
		80, 50, 40, 30, 19, 10	
'''
score = [10, 50, 30, 40, 80, 19]

i = 0
while i < len(score):

	max = score[i]
	maxIndex = i

	j = i
	while j < len(score):
		if max < score[j]:
			max = score[j]
			maxIndex = j
		j += 1
		
	temp = score[i]
	score[i] = score[maxIndex]
	score[maxIndex] = temp

	i += 1

print(score)