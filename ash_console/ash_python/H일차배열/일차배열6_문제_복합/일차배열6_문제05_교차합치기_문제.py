'''
	[문제] 
		a의 값과 b의 값을 교차로 c에 추가하시오.
		규칙은 아래와 같다.
		
		c = [10]     
		c = [10,40]  
		c = [10,40,20]
		c = [10,40,20,50]
		c = [10,40,20,50,30]
		c = [10,40,20,50,30,60]
	[정답]
		c = [10,40,20,50,30,60]
'''
'''
조건1 = 2개씩 끊어서


'''

a = [10,20,30]
b = [40,50,60]

c = []

# [1118]
# for i in range(len(a)) :
# 	c.append(a[i])
# 	c.append(b[i])
# print(c)

# [1116]
# for i in range(len(a)) :
# 	c.append(a[i])
# 	c.append(b[i])
# print(c)

# [1차] 
# for i in range(len(a)) :
# 	c.append(a[idx])
# 	c.append(b[idx])		
# 	idx += 1 
# print(c)
