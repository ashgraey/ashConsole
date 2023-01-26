'''
[문제] 
	랜덤으로 1~10을 10번 출력하고, 가장 큰 수를 출력하시오. 
	단, 가장 큰 수가 여러 번 나오는 경우 
	중복 출력된 횟수도 함께 출력하시오.
[예시]
	3 5 2 7 10 7 8 7 6 10 
	가장 큰 수 = 10
	반복 횟수 = 2
'''

import random

# 3 5 2 7 10 7 8 7 6 10 
max = 0
count = 0

i = 0
while i < 10:
	r = random.randint(1, 10)
	if max < r:
		max = r
		count = 0
	if max == r:
		count += 1

	print(r, end=" ")

	i += 1

print()
print("가장 큰 수 =", max)
print(count)