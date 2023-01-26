'''
	[문제] 
		a의 값을 순차적으로 c에 저장하고,
		그 후 b의 값을 c의 그 뒤부터 저장하시오.
	[정답] 
	 	a = [10,20,30]
		b = [40,50,60]
		
		c = [10,20,30,40,50,60]
'''


a = [10, 20, 30]
b = [40, 50, 60]

c = []

for i in range(len(a)):
	c.append(a[i])

for i in range(len(b)):
	c.append(b[i])
	
print("c =", c)
