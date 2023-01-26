'''
	[문제]
		a리스트의 값을 중복없이 value에 저장한다.
		그리고 중복되는 개수를 count에 저장한다.
	[정답]
		value = [10,20,30,100]
		count = [2,3,5,1]
'''

a = [10, 20, 30, 30, 100, 10, 30, 30, 20, 30, 20]

value = []
count = []

# 1124
# value에 값을 저장 
# 저장한 값과 a리스트를 비교
# 중복되지 않으면 저장, 중복되면 저장하지 않는다.
# for i in range(len(a)) :
# 	check = False

# 	j = 0 
# 	# 핵심 : len(value)
# 	while j < len(value) :
# 		if a[i] == value[j] :
# 			check = True 
# 			break
# 		j += 1 
	
# 	if check == False :
# 		value.append(a[i])
	
# print(value)
# # count 구하기
# for i in range(len(value)) :
# 	cnt = 0 
# 	for j in range(len(a)) :
# 		if value[i] == a[j] :
# 			cnt += 1 
# 	count.append(cnt)
# print(count)	
	
# 중복 검사
# 1122
# # 아예 못품
# for i in range(len(a)) :
# 	c = 0 
# 	check = False
# 	for j in range(len(a)) :
# 		if a[i] == a[j] :
# 			check = True
# 			c += 1 

# 	if check == True : 
# 		value.append(a[i])
# 		count.append(c)
# 		a[j] = 0

# print(value)
# print(count)