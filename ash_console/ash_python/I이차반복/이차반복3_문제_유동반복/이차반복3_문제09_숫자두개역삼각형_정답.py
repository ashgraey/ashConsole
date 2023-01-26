'''
	[문제]
		아래와 같이 삼각형을 출력하시오.
	[예시]
		1 2 3 4 5 6 7 8
  		1 2 3 4 5 6
		1 2 3 4
		1 2
'''

for i in range(4):
	len = (4 - i) * 2
	for j in range(len):
		print(j + 1, end=" ")
	print()