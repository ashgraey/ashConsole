'''
	[문제]
		철수는 30개짜리 계단의 최상단에 서 있다. 
		제일 아래까지 내려가려고 한다. 
		철수가 내려갈 때 왼발로 밟은 계단을 출력하시오. 
		아래 조건들을 참고하시오.
		
		[조건]
		[1] 철수는 무조건 한 계단씩 내려간다. 
		[2] 철수는 첫발은 왼쪽 다리부터 계단을 내려간다. 
		[3] 출력을 다섯 번 할 때마다 반대편 다리로 바꿔서 출력하시오.
	[정답]
		왼발 = 30
		왼발 = 29
		왼발 = 28
		왼발 = 27
		...
		왼발 = 8
		왼발 = 7
		왼발 = 6
		오른발 = 5
		오른발 = 4
		오른발 = 3
		오른발 = 2
		오른발 = 1
'''
'''
왼발 5번 
오른발 5번 
30 왼
29 왼
28 왼 
27 왼
26 왼
25 왼
24 오
'''
# [3차-1110]
# num = 30
# i = 0 
# turn = True
# while i < 30 :
# 	# print(num)
# 	if turn == True :
# 		print("왼발 =", num)
	
# 	if turn == False : 
# 		print("오른발 =", num)


# 	num -= 1 
# 	i += 1 

# 	if num % 5 == 0 :
# 		turn = not turn

# [2차]
# num = 30
# i = 0 
# turn = True
# while i < 30 :
# 	# print(num)
# 	if turn == True :
# 		print("왼발 =", num)
	
# 	if turn == False : 
# 		print("오른발 =", num)


# 	num -= 1 
# 	i += 1 

# 	if num % 5 == 0 :
# 		turn = not turn

# [1차]
# i = 30

# turn = True 

# while i >= 0 :
	
# 	if turn == True : 
# 		print("왼발 =", i)
	
# 	if turn == False : 
# 		print("오른발 =", i)
# 	i -= 1 

# 	# not ?
# 	if i % 5 == 0 : 
# 		turn = not turn
