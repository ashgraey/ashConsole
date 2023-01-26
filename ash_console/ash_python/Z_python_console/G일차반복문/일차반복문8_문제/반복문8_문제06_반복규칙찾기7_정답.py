'''  	
	[문제]
		반복문을 10회 반복해서 아래와 같이 출력하시오.
		
		[예시]
			0 1
			1 2
			2 2
			3 3
			4 3
			5 3
			6 4
			7 4
			8 4
			9 4
'''
x = 0
y = 1

plus = 1

i = 0
while i < 10:
	print(x, y)
	check = False

	x += 1
	if plus < y:
		plus += 1
		check = True
	if check == False and plus >= y:
		y += 1
		plus = 1

	i += 1
