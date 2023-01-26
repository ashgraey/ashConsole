'''
	[문제]
		아래 배열은 3명의 학생 데이터이다.		
		각 학생은 3개씩 데이터로 표현한다. 
		맨 앞은 번호, 그다음은 국어점수, 그다음은 수학점수이다.					
		(예) 
			1001번, 국어 100, 수학 20
			1002번, 국어 32,  수학 54
			1003번  국어 34,  수학 65	

		[1] 전체 평균을 출력하시오.
		[2] 국어 1등 학생을 출력하시오.
		[3] 수학 1등 학생을 출력하시오.
		[4] 전체 1등 학생을 출력하시오.
'''
'''
1. 전체평균
- 점수 인덱스 : 1 2 4 5 7 8
- 국어 : 1 , 4 , 7
- 수학 : 2  5  8 
'''
a = [1001, 100, 20, 1002, 32, 54, 1003, 34, 65]

# [1116]
kor = 0
maxKor = 0
maxKoridx = 0
math = 0 
maxMath = 0
maxMathidx = 0  
total1 = 0
maxTotal1 = 0  
maxTotal1idx = 0 

total = 0 
for i in range(len(a)) :
	if i % 3 == 1 :
		total += a[i] + a[i + 1]
	
		total1 = a[i] + a[i + 1]
		if total1 > maxTotal1 :
			maxTotal1 = total1
			maxTotal1idx = i - 1
		
		kor = a[i]
		if maxKor < kor :
			maxKor = kor
			maxKoridx = i - 1
	
	if i % 3 == 2 :
		math = a[i]
		if maxMath < math :
			maxMath = math
			maxMathidx = i - 2
avg = total / 3
print("전체 평균 =",round(avg,2))
print("국어 1등 =", a[maxKoridx], maxKor)
print("수학 1등 =", a[maxMathidx], maxMath)
print("전체 1등 =", a[maxTotal1idx], maxTotal1)

# [1차]
# idx = 1

# total = 0 
# for i in range(len(a)) :
# 	if i % 3 == 0 :
# 		total += a[i + 1] + a[i + 2]
	
# 		# print(total)
# avg = total / (len(a) // 3)
# print("전체평균 =", round(avg, 2)) 

# korMax = 0
# korIdx = 0
# mathMax = 0
# mathIdx = 0 
# totalMax = 0 
# totalIdx = 0
# total = []
# for i in range(len(a)) :
# 	if i % 3 == 1 :
# 		if korMax < a[i] : 
# 			korMax = a[i]
# 			korIdx = i 
	
# 	if i % 3 == 2 :
# 		if mathMax < a[i] :
# 			mathMax = a[i]
# 			mathIdx = i
	
# 	if i % 3 == 0 :
# 		total1 = a[i + 1] + a[i + 2]
# 		total.append(total1)
# 		# print(total)
# 		if i < 3 :
# 			if totalMax < total[i] :
# 				totalMax = total[i]
# 				totalIdx = i


# print("국어 1등 =", korMax, a[korIdx - 1])
# print("수학 1등 =", mathMax, a[mathIdx - 2])
# print("전체 1등 =", totalMax, a[totalIdx])