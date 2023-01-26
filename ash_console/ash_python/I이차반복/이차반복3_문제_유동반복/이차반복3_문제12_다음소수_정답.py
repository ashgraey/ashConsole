'''
	[문제]
		2~1000 사이의 랜덤 숫자 하나를 저장한다.
		위 숫자 바로 다음 소수를 출력하시오.
	
	[예시1]
		r = 1000
		소수 = 1009	 
	[예시2]
		r = 500
	    소수 = 503
'''

import random

r = random.randint(2, 1000)
print("r =", r)

num = r + 1

while True:
	count = 0

	for i in range(num):
		if num % (i + 1) == 0:
			count += 1
	
	if count == 2:
		print("소수 =", num)
		break

	num += 1