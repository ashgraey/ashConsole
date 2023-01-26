'''
	[문제]
		a리스트의 값을 b에 저장한다.
		단, 연속으로 중복되는 값은 한 개만 저장하고 나머지는 저장하지 않는다.
	[예시]
		b = [1,3,2,3,4,5,6]
'''
a = [1,1,1,3,3,3,3,2,2,3,3,3,4,5,6,6,6]
b = []

index = 0
b.append(a[index])

i = 1
while i < len(a):
	if b[index] != a[i]:
		b.append(a[i])
		index += 1
	i += 1
print(b)