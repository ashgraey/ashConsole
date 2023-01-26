'''
	[문제]
		랜덤(1~5) 숫자 하나를 저장하고 그 숫자만큼 a 리스트를 역순환시키시오.
		역순환이란, 모든 값들을 앞으로 밀고 맨 앞의 값은 맨 뒤로 이동하는 것을 말한다. 
	[예시]
		a = [10,20,30,40,50]
		r = 3
		랜덤이 3이 나왔으므로, 아래와 같이 세 번 역순환을 한다.
		
		a = [20,30,40,50,10]
		a = [30,40,50,10,20]
  		a = [40,50,10,20,30]
	
'''
import random 

a = [10,20,30,40,50]

# 1216
r = random.randint(1, 5)
print("random : ", r)

for i in range(r) :
	temp = a[0]

	for j in range(len(a) - 1) :
		a[j] = a[j + 1]
	
	a[len(a)-1] = temp
	print(a)

# 1125
# r = random.randint(1, 5)
# print("r =", r)

# for i in range(r) :
# 	temp = a[0]
	
# 	j = 0
# 	while j < len(a) - 1 : 
# 		a[j] = a[j + 1]
# 		j += 1 
	
# 	a[len(a) - 1] = temp	
# 	print(a)

# 1123
# r = random.randint(1, 5) 
# print("r =", r) 

# # a.append(temp)
	
	
# for i in range(r) :
# 	temp = a[0]
# 	# idx = 1
# 	for j in range(len(a) - 1) :
# 		a[j] = a[j + 1]
# 		# idx += 1
# 	a[len(a) - 1] = temp
# 	print(a)
	




    




