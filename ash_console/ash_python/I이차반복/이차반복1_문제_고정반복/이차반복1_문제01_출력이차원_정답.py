'''
	[문제]
		3~6 사이의 랜덤 숫자 하나를 저장하고 그 숫자만큼 아래와 같은 규칙으로 출력하시오.
		단, 일차 반복문과 이차 반복문으로 출력하시오.
 	[예시]
		r = 6
	[출력]
		1 1 1
		2 2 2
		3 3 3
		4 4 4
		5 5 5
		6 6 6
'''

import random

r = random.randint(3, 6)
print("r =", r)

for i in range(r):
	num = i + 1
	print(num, num, num)

print("----------")

for i in range(r):
	num = i + 1
	for j in range(3):
		print(num, end=" ")
	print()