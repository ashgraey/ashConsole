'''
	[문제]
		아래 a리스트의 값을 자리별로 분리 후,
		그 합을 total 리스트에 추가하시오.
	[예시]
		[1] 1 + 3 + 2  				total = [6]
		[2] 4 + 3 + 5 + 4  			total = [6,16]
		[3] 2 + 3 + 3 				total = [6,16,8]
		[4] 6 + 6 + 7 + 6 + 5  		total = [6,16,8,30]
	[정답]
		total = [6, 16, 8, 30]
'''
# tip : 반복문 안의 무한반복
a = [132, 4354, 233, 66765]
total = []

# 1216
for i in range(len(a)) :
	# cnt = 0 
	tot = 0
	while True :
		unit = a[i] % 10
		tot += unit
		
		a[i] //= 10
		# cnt += 1
		if a[i] == 0 :
			break
	total.append(tot)

print(total)
# 종료조건 확인
# cnt = 0 
# while True :
# 	a[0] //= 10
# 	cnt += 1 
# 	if a[0] == 0 :
# 		print(a[0], cnt)
# 		break

# 1125
# for i in range(len(a)) :
# 	t = 0
# 	num = 0  
# 	for j in range(5) :
# 		num = a[i] % 10 
# 		a[i] //= 10 
# 		t += num
# 		# print(t) 
# 	total.append(t)
# print(total)

# 1123
# count = 5
# for i in range(len(a)) :
# 	t = 0
# 	for j in range(count) :
# 		t += a[i] % 10 
# 		a[i] //= 10 
# 	total.append(t)

# print(total)