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

r = random.randint(3, 6)
print("r =", r)

i = 0
while True:
	x = r - i
	y = r - 1 - i
	z = r - 2 - i

	print(x, y, z)

	if z == 1:
		break

	i += 1 

print("---------")

num = r
while True:
	
	for i in range(3):
		print(num - i, end=" ")
	print()
	
	if num - 2 == 1:
		break

	num -= 1

	

