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
temp = []

# 1215
# temp에 복사
# 복사 이유 : a의 값이 바뀌기 때문에
for i in range(len(a)) :
	temp.append(a[i])
print(temp)

# 중복값이 나타나면 값을 0으로 만든다.
# 0이 아닌 값만 value에 저장한다.
for i in range(len(a)) :
	for j in range(len(a)) :
		if i != j and temp[i] == temp[j] :
			temp[j] = 0
	
	if temp[i] != 0 :
		value.append(temp[i])
# print(a)
print(temp)
print("value =", value)

# value리스트와 a리스트에 중복된 값을 cnt한다.
# cnt를 count리스트에 저장한다.
for i in range(len(value)) :
	cnt = 0 
	for j in range(len(a)) :
		if value[i] == a[j] :
			cnt += 1
	count.append(cnt)
print("count = ", count) 

# 1124
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