'''
	[문제] 	
		1. 인덱스 2개를 랜덤(0~5)으로 저장하고 각 인덱스의 값을 교환한다.
		2. 위 1번을 10회 반복하며 과정을 출력하시오.
	[예시] 		
		예) 1 , 2 ==> [10,30,20,40,50,60];  // 20 과 30이 교환된다.		
		예) 4 , 1 ==> [10,50,20,40,30,60];  // 50 과 30이 교환된다.	
		예) 3 , 3 ==> [10,50,20,40,30,60]; 	// 같을 땐 아무일도안생긴다.
'''
import random

arr = [10, 20, 30, 40, 50]

size = len(arr) - 1
for i in range(10):
	idx1 = random.randint(0, size)
	idx2 = random.randint(0, size)

	temp = arr[idx1]
	arr[idx1] = arr[idx2]
	arr[idx2] = temp

	print(idx1, ",", idx2, " : ", arr)








