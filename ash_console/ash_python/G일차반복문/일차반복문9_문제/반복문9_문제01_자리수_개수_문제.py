'''
[문제]
	10000~99999 사이의 랜덤숫자를 저장하고 
	자리별숫자가 5 이상인 개수를 출력하시오.
	
		예) 19200 ==> 9 하나만 5 이상 ==> 1
		예) 98436 ==> 9,8,6, 세 개가상 5 이 ==> 3
'''
"""

"""
# [3차 - 1111]
# # 조건문으로만 식을 해결함
# # 10000~99999 사이의 랜덤숫자를 저장하고 
# import random

# r = random.randint(10000, 99999)
# print("랜덤값 =", r)

# count = 0
# # i = 1
# # while i <= r :
# 만 = r // 10000
# 천 = r % 10000 // 1000
# 백 = r % 1000 // 100 
# 십 = r % 100 // 10 
# 일 = r % 10
# # print(일)
# # break

# if 만 >= 5 :
# 	count += 1 
# if 천 >= 5 :
# 	count += 1 
# if 백 >= 5 :
# 	count += 1 
# if 십 >= 5 :
# 	count += 1 
# if 일 >= 5 :
# 	count += 1 
# # break
# 	# i += 1 

# print("count =", count)

# [2차]
# import random

# r = random.randint(10000, 99999)
# print("랜덤 수 =", r)

# count = 0 
# while r != 0 :

# 	unit = r % 10
# 	print(unit, end = " ")
	
# 	if unit >= 5 :
# 		count += 1 
	
# 	r //= 10 
# print()
# print("5이상의 개수 =", count)

# [1차]
# import random

# num = random.randint(10000, 99999)
# print(num)
# count = 0
# temp = num 

# run = 1 
# while run == 1 :
# 	temp = temp // 10
# 	print(temp)
# 	count += 1 

# 	if count == 0 : 
# 		run = 0
# 	print(count) 


