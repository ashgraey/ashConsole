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

result = 0

i = 2
while i <= r:

	count = 0

	j = 1
	while j <= i:
		if i % j == 0:
			count += 1
		j += 1
	
	if count == 2:
		print(i, end=" ")
		result += 1

	i += 1

print()
print("개수 =", result)