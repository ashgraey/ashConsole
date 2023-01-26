'''
	[문제]
		a리스트의 값 중 b리스트의 값과 같은 값이 있으면
		total에 저장한다. 
	[정답]
		total = [20, 30]
'''

a = [10, 20, 30, 60]
b = [40, 30, 20, 50]
total = []

for i in range(len(a)):
	for j in range(len(b)):
		if a[i] == b[j]:
			total.append(a[i])
print(total)