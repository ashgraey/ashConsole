'''
	[문제]
		랜덤으로 2~5 를 저장하고, 
		랜덤숫자의 개수만큼 숫자를 더하는 문제와 답을 만들어 출력하시오..
		단 더하기 할 숫자들은 1~9사이의 홀수인 랜덤숫자여야 한다. 
		
		아래 [출력] 뒤에 나오는 모양과 똑같은 모양으로 출력한다. 
		(단, 숫자는 랜덤이므로 숫자는 다르게 나올 수 있다.)
			
		[예시1]		  		
			랜덤 ==> 3
			[출력] 5 + 3 + 1 = 9
			
		[예시2]
			랜덤 ==> 5
			[출력] 1 + 5 + 3 + 7 + 1 = 17
'''
'''
랜덤 = 2 ~ 5의 수를 저장 
랜덤 숫자의 개수만클 숫자를 더한다.
더하기 숫자는 1 ~ 9사이의 홀수
'''

# import random

# [3차-1111]
# # 처음 랜덤의 값이 횟수
# # 무한반복을 쓰지 않아도된다
# # 연산자를 넣기위해 중첩 if 횟수 - 1 print(end = " + ")
# r = random.randint(2, 5)
# print("random =", r)

# 종료 = r
# total = 0
# count = 0 

# while True :
# 	r = random.randint(1, 9)

# 	if r % 2 == 1 :
# 		count += 1
# 		total += r
# 		print(r, end = " ")
	
# 	if count == 종료 :
# 		break 
# print(" =", total)

# [2차]
# 개수 = random.randint(2, 5)
# print("개수 =", 개수)
# 홀수 = 0

# i = 0 
# while i < 개수 :
# 	숫자 = random.randint(1, 9)
# 	print(숫자, end = " ")

# 	if 숫자 % 2 == 1 :
# 		홀수 += 숫자
# 		# print(홀수, end = " ")
	
# 	if i < 개수 - 1 :
# 		print(end = " + ")

# 	i += 1
# print()
# print("홀수 합 =", 홀수) 

# [1차]
# 횟수 = random.randint(2,5)
# print("랜덤 수의 갯수 =", 횟수)

# total = 0
# i = 0 
# while i < 횟수 : 
# 	# 횟수에 맞는 조건의 수
# 	num = random.randint(1, 9)
# 	# print(num, end = " ")

# 	# 홀수인 조건, num값 중 홀수인 수만 더한다. 
# 	if num % 2 == 1 : 
# 		total += num 
# 		print(num, end = " ")
		
# 		# 연산자 넣는 공식
# 		if i < 횟수 - 1 : 
# 			print(end = " + ")
# 	i += 1

# print(" =",total)
