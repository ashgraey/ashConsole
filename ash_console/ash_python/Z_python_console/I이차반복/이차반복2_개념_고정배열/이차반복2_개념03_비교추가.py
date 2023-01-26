'''
	[문제]
		a리스트와 b리스트를 전체 비교하여 
		a리스트 안에도 있고 b리스트 안에도 있는 값은 
		c리스트에 저장하시오.
	[정답]
		c = [10, 20]
'''
a = [10, 20, 30, 40]
b = [10, 5, 20, 9]
c = []

for i in range(len(a)):
    for j in range(len(b)):
        if a[i] == b[j]:
        	c.append(a[i])
  
print(c)