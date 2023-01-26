'''
	[문제]
		아래와 같이 삼각형을 그려보시오.  	
   
	[예시]
		*
		**
		***
		****	
'''
# 정답
for i in range(4):
	for j in range(i + 1):
		print("*", end="")
	print()

# 1123
# for i in range(4) :
# 	for j in range(i + 1) :
# 		print("*", end = "")
# 	print()

# 1121
# for i in range(4) :  
# 	for j in range(i + 1) :
# 		print("*", end = " ")
# 	print()