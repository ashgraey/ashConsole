'''
	[문제]
		[1] a리스트의 값들을 순차적으로 검사한다. 
		[2] 연속으로 같은 값이 두 개가 있다면, 
		[3] 두 수를 삭제하고 그 합을 다시 그 자리에 저장한다.
		[4] 연속으로 같은 값이 없을 때까지 (1~3)을 반복한다.

		b = [8,4,2,2,8,4,4] 세번째 자리 2, 2가 연속이다.
		b = [8,4,4,8,4,4] , 두번째 자리 4, 4가 연속이다.
		b = [8,8,8,4,4] , 첫번째자리 8, 8 이 연속이다.
		b = [16,8,4,4] , 세번째자리 4, 4 이 연속이다.
		b = [16,8,8] , 두번째자리 8, 8 이 연속이다.
		b = [16,16] , 첫번째자리 16, 16 이 연속이다.
		b = [32] , 연속된 수가 없다. 
	[정답]
		b = [32, 0, 0, 0, 0, 0, 0]
'''
a = [8,4,2,2,4,4,8]
b = [0,0,0,0,0,0,0]

index = 0
b[index] = a[index]
# print(b[index])

# i = 1
for i in range(1, len(a)):
	if b[index] == a[i]:
		b[index] = b[index] * 2

		# b리스트의 중복검사식이 있어야함
		while True:
			check = False
			for j in range(index):
				if b[j] == b[j + 1]:
					b[j] = b[j] * 2
					b[j + 1] = 0
					check = True
					index -= 1
			if check == False:
				break
	else:
		# 한칸 전진
		b[index + 1] = a[i]
		index += 1
	# i += 1
print(b)

# for i in range(1, len(a)) :
# 	if a[i] == b[index] :
# 		b[index] = b[index] * 2

# 		# b리스트에서의 중복 검사
# 		while True :
# 			ck = False
# 			for j in range(index) :
# 				if b[j] == b[j + 1] :
# 					b[j] = b[j] * 2
# 					b[j + 1] = 0 
# 					ck = True 
# 					index -= 1
# 			if ck == False :
# 				break 
				
# 	else :
# 		b[index + 1] = a[i]
# 		index += 1 
# print(b)
