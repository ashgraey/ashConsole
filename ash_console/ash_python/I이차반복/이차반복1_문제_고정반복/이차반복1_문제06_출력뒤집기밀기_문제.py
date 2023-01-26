'''
	[문제]
		3~6 사이의 랜덤 숫자 하나를 저장하고 그 숫자만큼 아래와 같은 규칙으로 출력하시오.
		단, 일차 반복문과 이차 반복문으로 출력하시오.
 	[예시]
		r = 6
	[출력]
		6 5 4
		5 4 3
		4 3 2
		3 2 1
'''
import random
start = 3
end = 6
r = random.randint(start, end)
print("r =", r)

# # 1123
# # 1차
# i = 0 
# while start <= r :
# 	x = r - i
# 	y = x - 1
# 	z = y - 1
#
# 	print(x, y, z)
#	
# 	start += 1 
# 	i += 1 
#
# # 2차
# for i in range((r - start) + 1) :
# 	for j in range(3) :
# 		print(r - j, end = " ")
# 	r -= 1
# 	print()

# 1117
# [일차반복문]
# i = 0 
# while True :
#	
# 	x = r - i
# 	y = (r - 1) - i 
# 	z = (r - 2) - i
#
# 	print(x , y, z, end = " ")
# 	print()
#
# 	if z == 1 :
# 		break
#	
# 	i += 1 
# [이차반복문]
# j = 3
# temp = r
# for j in range(r) :
#
# 	for i in range(3) :
# 		print(temp - i, end = " ") 
#	
# 	print()
# 	temp -= 1
# 	j += 1 
#
# num = r
# while True :
#
# 	for i in range(3) :
# 		print(num - i, end = " ")
# 	print()
#
# 	# 종료조건이 print보다 뒤에 있기때문에 
# 	# 3 2 1을 출력하고 num - 2 == 1이므로 break 반복문을 나간다.
# 	# num == 3이면 이란 조건으로도 종료조건을 쓸 수 있다.
# 	# if num == 3 :
# 	if num - 2 == 1 :
# 		break
#
# 	num -= 1
