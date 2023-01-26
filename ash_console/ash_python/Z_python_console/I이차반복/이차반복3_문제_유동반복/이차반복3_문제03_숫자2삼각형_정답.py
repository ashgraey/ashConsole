'''
	[문제]
		아래와 같이 삼각형을 출력하시오.
	[예시]
		1
		1 2
		1 2 3
		1 2 3 1
		1 2 3 1 2
		1 2 3 1 2 3
		1 2 3 1 2 3 1
		1 2 3 1 2 3 1 2
		1 2 3 1 2 3 1 2 3
		1 2 3 1 2 3 1 2 3 1
'''

for i in range(10):
	num = 1
	for j in range(i + 1):
		print(num, end=" ")
		num += 1

		if num % 4 == 0:
			num = 1
	print()