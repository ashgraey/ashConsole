'''
	[문제]
	    18의 약수를 출력하시오.
	[정답]
		1
		2
		3
		6
		9
		18
'''

num = 18

i = 1
while i <= num:
	if num % i == 0:
		print(i)
	i += 1