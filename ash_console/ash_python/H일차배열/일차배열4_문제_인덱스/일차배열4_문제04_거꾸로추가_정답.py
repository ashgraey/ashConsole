'''
	[문제]
		a 리스트의 값을 b리스트에 추가한다.
		단, 값은 거꾸로 추가한다.
	[결과]
		b = [40,30,20,10]
'''

a = [10, 20, 30, 40]
b = []

index = len(a) - 1
for i in range(len(a)):
	b.append(a[index])
	index -= 1
print("b =", b)