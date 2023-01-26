'''
	[문제]
		아래 리스트 두 개를 합치고 오름차순으로 정렬하시오. 
	[정답]
		[1, 2, 3, 5, 7, 8, 9, 10, 12, 15, 19, 20]
'''
a =[9,10,3,2,20,19]
b = [15,12,1,5,7,8]
c = []

for i in range(len(a)):
	c.append(a[i])

for i in range(len(b)):
	c.append(b[i])

print(c)

i = 0
while i < len(c):
	min = c[i]
	minIndex = i

	j = i
	while j < len(c):
		if min > c[j]:
			min = c[j]
			minIndex = j 
		j += 1
	
	temp = c[i]
	c[i] = c[minIndex]
	c[minIndex] = temp

	i += 1
print(c)