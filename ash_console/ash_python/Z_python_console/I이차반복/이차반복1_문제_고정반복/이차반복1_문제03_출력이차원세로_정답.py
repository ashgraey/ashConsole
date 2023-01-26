'''
	[문제]
		3~6 사이의 랜덤 숫자 하나를 저장하고 그 숫자만큼 아래와 같은 규칙으로 출력하시오.
		단, 이차 반복문으로 출력하시오.
 	[예시1]
		r = 6
	[출력]
		1 2 3 4 5 6
		1 2 3 4 5 6
		1 2 3 4 5 6
  
   	[예시2]
		r = 3
	[출력]
		1 2 3 
		1 2 3 
		1 2 3 
  
'''
import random

r = random.randint(3, 6)
print("r =", r)

for i in range(3):
	for j in range(r):
		print(j+1, end=" ")
	print()




