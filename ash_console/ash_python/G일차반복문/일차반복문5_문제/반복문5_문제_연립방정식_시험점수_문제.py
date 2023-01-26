'''
	[문제]
		철수네 학교의 수학 시험은 4점짜리 문제와 5점짜리 문제가 섞여서 출제된다.	
		철수는 20개의 문제를 맞혀서 90점을 받았다. 	
		각각 몇 문제씩 맞혔는지 구하시오. 
		주석으로 표현하시오.
	[정답]
		4점 문제 = 10
		5점 문제 = 10
'''
'''
math4 = 4 
math5 = 5 

total = 20
score = 90

math4_ea a
math5_ea b 

a + b = total
math4 * a + math5 * b = score

a + b = 20
a = 20 - b

4(20 - b) + 5b = 90
80 - 4b + 5b = 90
b = 10 
a = 10
'''
# [1110]
# math4 = 4 
# math5 = 5 

# total = 20
# score = 90

# math4_ea = total 
# math5_ea = 0

# i = 1 
# while i <= total :
# 	if math4_ea + math5_ea == total and (math4 * math4_ea) + (math5 * math5_ea) == score :
# 		print("4점 개수 =",math4_ea)
# 		print("5점 개수 =", math5_ea)

# 	math4_ea -= 1 
# 	math5_ea += 1
# 	i += 1 
"""
사점 = 4
오점 = 5
철수_문제수 = 20
철수_점수 = 90

사점_맞힌수 = x = 10 
오점_맞힌수 = y = 10

x + y = 20
x = 20 - y

4x + 5y = 90
4(20 - y) + 5y = 90
80 - 4y + 5y = 90
1y = 10
x = 10
"""
# []
# 총_문제수 = 20
# 총_점수 = 90

# 사점_맞힌수 = 총_문제수
# 오점_맞힌수 = 0

# run = 1 
# while run == 1 :
# 	if 사점_맞힌수 + 오점_맞힌수 == 총_문제수 and 사점_맞힌수 * 4 + 오점_맞힌수 * 5 == 총_점수 :
# 		print("사점_맞힌수 =", 사점_맞힌수)
# 		print("오점_맞힌수 =", 오점_맞힌수)
# 		run = 0 
	
# 	else :
# 		사점_맞힌수 -= 1
# 		오점_맞힌수 += 1


