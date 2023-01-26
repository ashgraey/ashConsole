'''
[문제]
	5~15 사이의 숫자 중에서 
	[조건1] 4의 배수를 출력하고, 
	[조건2] 그 총합을 구하시오. 
	[조건3] 그 개수를 출력하시오.
[정답]
	8 12 
	합 = 20
	개수 = 2
'''
total = 0
count = 0

i = 5
while i <= 15:
	if i % 4 == 0:
		print(i, end=" ")
		total += i
		count += 1
	i += 1
print()
print("total =", total)
print("count =", count)


