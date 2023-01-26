'''
	[문제]
		철수는 도서관에서 책을 한 권 빌렸다. 
		빌린 날짜는 2021년 10월 10일이고, 대여 일수는 20일이다. 
		도서가 연체되면 연체 비용은 하루에 100원이다.
		오늘은 2022년 2월 25일 이라고 할 때, 지급해야 하는 비용은 얼마인지 구하시오.
		또한 2021년 1월1일이 월요일이라고하면, 오늘은 무슨 요일인지 구하시오.
		단, 윤년은 계산하지 않는다.
	[정답]
		11800
'''

monthList = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

rentYear = 2021
rentMonth = 10
rentDay = 10

thisYear = 2022
thisMonth = 2
thisDay = 25

total = 0
if thisYear - rentYear > 1:
	total += (thisYear - rentYear - 1) * 365
	total += monthList[rentMonth - 1] - rentDay

	i = rentMonth
	while i < len(monthList):
		total += monthList[i]
		i += 1
	print(total)
elif thisYear - rentYear == 1:
	total += monthList[rentMonth - 1] - rentDay

	i = rentMonth
	while i < len(monthList):
		total += monthList[i]
		i += 1
	print(total)


i = 0
while i < thisMonth - 1:
	total += monthList[i]
	i += 1
total += thisDay
print(total)

price = (total - 20) * 100
print(price)