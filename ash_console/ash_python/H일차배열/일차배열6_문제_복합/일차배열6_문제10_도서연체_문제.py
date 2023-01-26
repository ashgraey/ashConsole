'''
	[문제]
		철수는 도서관에서 책을 한 권 빌렸다. 
		빌린 날짜는 작년 12월 10일이고, 대여 일수는 20일이다. 
		도서가 연체되면 연체 비용은 하루에 100원이다.
		오늘은 1월 25일 이라고 할 때, 지급해야 하는 비용은 얼마인지 구하시오.
		또한 작년 1월1일이 월요일이라고하면, 오늘은 무슨 요일인지 구하시오.
		단, 윤년은 계산하지 않는다.
	[정답]
		2600
'''
'''
빌린 날짜 = 12월 10일
대여일수 = 20
연체 비용_하루 = 100
오늘 날짜 = 1월 25일 
지급해야하는 비용 = ? 
오늘 요일 = ? 
각각의 개념을 따로 생각해야함
세분화 시키는게 중요
'''
monthList = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

rentYear = 2020
rentMonth = 12
rentDay = 10

thisYear = 2022
thisMonth = 1
thisDay = 25

total = 0 
# 빌린년도 대여일수
if thisYear - rentYear == 1 :
	total += monthList[rentMonth - 1] - rentDay
	
	if rentMonth - 1 < len(monthList) - 1 :
		i = rentMonth 
		while i < len(monthList) :
			total += monthList[i]
			i += 1 

elif thisYear - rentYear > 1 :
	total += (thisYear - rentYear - 1) * 365
	total += monthList[rentMonth - 1] - rentDay
	
	if rentMonth - 1 < len(monthList) - 1 :
		i = rentMonth 
		while i < len(monthList) :
			total += monthList[i]
			i += 1 

# 이번년도 렌트일수
if thisMonth - 1 > 0 :
	i = 0
	while i < thisMonth - 1 :
		total += monthList[i]
		i += 1

total += thisDay
rentPay = (total - 20) * 100

print(total)
print(rentPay)
