'''
	[문제]
		랜덤으로 10000 ~ 99999 사이의 랜덤숫자를 저장하고 
		다음 규칙에 따라 결과를 출력하시오.
		랜덤숫자를 두 개로 분리하는데
		한 자리씩 늘리면서 분리한다. 
		각 분리한 숫자의 합을 출력한다.
	[예시]
		r = 34567
	[결과]
		3 + 4567
		34 + 567
		345 + 67
		3456 + 7
'''
import random

rNum = random.randint(10000, 99999)
print("rNum =", rNum)

temp = rNum

div = 1
count = 0
while True:
	if temp == 0:
		break

	unit = temp % 10
	print(unit, end=" ")
	temp //= 10
	count += 1
	div *= 10

print()
print("count =", count)
div //= 10
print(div)

temp = rNum
for i in range(count - 1):
	front = temp // div
	back = temp % div
	print(front, "+", back)

	div //= 10