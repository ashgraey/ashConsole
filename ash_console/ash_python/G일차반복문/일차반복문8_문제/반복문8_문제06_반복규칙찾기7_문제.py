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
# [3차- 1110]
# # 못 풀었음
# # tip : plus변수를 생성해서 y값의 반복 카운트 역할로 사용해야함
# i = 0 
# x = 1
# while i < 10 :
# 	print(i, x)

# 	if i % x == 0 :
# 		x += 1 
# 	else :
# 		x = x 
# 	i += 1 

# [2차]
# a = 0 
# b = 1 
# plus = 1 

# i = 0 
# while i < 10 :
# 	print(a, b)
	
# 	a += 1
	 
# 	if plus < b :
# 		plus += plus
# 	else :
# 		b += 1 
# 		plus = 1 

# 	i += 1 

# [1차]
# a = 0
# b = 1 
# plus = 1

# i = 0
# while i < 9 : 
# 	print(a, b)
	
# 	a += 1 

# 	if plus < b :
# 		plus += plus
# 	else : 
# 		b += 1 
# 		plus = 1 
# 	i += 1 


