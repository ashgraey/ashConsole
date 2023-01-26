'''
	[문제]
		3~6 사이의 랜덤 숫자 하나를 저장하고 그 숫자만큼 아래와 같은 규칙으로 출력하시오.
		단, 일차 반복문으로 출력하시오.
 	[예시]
		r = 6
	[출력]
		18 12 6
		17 11 5
		16 10 4
		15 9 3
		14 8 2
		13 7 1
'''
import random

r = random.randint(3, 6)
print("r =", r)

# 1123
# 1차
# num = r * 3
# num2 = num - r
# num3 = num2 - r
# for i in range(r) :
# 	print(num - i, num2 - i, num3 - i)
#
# 2차
# for i in range(r) :
# 	num = r * 3
# 	num -= i
# 	for j in range(3) :
# 		print(num, end = " ")
# 		num -= r
# 	print()

# 1117
# x = r * 3
# y = r * 2
# z = r * 1
# for i in range(r):
# 	print(x-i, y-i, z-i)



