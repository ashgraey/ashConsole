'''
	[문제]
		아래와 같이 삼각형을 출력하시오.
	[예시]
		1 2 3 4 5 6 7
		2 3 4 5 6 7
		3 4 5 6 7
		4 5 6 7
		5 6 7
		6 7
		7
'''

for i in range(7):
	num = i + 1
	for j in range(7 - i):
		print(num, end=" ")
		num += 1
	print()