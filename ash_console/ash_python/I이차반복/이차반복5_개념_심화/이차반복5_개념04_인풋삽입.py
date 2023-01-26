'''
	[문제]
		a리스트에 value값 3개를 추가하려고 한다.
		단, a리스트 마지막에 추가하는것이 아니고,
		index리스트의 위치에 추가하고, 위치 뒤의 모든 값은
		한칸씩 뒤로 이동한다. 
	[예시]
		index : 2 , value = 60 , a = [10,20,60,30,40,50]
		index : 1 , value = 70 , a = [10,70,20,60,30,40,50]
		index : 0 , value = 80 , a = [80,10,70,20,60,30,40,50]
	[정답]
		a = [80, 10, 70, 20, 60, 30, 40, 50]
'''
a = [10,20,30,40,50]
index = [2,1,0]
value = [60,70,80]

# # 정답
# for i in range(3):
# 	a.append(value)
# 	# print(a)

# 	j = len(a) - 1
# 	while j > index[i]:
# 		a[j] = a[j - 1]
# 		j -= 1
# 	a[index[i]] = value[i]
# print(a)

# 1124
for i in range(3) :
	a.append(value[i])

	# 뒤로 밀기는 마지막 인덱스부터 하나씩 감소시키는게 편하다.
	j = len(a) - 1  
	while j > index[i] :
		a[j] = a[j - 1]
		j -= 1  

	a[index[i]] = value[i]
print(a)

# 1122
# for i in range(3) :
# 	# 인덱스 길이를 늘리기 위함
# 	a.append(value[i])
# 	# print(a)
	
# 	j = len(a) - 1 
# 	while j > index[i] :
# 		a[j] = a[j - 1]
# 		j -= 1 
# 	a[index[i]] = value[i]
	
# print(a)
