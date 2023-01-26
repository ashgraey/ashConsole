'''
	[문제]
		아래 리스트 두 개를 합치고 오름차순으로 정렬하시오. 
	[정답]
		[1, 2, 3, 5, 7, 8, 9, 10, 12, 15, 19, 20]
'''
a =[9,10,3,2,20,19]
b = [15,12,1,5,7,8]
c = []

# 1216
# c리스트로 합치기
for i in range(len(a)) :
	c.append(a[i])
	c.append(b[i])
print("정렬 전 = ", c)

# 정렬
for i in range(len(c)) :

	min = 100
	minIdx = 0 
	j = i
	while j < len(c) :
		if min > c[j] :
			min = c[j]
			minIdx = j
		j += 1
	
	temp = c[minIdx]
	c[minIdx] = c[i]
	c[i] = temp

print("정렬 후 = ", c)
		
# 1124 
# 리스트 두개 합치기
# for i in range(len(a)) :
# 	c.append(a[i])
# 	c.append(b[i])
# print(c)

# # 오름차순 정렬
# # 원리 : 가장 작은 값을 찾는다 -> i의 인덱스와 값 교환 -> j = i 교환된 인덱스 제외한 자리부터 다시 가장 작은 값을 구한다. => 리스트의 길이만큼 반복

# for i in range(len(c)) :
# 	min = 100 
# 	minIdx = 0 
	
# 	j = i
# 	while j < len(c) :
# 		if min > c[j] :
# 			min = c[j]
# 			minIdx = j
# 		j += 1 
	
# 	temp = c[i]
# 	c[i] = c[minIdx]
# 	c[minIdx] = temp

# print(c)

