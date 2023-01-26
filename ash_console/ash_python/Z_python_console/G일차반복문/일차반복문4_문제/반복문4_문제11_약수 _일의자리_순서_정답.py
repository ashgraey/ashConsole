'''
	[문제]
	  	120의 약수 중에서 순서대로 약수를 출력했을 때, 
        일의자리가 4인 두 번째 약수를 출력하시오.
	[정답]
		24
'''

num = 120

count = 0

i = 1
while i <= num:
	if num % i == 0 and i % 10 == 4:
		count += 1

		if count == 2:
			print(i)
	i += 1