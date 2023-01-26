'''
	[문제]
		a와 b 두 리스트를 비교해서 서로 겹치지 않는 값을 
		temp에 저장하고 출력하시오.
	[정답]
		temp = [6, 4, 20, 3, 17, 13, 7]
'''
a = [16,  5, 11, 6, 19, 12, 18,  4, 20, 3]
b = [17, 11, 19, 5, 13, 18, 16, 12, 11, 7]
temp = []

# 1124
# for i in range(len(a)) :
# 	count = 0 
# 	check = 0 
# 	for j in range(len(b)) :
# 		if a[i] == b[j] : 
# 			count += 1 
# 		if a[j] == b[i] :
# 			check += 1 

# 	if count == 0 :
# 		temp.append(a[i])
# 	if check == 0 :
# 		temp.append(b[i])	
# print(temp)

# 1122
# # count 변수대신 check , True, False를 이용하면 훨씬 더 직관적으로 풀 수 있다.
# # 반복문 두개 사용

# # a리스트의 중복값이 없는 인덱스의 값을 찾는 반복
# for i in range(len(a)) :
# 	count = 0  
# 	for j in range(len(b)) :
# 		if a[i] == b[j] :
# 			count += 1 
# 	if count == 0 : 
# 		temp.append(a[i])

# # b리스트의 중복값이 없는 인덱스의 값을 찾는 반복
# for i in range(len(a)) :
# 	count = 0  
# 	for j in range(len(b)) :
# 		if b[i] == a[j] :
# 			count += 1 
# 	if count == 0 :
# 		temp.append(b[i])

# print(temp)