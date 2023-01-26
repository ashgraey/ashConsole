'''
	[문제]
		a리스트는 학생 번호와 점수 한 세트를 이루고 있다.		
		일등 학생의 번호와 점수를 출력하시오.
	[정답]
		번호 = 1002
		점수 = 82
'''
'''
점수 idx = i % 2 == 1

조건1 : 점수 인덱스 번호만 찾기
조건2 : 가장 높은 점수 찾기, 
- 최대값 변수를 하나 생성 -> 최대값 < 점수 리스트[] 값 비교 -> 점수 리스트의 값이 크다면 최대값 변수에 저장
-> 다시 비교 최대의 값이 나올때 까지
조건3 : 번호 인덱스는 점수 인덱스 왼쪽에 위치 - 1을 해준다.

'''
a = [1001, 40, 1002, 82, 1003, 65, 1004, 70]
maxScore = 0 
maxIndex = 0 

# [1116]
# for i in range(len(a)) :
# 	if i % 2 == 1 :
# 		if maxScore < a[i] :
# 			maxScore = a[i]
# 			maxIndex = i - 1 

# print(a[maxIndex], maxScore)

# [1차]
# for i in range(len(a)) :
# 	if i % 2 == 1 : 
# 		if maxScore < a[i] :
# 			maxScore = a[i]
# 			maxIndex = i

# print("번호 =", a[maxIndex - 1])
# print("점수 =", maxScore)
		
