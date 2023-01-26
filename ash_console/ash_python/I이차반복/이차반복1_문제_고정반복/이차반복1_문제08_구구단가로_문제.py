'''
	[문제]
		아래와 같이 구구단을 가로로 출력해보시오.
		2 * 1 = 2	3 * 1 = 3    ...  	9 * 1 = 9
		2 * 2 = 4  	3 * 2 = 6	 ...	9 * 2 = 18
		2 * 3 = 6  	3 * 3 = 9	 ...	9 * 3 = 27
		...      	...				    ...
		...      	...				    ...
		2 * 9 = 18	3 * 9 = 27 	 ...	9 * 9 = 81
'''
# 1123
# for i in range(9) :
# 	a = i + 1
# 	for j in range(8) :
# 		b = j + 2
# 		total = a * b
# 		print(b, "*", a ,"=", total, end = "\t")
# 	print()

# 1117
# for i in range(9) :
# 	a = i + 1
# 	for j in range(8) :
# 		b = j + 2 
# 		# end = "\t"??
# 		# \t 문자열사이에 tap간격을 줄때 사용
# 		print(b, " x ", a, " =", b * a, end = "\t")
# 	print()
	