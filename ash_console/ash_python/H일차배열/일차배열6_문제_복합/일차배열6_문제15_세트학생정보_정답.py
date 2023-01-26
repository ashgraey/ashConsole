'''
	[문제]
		아래 배열은 3명의 학생 데이터이다.		
		각 학생은 3개씩 데이터로 표현한다. 
		맨 앞은 번호, 그다음은 국어점수, 그다음은 수학점수이다.					
		(예) 
			1001번, 국어 100, 수학 20
			1002번, 국어 32,  수학 54
			1003번  국어 34,  수학 65	

		[1] 전체 평균을 출력하시오.
		[2] 국어 1등 학생을 출력하시오.
		[3] 수학 1등 학생을 출력하시오.
		[4] 전체 1등 학생을 출력하시오.
'''

a = [1001, 100, 20, 1002, 32, 54, 1003, 34, 65]

total = 0
for i in range(len(a)):
	if i % 3 == 0:
		total = total + a[i + 1] + a[i + 2]
avg = total / 3
print("평균 =", avg)

korMax = 0
korIndex = 0
mathMax = 0
mathIndex = 0

for i in range(len(a)):
	if i % 3 == 1:
		if korMax < a[i]:
			korMax = a[i]
			korIndex = i
	if i % 3 == 2:
		if mathMax < a[i]:
			mathMax = a[i]
			mathIndex = i
print("국어 1등 =", a[korIndex - 1], korMax)
print("수학 1등 =", a[mathIndex - 2], mathMax)
