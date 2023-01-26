'''
	[문제]	
		아래 리스트 a의 값을 사각형 모양으로 출력하시오.
	[예시]
		123
		456
		789
'''

a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
size = len(a)

# [1115]
# #case1
# for i in range(len(a)) :
# 	print(a[i], end = " ")

# 	if i % 3 == 2 :
# 		print()

# #case2
# print()
# for i in range(len(a)) :
# 	print(a[i], end = " ")
# 	count += 1 
# 	if count == 3 :
# 		print()
# 		count = 0

# [1차]
# index = len(a) 
# for i in range(size) :
# 	if i < 3 : 
# 		print(a[i], end = " ")
# 	elif i >= 3 and i <= 5 :
# 		print(a[i])
# 	elif i >= 6 and i <= 8 :
# 		print(a[i])
# print(a[0], a[1], a[2])
# print(a[3], a[4], a[5])
# print(a[6], a[7], a[8])


