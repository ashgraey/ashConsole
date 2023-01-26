'''
	[문제]
		a리스트에 -100~100 사이의 랜덤 값 5개 저장한다. 
		그 중 가장 큰 수와 가장 작은 수를 출력하시오. 
	[예시]
		[37, 53, 90, -82, -17]
		90
		-82
'''

import random

a = []

for i in range(5):
	r = random.randint(-100, 100)
	a.append(r)
print("a =", a)

max = 0
min = 100
for i in range(len(a)):
	if max < a[i]:
		max = a[i]
	if min > a[i]:
		min = a[i]
		
print("max = ", max)
print("min = ", min)







