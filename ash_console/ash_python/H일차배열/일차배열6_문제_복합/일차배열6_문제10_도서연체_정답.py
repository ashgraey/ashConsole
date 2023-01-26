'''
	[문제]
		철수는 도서관에서 책을 한 권 빌렸다. 
		빌린 날짜는 작년 10월 10일이고, 대여 일수는 20일이다. 
		도서가 연체되면 연체 비용은 하루에 100원이다.
		오늘은 2월 25일 이라고 할 때, 지급해야 하는 비용은 얼마인지 구하시오.
		또한 작년 1월1일이 월요일이라고하면, 오늘은 무슨 요일인지 구하시오.
		단, 윤년은 계산하지 않는다.
	[정답]
		11800
'''

monthList = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

rentYear = 2020
rentMonth = 10
rentDay = 10

thisYear = 2022
thisMonth = 2
thisDay = 25

total = 0
# 연체비용
# 현재년도 - 빌린년도의 값이 1보다 클때
# 작년 이상일 경우
if thisYear - rentYear > 1:
	# 빌린날짜가 년단위만 total에 저장
	# 여기 코드만 다르고 total을 구하는 식은 작년 기준하고 동일
	total += (thisYear - rentYear - 1) * 365
	# 인덱스의 위치 -1, -rentday를 빼주면 대여 시작한 달의 대여일수가 나옴
	# total에 저장
	total += monthList[rentMonth - 1] - rentDay

	i = rentMonth
	# 남은 달의 대여일수도 total에 저장
	while i < len(monthList):
		total += monthList[i]
		i += 1
	print(total)

# 현재년도 - 빌린년도의 값이 1일때
# 작년기준 계산법
elif thisYear - rentYear == 1:
	# rentMonth - 1 : 10월의 날짜 인덱스의 값은 0부터 시작이니깐 인덱스 9가 나와야함
	# rentday를 빼면 10월 한달간 빌린 일수가 나옴
	total += monthList[rentMonth - 1] - rentDay

	# total값에 10월의 대여일수가 선 저장되어있음
	# 남은 11월, 12월의 인덱스 위치는 10,11
	# 즉, 11월, 12월의 대여일수도 모두 토탈 변수에 저장
	i = rentMonth
	while i < len(monthList):
		total += monthList[i]
		i += 1
	# 작년 기준 총 대여일수
	print(total) # 82


# 올해 대여 일수
i = 0
# 인덱스의 값으로 봐야하기때문에 thiMonth -1을 해준다.
# 빌린달 전달의 값을 total에 저장
while i < thisMonth - 1:
	total += monthList[i]
	i += 1
# 빌린달의 날짜 수를 total에 저장
total += thisDay
# total은 총 대여일수
print(total)

# total은 총 대여일수, 기본 대여일 : 20을 뺀 값이 총 연체일수
# 연체료 = 연체일 * 연체금액
price = (total - 20) * 100
print(price)