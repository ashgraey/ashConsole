'''
	[문제]
		2~100 사이의 랜덤 숫자 하나를 저장하고, 
		2부터 그 숫자 사이의 모든 소수의 개수를 출력하시오.

	[예시]
		r = 20
	 	소수 = 2, 3, 5, 7, 11, 13, 17, 19
		개수 = 8
'''
import random

r = random.randint(2, 100)
print("r =", r)

# # 1123
# # 개념이해부족
# result = 0 

# i = 2
# # 2부터 r값까지 i를 1씩 증가시키며 반복 
# while i <= r :
	
# 	count = 0 

# 	j = 1 
# 	# i == y, j == x
# 	# i 즉, 랜덤값보다 작은 값의 소수를 찾기위해 약수의 개수를 세어보는 조건
# 	while j <= i :
# 		if i % j == 0 :
# 			count += 1
# 		j += 1  

# 	# count == 2이면 약수가 2개, 즉 소수
# 	# i값을 출력하고 출력할때마다 result값(소수의 개수)도 증가시킨다.
# 	if count == 2 :
# 		print(i, end = " ")
# 		result += 1
	
# 	i += 1 

# 1121
# result = 0

# i = 2
# while i <= r:

# 	count = 0

# 	j = 1
# 	while j <= i:
# 		if i % j == 0:
# 			count += 1
# 		j += 1
	
# 	if count == 2:
# 		print(i, end=" ")
# 		result += 1

# 	i += 1

# print()
# print("개수 =", result)