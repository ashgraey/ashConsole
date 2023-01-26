'''
	[문제]
		아래와 같이 삼각형을 출력하시오.	
	[예시]
		7
		6 7
		5 6 7
		4 5 6 7
		3 4 5 6 7
		2 3 4 5 6 7
		1 2 3 4 5 6 7
'''

for i in range(7):
	num = 7 - i
	for j in range(i + 1):
		print(num, end=" ")
		num += 1
	print()