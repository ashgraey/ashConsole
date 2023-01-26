'''
	[문제]
		1. 10회 반복을 한다.
		2. 0~100 사이의 랜덤 숫자를 출력한다. (학생 점수)
		3. 번호는 1번부터 시작한다. 번호와 점수를 출력한다. 
		4. 성적이 60점 이상이면 합격생이다. 
		   합격생은 점수 옆에 [합격]을 불합격생은 [불합격]을 출력한다. 
		5. 전교생(10명)의 총점과 평균을 출력한다.
		6. 1등의 번호와 점수를 출력한다.
'''

import random

total = 0

maxScore = 0
maxIndex = 0

i = 1
while i <= 10:
    score = random.randint(0, 100)

    if maxScore < score:
        maxScore = score
        maxIndex = i

    total += score

    if score >= 60:
        print(score, "[합격]")
    if score < 60:
        print(score, "[불합격]")
    
    i += 1

avg = total / 10
print("총점 =", total)
print("평균 =", avg)
print("1등 =", maxScore, ":", maxIndex)