'''
	[문제]
		아래와 같이 2단부터 9단까지 구구단을 출력해보시오. 
		단, 이차 반복문을 사용한다. 
	
 	[예시]
		2 X 1 = 2
		2 X 2 = 4
		2 X 3 = 6
		2 X 4 = 8
		2 X 5 = 10
		2 X 6 = 12
		2 X 7 = 14
		2 X 8 = 16
		2 X 9 = 18
  
		3 X 1 = 3
		3 X 2 = 6
  		3 X 3 = 9
		3 X 4 = 12
		...
		...

		9 X 8 = 72
		9 X 9 = 81
'''
# for문은 i값이나 j값을 변경할 수 없다.
# i의 값이나 j의 값을 변경하려면 따로 변수를 지정해주어야한다.

# 1123
# num = 2
# for i in range(8) :
# 	for j in range(9) :
# 		total = num * (j + 1)
# 		print(num, "*", j + 1, "=", total)
# 	num += 1  
# 	print()

# 1117
# for i in range(8) :
# 	a = i + 2
# 	print("-----", a,"단-----")
# 	for j in range(9) :
# 		b = j + 1
# 		print(a, " x ", b, " =", a * b)
	