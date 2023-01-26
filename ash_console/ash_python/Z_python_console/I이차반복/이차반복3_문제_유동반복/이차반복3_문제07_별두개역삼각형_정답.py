'''
	[문제]
		아래와 같이 삼각형을 출력하시오.
  
	[예시]
		********
		******
		****
		**
'''

for i in range(4):
	len = (4 - i) * 2
	for j in range(len):
		print("*", end="")
	print()