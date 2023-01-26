'''
	[문제] 	
		1. 인덱스 2개를 랜덤(0~5)으로 저장하고 각 인덱스의 값을 교환한다.
		2. 위 1번을 10 번 반복하며 과정  출력 		
		예) 1 , 2 ==> [10,30,20,40,50,60];  // 20 과 30이 교환된다.		
		예) 4 , 1 ==> [10,50,20,40,30,60];  // 50 과 30이 교환된다.	
		예) 3 , 3 ==> [10,50,20,40,30,60]; 	// 같을 땐 아무일도안생긴다.
'''
'''
조건1 : 인덱스2개, 랜덤(0,5)저장
조건2 : 출력된 값 2개를 서로 교환
조건3 : 조건1, 조건2 10번 반복
'''

import random

# [1115]
arr = [10, 20, 30, 40, 50]
size = len(arr) - 1

for i in range(10) :
	idx1 = random.randint(0, size)
	idx2 = random.randint(0, size)
	print("idx1 =", idx1)
	print("idx2 =", idx2)

	temp = arr[idx1]
	arr[idx1] = arr[idx2]
	arr[idx2] = temp

print("arr =", arr)

# [2차]
# # size변수에 담는 이유는? 
# # 인덱스는 0부터 시작 위치값 마지막이 배열 길이 - 1이기때문
# for i in range(10) :
# 	r1 = random.randint(0, size)
# 	r2 = random.randint(0, size)
# 	# print(r1, r2)

# # for i in range(10) : 
# 	temp = arr[r1]
# 	arr[r1] = arr [r2]
# 	arr[r2] = temp

# 	print(r1, "," , r2, ":", arr)

# [1차]
# size = len(arr) - 1

# for i in range(10):
# 	index1 = random.randint(0, size)
# 	index2 = random.randint(0, size)

# 	temp = arr[index1]
# 	arr[index1] = arr[index2]
# 	arr[index2] = temp

# 	print(index1, ",", index2, ":", arr)




