'''
	[문제]
		리스트의 모든 값이 짝수이면 True를 출력하고,
		단 하나라도 짝수가 아니면 False를 출력하는 함수를 작성하시오.
		단, 0은 짝수이다.
	[정답]
		True
'''

def allEven(arr) :
	cnt = 0 
	for i in range(len(arr)) :
		if arr[i] % 2 == 0 :
			cnt += 1
		else :
			cnt = 0 
	if cnt == len(arr) :
		ck = True
	else :
		ck = False

	return ck 

arr = [8, 0, 2, 6]
result = allEven(arr)
print("전부 짝수 : ", result)


