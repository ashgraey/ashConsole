'''
	[1] 비교연산자를 활용해 짝수 , 홀수 판별법 
		(1) 짝수 : 2의 배수이면 짝수 
		(2) 홀수 : 2의 배수가 아니면 홀수 
 		(3) 2의 배수 : 어떤수를 2로나눴을때 나머지가 0 이면 2의배수 
  		(4) 3의 배수 : 어떤수를 3으로나눴을때 나머지가 0 이면 3의 배수 
'''

a = 3
print(a % 3 == 0) # 3의배수이다.

b = 2
print(b % 2 == 0) # (짝수) 2의배수이다.

c = 5
print(c % 2 != 0) # (홀수) 2의배수가 아니다.