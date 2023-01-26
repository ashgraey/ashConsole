'''
	[문제]
		a 리스트가 데칼코마니인지 구하시오.
		데칼로마니이면 True를 출력 아니면 False 출력하시오.
		데칼코마니란? 절반으로 나눴을 때 서로 값들이 대칭이면 데칼코마니이다.

	[예시]	
		[1,5,4,4,5,1] True
		[1,5,4,3,5,1] False
'''


a = [1,5,4,4,5,1]

middle = len(a) // 2 # 리스트의 중간값

count = 0 

idx = len(a) - 1 # 리스트 마지막 인덱스 값 

for i in range(len(a) // 2) :
	# 데칼코마니인지 확인하는 조건
	# a[0] == a[5], a[1] == a[4], a[2] == a[3]
	if a[i] == a[idx] :
		count += 1 
	idx -= 1

# 반복문을 나와서 
# count의 값이 리스트의 절반값(middle)와 같다면 True
# 그렇지 않다면 False

if count == middle :
	print(True)
else :
	print(False)


