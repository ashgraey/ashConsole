'''
	[문제]
	  	1980의 약수 중에서 순서대로 약수를 출력했을 때, 
        십의자리가 3인 두 번째 약수를 출력하시오.
	[정답]
		33
'''

num = 1980

count = 0

i = 1
while i <= num:
	if num % i == 0 and i % 1000 % 100 // 10 == 3:
		count += 1

		if count == 2:
			print(i)
	i += 1