'''
	[문제]
		[조건1] 18의 약수 중 짝수들만 출력하고, 
     	[조건2] 총합을 출력하시오.
		[조건3] 개수를 구하시오.
	[정답]
		2 6 18 
		total = 26
		count = 3
'''

num = 18

total = 0
count = 0

i = 1
while i <= num:
	if num % i == 0 and i % 2 == 0:
		print(i, end=" ")
		total += i
		count += 1
	i += 1

print()
print("total =", total)
print("count =", count)