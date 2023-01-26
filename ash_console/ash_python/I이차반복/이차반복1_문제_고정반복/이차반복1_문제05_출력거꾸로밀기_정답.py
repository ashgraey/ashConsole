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

r = random.randint(3, 6)
print("r =", r)

i = 0
while True:
	x = 1 + i
	y = 2 + i
	z = 3 + i

	print(z, y, x)

	if z == r:
		break

	i += 1

print("----------")

j = 3
while j <= r:
	for i in range(3):
		print(j-i, end=" ")
	print()
	j += 1

