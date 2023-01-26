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
# 1123
# for i in range(10) :
# 	num = 1
# 	for j in range(i + 1) :
# 		if j % 3 == 0 :
# 			num = 1
# 		print(num, end = " ")
# 		num += 1 
# 	print()

# 1121
# for i in range(10) :
# 	# 초기화식의 위치도 중요함
# 	num = 0 
# 	for j in range(i + 1) :
# 		print(num + 1, end = " ")
# 		num += 1 
# 		if num % 3 == 0 :
# 			num = 0 
# 	print()