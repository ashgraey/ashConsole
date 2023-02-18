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

# 1123
# 소수에 대한 개념 부족

# 1121
# r보다 큰 수여야 하기 때문에
num = r + 1 

while True :
	count = 0 

	# 소수 : 약수가 1과 자기 자신뿐인 자연수
	for i in range(num) :
		# 약수 : 1, 자기자신 => count = 2
		if num % (i + 1) == 0 :
			count += 1

	# count == 2가 아니면 소수가 아니다.
	if count == 2 :
		print("소수 =", num)
		break
	num += 1 