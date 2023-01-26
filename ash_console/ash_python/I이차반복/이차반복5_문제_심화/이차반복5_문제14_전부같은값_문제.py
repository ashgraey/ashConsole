'''
	[문제]
		a리스트와 b리스트의 값들이 각각 값과 개수가 똑같은지 확인한다.
		똑같으면 "같음", 아니면 "다름"을 출력하시오.
		위치는 상관없이 각각의 숫자의 개수가 일치하면 "같음"이다. 
	[정답]
'''
a = [10, 20, 30, 10, 20, 30]
b = [30, 20, 10, 20, 30, 10]

# 1125
# 중복되는값을 하나만 temp리스트에 저장
# 다른 리스트 변수를 만들어 중복되는 기준의 값을 먼저 저장한다는 생각이 필요
# temp = []
# i = 0
# while i < len(a) :
# 	check = False

# 	j = 0 
# 	while j < i :
# 		if a[i] == temp[j] :
# 			check = True
# 			break
# 		j += 1 
	
# 	if check == False :
# 		temp.append(a[i])
# 	i += 1 
# # print(temp)

# for i in range(len(temp)) :
# 	ca = 0
# 	cb = 0 
# 	for j in range(len(a)) :
# 		if temp[i] == a[j] :
# 			ca += 1 
# 		if temp[i] == b[j] :
# 			cb += 1 
	
# 	print(temp[i], ca, cb)
# 	if ca == cb :
# 		print("같음")
# 	else :
# 		print("다름")

# 1121
# for i in range(len(a) // 2) :
# 	ca = 0 
# 	cb = 0 
# 	# a[0]은 10
# 	for j in range(len(a)) :
# 		if a[i] == a[j] :
# 			ca += 1 

# 	# b[0]은 30이므로 10과 같은 인덱스를 찾아서
# 	# temp변수에 저장
# 	# 반복문을 한번 더 써서 tmep의 값을 a[j]인덱스와 비교 
# 	# 값이 동일하면 count += 1 
# 	j = 0 
# 	while j < len(a) :
# 		if b[j] == a[i] :
# 			temp = b[j]
			
# 			j = 0 
# 			while j < len(a) :
# 				if temp == b[j] :
# 					cb += 1 
# 				j += 1 
# 		j += 1 
			
# 	print(a[i], temp)
# 	print("ca =", ca)
# 	print("cb =", cb)
	
# 	if ca == cb : 
# 		print("같음")
# 	else : 
# 		print("다름")