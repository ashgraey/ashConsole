'''
	[문제]
		철수는 2시간 동안 블럭을 231개 쌓았다. 
		민수는 1시간 반동안 블럭을 177개 쌓았다.
		철수가 민수보다 블럭쌓는속도가 더빠른가요? 
	
		위내용을 비교연산자로 표현하시오.
'''
'''
철수 
2 : 231 = 1.5 : ?
2? = 231 * 1.5
? = 231 * 1.5 / 2
'''
민수블럭 = 177
철수_1시간반_블럭 = 231 * 1.5 / 2 
print(철수_1시간반_블럭)
print(철수_1시간반_블럭 > 민수블럭)