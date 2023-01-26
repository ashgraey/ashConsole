'''
	[문제]
		[1] a리스트에 1~10까지의 랜덤 숫자 3개를 저장 후 출력하시오.
		[2] 단, 숫자 3개는 서로 중복되면 안 된다. 
		[3] 숫자 3개의 합은 반드시 20이어야 한다. 
	[예시]
		[3, 10, 7] o 
		[5, 10, 5] x 
'''
import random

a = [0,0,0]

# 1124
# 중복검사
# while True :
# 	i = 0
# 	while i < 3 :
# 		r = random.randint(1, 10)
# 		check = False

# 		j = 0
# 		while j < i :
# 			if a[j] == r :
# 				check = True
# 				break 
# 			j += 1 
		
# 		if check == False : 
# 			a[i] = r
# 			i += 1 

# 	# total
# 	total = 0
# 	for i in range(len(a)) :
# 		total += a[i]

# 	# 종료조건
# 	print(a, total)
# 	if total == 20 :
# 		# print(a, total)
# 		break 



# 1122
# run = True
# while run : 
	
# 	# 중복x, 랜덤값 3개를 리스트에 저장하는 식
# 	i = 0 
# 	while i < 3 :
# 		r = random.randint(1, 10)
# 		check = False
		
# 		j = 0 
# 		while j < i :
# 			if a[i] == r :
# 				check = True
# 				break
# 			j += 1 

# 		if check == False :
# 			a[i] = r
# 		i += 1 	
# 	print(a)
		
# 	# total값 구하는 식
# 	i = 0 
# 	total = 0 
# 	for i in range(3) :
# 		total += a[i]
# 	print("total =", total)

# 	# 종료식
# 	if total == 20 : 
# 		run = False 	