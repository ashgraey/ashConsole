'''
	[문제]
		3~6 사이의 랜덤 숫자 하나를 저장하고 그 숫자만큼 아래와 같은 규칙으로 출력하시오.
		단, 일차 반복문과 이차 반복문으로 출력하시오.
 	[예시]
		r = 6
	[출력]
		3 2 1
		4 3 2
		5 4 3
		6 5 4
'''
import random 
start = 3
r = random.randint(start, 6)
# r = 6
print("r =", r)

# 1123
# # 1차
# x = start
# y = start - 1
# z = start - 2 
# for i in range(r - 2) :
# 	print(x + i, y + i, z + i)
# # 2차
# for i in range(r - 2) :
# 	for j in range(3) :
# 		print(start - j, end = " ")
# 	start += 1 
# 	print()

# 1117
# [일차반복]
# x = (r // 2)
# y = x - 1 
# z = y - 1

# for i in range(x + 1) :
# 	print(x + i, y + i, z + i)
# [이차반복]
# num = 3 
# for i in range(4) :
# 	v = num + i
# 	for j in range(3) :
# 		print(v - j, end = " ")
# 	print()