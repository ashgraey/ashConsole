'''
	[문제]
		랜덤(2~10)의 숫자를 저장하고 
		랜덤 개수만큼 반복하면서 반복적으로 숫자를 저장한다.
		반복 숫자란? 1 2 3 1 2 3 1 2 3 을 반복해서 저장하는 것이다.
	[예1] 
		r = 8
		arr = [1,2,3,1,2,3,1,2]
  
	[예2] 
		r = 4
		arr = [1,2,3,1]
'''
# [문제]
# 랜덤(2~10)의 숫자를 저장하고 
# 랜덤 개수만큼 반복하면서 반복적으로 숫자를 저장한다.
# 반복 숫자란? 1 2 3 1 2 3 1 2 3 을 반복해서 저장하는 것이다.
'''
idx 0 1 2 3 4 5 

'''
import random

arr = []

# [1115]
# r = random.randint(2, 10)
# print("r =", r)

# value = 1 

# for i in range(r) :
# 	arr.append(value)
# 	value += 1 

# 	if i % 3 == 2 :
# 		value = 1
	
# print(arr)

# [1차]
# r = 4
# # r = random.randint(2, 10)
# print("r =", r)

# idx = 1
# for i in range(r) : 
# 	arr.append(idx)
# 	idx += 1 
	
# 	if idx % 4 == 0 :
# 		idx = 1
# print(arr)

