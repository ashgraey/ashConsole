'''
	[문제]
		아래 a리스트의 값을 자리별로 분리 후,
		그 합을 total 리스트에 추가하시오.
	[예시]
		[1] 1 + 3 + 2  				total = [6]
		[2] 4 + 3 + 5 + 4  			total = [6,16]
		[3] 2 + 3 + 3 				total = [6,16,8]
		[4] 6 + 6 + 7 + 6 + 5  		total = [6,16,8,30]
	[정답]
		total = [6, 16, 8, 30]
'''

a = [132, 4354, 233, 66765]
total = []

for i in range(len(a)):

	temp = a[i]

	tot = 0
	while True:
		unit = temp % 10
		print(unit, end=" ")
		tot += unit

		temp //= 10
		if temp == 0:
			break
	total.append(tot)
	print()

print(total)