'''
	[문제]	  
		철수는 최근 무인도를 구입하고, 그 나라의 왕이 되었다.
		평소 월요병이 있던 철수는 일주일에서 월요일을 삭제하였다.
		만약 이번 달 1일이 일요일일 때, 랜덤으로 1~31을 저장하고,
		해당 날짜의 요일을 출력하시오.

		[예]
			1 : 일요일
			2 : 화요일
			3 : 수요일
			4 : 목요일
			5 : 금요일
			6 : 토요일
			7 : 일요일
			8 : 화요일 
			...
'''  
import random

num = random.randint(1, 31)
print("num =", num)

unit = num % 6 
if unit == 1 :
	print(num, ":", "일요일")
if unit == 2 :
	print(num, ":", "화요일")
if unit == 3 :
	print(num, ":", "수요일")
if unit == 4 :
	print(num, ":", "목요일")
if unit == 5 :
	print(num, ":", "금요일")
if unit == 0 :
	print(num, ":", "토요일")
