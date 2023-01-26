'''
	[문제]
		아래 a리스트는 최근 주식의 변동을 저장한 값이다. 
		숫자들은 가격을 의미한다. 
		리스트의 값들 중 연속으로 가장 많이 오른 기간이 얼마인지 출력하시오.
	[예시]
		(1) 3, 1 은 떨어진 것이다.
		(2) 1, 2 는 오른 것이다.
		(3) 2, 7 는 오른 것이다.
		(4) 7, 2 는 떨어진 것이다. (여기까지 연속으로 가장 많이 오른 것은 2일이다.)
		(5) 2, 3 은 오른 것이다.
		(6) 3, 4 는 오른 것이다.
		(7) 4, 6 은 오른 것이다.
		(8) 6, 1 은 떨어진 것이다. (여기까지 연속으로 가장 많이 오른 것은 3일이다.)
	[정답]
		3일 
'''

a = [3, 1, 2, 7, 2, 3, 4, 6, 1]
# print(len(a) - 1 )
count = 0
maxCount = 0

[1116]
for i in range(len(a) - 1) :
	if a[i] < a[i + 1] :
		count += 1
		if count > maxCount :
			maxCount = count 
	else :
		count = 0 
print(maxCount,"일")

# [1차]
start = 0
end = 1
for i in range(len(a) - 1):
	print(a[start], a[end])
	
	# 리스트 비교 중 큰값일때 count += 1 
	if a[start] < a[end]:
		start = end
		end += 1
		count += 1
	# 중간에 떨어지면 count = 0으로 초기화 하는 식이 있음
	else:
		start = i + 1
		end = start + 1
		count = 0
	
	if maxCount < count:
		maxCount = count
print(maxCount)