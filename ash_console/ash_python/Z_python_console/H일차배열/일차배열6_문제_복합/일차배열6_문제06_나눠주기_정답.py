'''
	[문제] 
		c리스트의 값의 절반을 a리스트에 추가한 후, 
		나머지 절반은 b리스트에 추가하시오.
	[정답]
		a = [10,20,30]
		b = [40,50,60]
'''

c = [10,20,30,40,50,60]
a = []
b = []

for i in range(len(c)):
	if i < len(c) / 2:
		a.append(c[i])
	else:
		b.append(c[i])

print(a)
print(b)