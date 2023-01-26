'''
	[문제]
		3~6 사이의 랜덤 숫자 하나를 저장하고 그 숫자만큼 아래와 같은 규칙으로 출력하시오.
		단, 일차 반복문과 이차 반복문으로 출력하시오.
 	[예시]
		r = 6
	[출력]
		3 2 1
		6 5 4
		9 8 7
		12 11 10
		15 14 13
		18 17 16
'''
import random 

start = 3
r = random.randint(start, 6)
print("r =", r)

# 1123
# for i in range(r) :
# 	for j in range(3) :
# 		print(start - j, end = " ")
# 	start += 3
# 	print()

# 1117
# for i in range(r) :
# 	# num의 조건이 중요하다.
# 	num = 3 * (i + 1)
# 	for j in range(3) :
# 		print(num, end = " ")
# 		num -= 1 
# 	print()





