'''
	[문제]
		a리스트의 값중 0을 제외하고 모든값을 오른쪽으로 모으시오.
 	[결과]
 		a = [0,0,0,0,0,0,2,3,4,5];
'''


a = [0,0,2,0,3,0,4,0,0,5]


j = len(a) - 1
idx = len(a) - 1
for i in range(len(a)):
	if a[j] != 0:
		temp = a[idx]
		a[idx] = a[j]
		a[j] = temp

		idx -= 1
	j -= 1
print(a)
