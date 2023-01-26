'''
	[문제]
		a리스트의 값을 b에 저장한다.
		단, 연속으로 중복되는 값은 한 개만 저장하고 나머지는 저장하지 않는다.
	[예시]
		b = [1,3,2,3,4,5,6]
'''
# tip : b리스트를 활용하여라
a = [1,1,1,3,3,3,3,2,2,3,3,3,4,5,6,6,6]
b = []

# 1216
b.append(a[0])

idx = 0 
for i in range(1, len(a)) :
	ck = False
	if b[idx] == a[i] :
		ck = True
	
	if ck == False :
		b.append(a[i])
		idx += 1 

print(b)

# 1125
# for i in range(len(a)) :
# 	check = False
# 	j = i 
# 	while j < len(a) :
# 		if i != j and a[i] == a[j] :
# 			check = True 
# 		j += 1 

# 	if check == False :
# 		b.append(a[i])

# print(b)

# 1122
# for i in range(len(a)) :
# 	count = 0 
# 	j = i 
# 	while j < len(a) :
# 		if a[i] == a[j] :
# 			temp = a[j]
# 			count += 1
# 		j += 1
	
# 	if count == 1 :
# 		b.append(temp)

# print(b)