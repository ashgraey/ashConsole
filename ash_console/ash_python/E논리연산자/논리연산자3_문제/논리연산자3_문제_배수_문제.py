'''	
	[문제] 
		아래 변수의 a값이 
	  	100의 자리가 6의 배수 이거나 10의 자리가 짝수이면,
	  	True 출력하시오.
	[정답]
		True
'''
a = 3640
백의자리 = a % 1000 // 100
십의자리 = a % 100 // 10
print(백의자리)
print(십의자리)
print(백의자리 % 6 == 0 or 십의자리 % 2 == 0)

