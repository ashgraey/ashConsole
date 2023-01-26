'''
	[문제]
		리스트의 모든 값이 짝수이면 True를 출력하고,
		단 하나라도 짝수가 아니면 False를 출력하는 함수를 작성하시오.
		단, 0은 짝수이다.
	[정답]
		True
'''
def checkEven(list):
	count = 0
	for i in range(len(list)):
		if list[i] % 2 == 0:
			count += 1
	if count == len(list):
		print(True)
	else:
		print(False)

arr = [10, 0, 2, 6]
checkEven(arr)

