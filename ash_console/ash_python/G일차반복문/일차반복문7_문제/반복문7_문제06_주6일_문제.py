'''
	[문제]
		철수는 무인도를 사들여 국왕이 되었다.
		철수는 평소 월요일을 싫어해서 주 7일을 주 6일로 바꾸고 월요일을 삭제했다.
		5월 1일이 일요일이면, 
		5월 1일부터 5월31일까지 날짜와 요일을 전부 출력해보자.
				 
		[예시]
			1 일
			2 화
			3 수
			4 목
			5 금
			6 토
			7 일
			8 화
			9 수
			10 목
			...
			22 목
			23 금
			24 토
			25 일
			26 화
			...
			30 토
			31 일
'''
"""
일 1 7 13 19 25 31
월 2 8 14 20 26 
화 3 9 15 21 27
수 4 10 16 22 28
목 5 11 17 23 29
금 6 12 18 24 30
"""
월 = 31

i = 1 
while i <= 월 :
	unit = i % 6

	if unit == 1 :
		print(i, "일")
	if unit == 2 :
		print(i, "월")
	if unit == 3 :
		print(i, "화")
	if unit == 4 :
		print(i, "수")
	if unit == 5 :
		print(i, "목")
	if unit == 0 :
		print(i, "금")
	
	i += 1 

# 한달 = 31 

# i = 1 
# while i <= 한달 : 
# 	unit = i % 6

# 	if unit == 1 :
# 		print(i, "일")

# 	if unit == 2 :
# 		print(i, "월")
# 	if unit == 3 :
# 		print(i, "화")
# 	if unit == 4 :
# 		print(i, "수")
# 	if unit == 5 :
# 		print(i, "목")
# 	if unit == 0 :
# 		print(i, "금")
	
# 	i += 1 

