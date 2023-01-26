'''
	[문제] 
		c리스트의 값을 a에 한번 b에 한번 교차로 추가하시오.
	[정답]
		a = [10,30,50]
		b = [20,40,60]
'''

c = [10,20,30,40,50,60]

a = []
b = []

for i in range(len(c)):
	if i % 2 == 0:
		a.append(c[i])
	else:
		b.append(c[i])
print("a =", a)
print("b =", b)