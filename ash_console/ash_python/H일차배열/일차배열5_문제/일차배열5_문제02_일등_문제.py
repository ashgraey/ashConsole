'''
	[문제]
		다음은 학생 번화와 점수의 한 세트이다.
		일등의 번호와 점수, 꼴등의 번호와 점수를 출력하시오.
	[정답]
		일등 = 1004 98
		꼴등 = 1002 11
'''


numberList = [1001, 1002, 1003, 1004, 1005]
scoreList = [87, 11, 45, 98, 23]

max = 0
min = 100 
maxIdx = 0 
minIdx = 0

for i in range(len(numberList)) :

	if max < scoreList[i] :
		max = scoreList[i]
		maxIdx = i

	if min > scoreList[i] :
		min = scoreList[i]
		minIdx = i

print("일등 =", numberList[maxIdx], max)
print("꼴등 =", numberList[minIdx], min)