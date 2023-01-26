'''
	[문제]
		랜덤(1~5)숫자 하나를 저장하고 그 숫자만큼 a 리스트를 순환시키시오.
		순환이란, 모든 값을 뒤로 밀고 맨 뒤의 값은 맨 앞으로 오는 것을 의미한다.
	[예시]
		a = [10,20,30,40,50]
		r = 3
		랜덤이 3이 나왔으므로, 아래와 같이 세번 순환을 한다.
		
		a = [50,10,20,30,40]
		a = [40,50,10,20,30]
  		a = [30,40,50,10,20]
'''
import random 

a = [10,20,30,40,50]

r = random.randint(1, 5)
print("r =", r)

for i in range(r):
	index = len(a) - 1
	temp = a[index]

	while index > 0:
		a[index] = a[index - 1]
		index -= 1
	a[0] = temp
	print(a)


    




