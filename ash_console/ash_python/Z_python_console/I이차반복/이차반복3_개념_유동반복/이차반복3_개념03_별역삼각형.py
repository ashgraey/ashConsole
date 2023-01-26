'''
	[문제]
		아래와 같이 삼각형을 그려보시오.  	
   
	[예시]
		****
		***
		**
		*
'''

for i in range(4):
	for j in range(4-i):
		print("*", end="")
	print()