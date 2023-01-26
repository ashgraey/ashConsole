'''
	[문제]
		1. 10회 반복을 한다.
		2. 0~100 사이의 랜덤 숫자를 출력한다. (학생 점수)
		3. 번호는 1번부터 시작한다. 번호와 점수를 출력한다. 
		4. 성적이 60점 이상이면 합격생이다. 
		   합격생은 점수 옆에 [합격]을 불합격생은 [불합격]을 출력한다. 
		5. 전교생(10명)의 총점과 평균을 출력한다.
		6. 1등의 번호와 점수를 출력한다.
'''
# [2차 - 1111]
# import random

# 합격여부 = "" 
# max = 0
# max_idx = 0

# total = 0
# i = 1 
# while i <= 10 :
#     score  = random.randint(0, 100)

#     if score >= 60 :
#         합격여부 = "[합격]"
#         total += score
#     else :
#         합격여부 = "[불합격]"
#         total += score

#     if max < score :
#         max = score
#         max_idx = i

#     print("번호 =", i, "점수 =", score, 합격여부)
#     i += 1 
# print()
# print("총점 =", total)
# print("평균 =", total / 10)
# print("1등 번호 =", max_idx, "점수 =", max)

# [1차]
# 일등 = 0 
# total = 0
# i = 1 
# while i <= 10 :
#     r = random.randint(0, 100)
#     # print("번호",i,"=",r,)

#     if r >= 60 :
#         print("번호",i,"=",r,"합격")
#     else :
#         print("번호",i,"=",r,"불합격")

#     if r > 일등 :
#         번호 = i
#         일등 = r

#     total += r 
       
#     i += 1 
# avg = total / 10
# print("합계 =",total)
# print("평균 =", avg)
# print("일등 =", "번호", 번호, 일등)















# total = 0
# i = 0
# while i <= 10 : 
# 	num = random.randint(0, 100)
# 	# print(num, end = " ")

# 	if i == 1 : 
# 		# print(i, num)
# 		if num >= 60 : 
# 			print(i, num, "합격")
# 		if num < 60 : 
# 			print(i, num, "불합격")
# 	if i == 2 : 
# 		print(i, num)
# 	if i == 3 : 
# 		print(i, num)
# 	if i == 4 : 
# 		print(i, num)
# 	if i == 5 : 
# 		print(i, num)
# 	if i == 6 : 
# 		print(i, num)
# 	if i == 7 : 
# 		print(i, num)
# 	if i == 8 : 
# 		print(i, num)
# 	if i == 9 : 
# 		print(i, num)
# 	if i == 10 : 
# 		print(i, num)
	
# 	i += 1 

# [정답]
# import random

# total = 0

# maxScore = 0
# maxIndex = 0

# i = 1
# while i <= 10:
#     score = random.randint(0, 100)

#     if maxScore < score:
#         maxScore = score
#         maxIndex = i

#     total += score

#     if score >= 60:
#         print(score, "[합격]")
#     if score < 60:
#         print(score, "[불합격]")
    
#     i += 1

# avg = total / 10
# print("총점 =", total)
# print("평균 =", avg)
# print("1등 =", maxScore, ":", maxIndex)