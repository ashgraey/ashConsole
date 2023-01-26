'''
	[문제]
		2~100 사이의 랜덤 숫자 하나를 저장하고, 
		2부터 그 숫자 사이의 모든 소수를 출력하시오.

	[예시]
		r = 20
	 	소수 = 2, 3, 5, 7, 11, 13, 17, 19	
'''
# 오류 : 소수식이 아님
import random

r = random.randint(2, 100)
print("r =", r)

i = 2
while i <= r:
	if r % i == 0:
		print(i, end=" ")
	i += 1

# 1121
# r = random.randint(2, 100)
# print("r =", r)

# i = 2 
# while i <= r :
# 	if r % i == 0 :
# 		print(i, end = " ")
	
# 	i += 1 