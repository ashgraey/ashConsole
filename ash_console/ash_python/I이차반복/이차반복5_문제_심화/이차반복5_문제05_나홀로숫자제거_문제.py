'''
	[문제]
		a리스트에서 혼자 있는 값만 제외하고 b에 추가하시오.
	[예시]
		[1,2,3,2,1] : b = [1,2,2,1]    # 3 삭제
		[1,3,4,4,2] : b = [4,4]        # 1,2,3 삭제
		[1,1,1,1,1] : b = [1,1,1,1,1]  # 없음
'''

a = [1,2,3,2,1]
# a = [1,3,4,4,2]
# a = [1,1,1,1,1]
b = []

# 1216
for i in range(len(a)) :
	ck = False
	for j in range(len(a)) :
		if i != j and a[i] == a[j] :
			ck = True
			break
			
	if ck == True :
		b.append(a[i])

print(b)


# 2차
# for i in range(len(a)) :

# 	check = False

# 	j = 0 
# 	while j < len(a) :
# 		if i != j and a[i] == a[j] :
# 			check = True 
# 			break
# 		j += 1 

# 	if check == True :
# 		b.append(a[i])
# print(b) 

# # 1124
# 1차
# for i in range(len(a)) :

# 	for j in range(len(a)) :
# 		if i != j and a[i] == a[j] :
# 			b.append(a[i])

# print(b)