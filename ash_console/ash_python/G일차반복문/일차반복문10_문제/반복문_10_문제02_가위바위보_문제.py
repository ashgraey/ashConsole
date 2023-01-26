'''
	[문제]
		철수와 민수는 계단에서 가위바위보를 한다. 	 	
		철수와 민수는 각각 0 ~ 2 의 랜덤 값을 저장한다.
		0 : 가위 , 1 : 바위 , 2 : 보를 뜻한다.	 
		철수와 민수는 50번째 계단의 위치에서 시작한다.
		룰은 다음과 같다.	
		이기면 3칸 올라가기, 비기면 2칸 올라가기, 지면 1칸 내려가기.	 	
		둘 중 아무나 100 이상 도착하거나 
		둘 사이의 간격이 10 이상이면 게임은 종료된다. 
		게임이 종료될 때까지 두 사람의 이동 경로를 출력하시오.
'''
'''

가위 0 바위 1 보 2 경우의 수

철수 0 민수 2 철수가 이김
철수 1 민수 0 철수가 이김
철수 2 민수 1 철수가 이김
철수 0 민수 1 민수가 이김
철수 1 민수 2 민수가 이김
철수 2 민수 0 민수가 이김
'''
# [3차 - 1111]
# import random

# 철수위치 = 50 
# 민수위치 = 50 

# 종료조건 = 100
# 간격 = 10

# 승리 = 3 
# 패배 = 1
# 무승부 = 2

# while True :		
# 	철수 = random.randint(0, 2)
# 	민수 = random.randint(0, 2)
# 	print("철수 =", 철수)
# 	print("민수 =", 민수)

# 	if 철수 == 민수 : 
# 		print("무승부")
# 		철수위치 += 무승부
# 		민수위치 += 무승부

# 	elif 철수 == 0 and 민수 == 2 :
# 		print("철수 승")
# 		철수위치 += 승리
# 		민수위치 -= 패배
# 	elif 철수 == 1 and 민수 == 0 :
# 		print("철수 승")
# 		철수위치 += 승리
# 		민수위치 -= 패배
# 	elif 철수 == 2 and 민수 == 1 :
# 		print("철수 승")
# 		철수위치 += 승리
# 		민수위치 -= 패배
# 	else :
# 		print("민수 승")
# 		민수위치 += 승리
# 		철수위치 -= 패배

# 	if 철수위치 >= 100 or 민수위치 >= 100 :
# 		print(철수위치, 민수위치)
# 		print("게임종료")
# 		break
	
# 	if 철수위치 - 민수위치 >= 10 or 민수위치 - 철수위치 >= 10 :
# 		print(철수위치, 민수위치)
# 		print("간격이 10이상 차이")
# 		break


# [2차]
# import random
# 철수_위치 = 50 
# 민수_위치 = 50

# run = 1 
# while run == 1 : 
# 	철수 = random.randint(0, 2)
# 	민수 = random.randint(0, 2)
# 	print("철수 =", 철수)
# 	print("민수 =", 민수)

# 	if 철수 == 민수 :
# 		철수_위치 += 2
# 		민수_위치 += 2
# 		print("무승부")

# 	if 철수 == 0 and 민수 == 1 :
# 		민수_위치 += 3
# 		철수_위치 -= 1 
# 		print("민수가 이김")
# 	if 철수 == 1 and 민수 == 2 :
# 		민수_위치 += 3
# 		철수_위치 -= 1 
# 		print("민수가 이김")
# 	if 철수 == 2 and 민수 == 0 :
# 		민수_위치 += 3
# 		철수_위치 -= 1 
# 		print("민수가 이김")

# 	if 철수 == 0 and 민수 == 2 :
# 		철수_위치 += 3
# 		민수_위치 -= 1
# 		print("철수가 이김")
# 	if 철수 == 1 and 민수 == 0 :
# 		철수_위치 += 3
# 		민수_위치 -= 1
# 		print("철수가 이김")
# 	if 철수 == 2 and 민수 == 1 :
# 		철수_위치 += 3
# 		민수_위치 -= 1
# 		print("철수가 이김")
	
# 	둘_차이 = 철수_위치 - 민수_위치 
# 	if 둘_차이 < 0 :
# 		둘_차이 = -둘_차이 

# 	if 철수_위치 >= 100 or 민수_위치 >= 100 or 둘_차이 >= 10 :
# 		print("게임종료")
# 		run = 0

# print("최종위치 =", 철수_위치, 민수_위치 )

# chul_total = 50
# min_total = 50

# [1차]
# run = 1
# while run == 1 : 
# 	print("철수 위치 =", chul_total)
# 	print("민수 위치 =", min_total)

# 	chul = random.randint(0,2)
# 	min = random.randint(0,2)
# 	print(chul, min)
	
# 	if chul == min : 
# 		chul_total += 2
# 		min_total += 2 
# 		print("비겼다")

# 	if chul == 0 and min == 1 : 
# 		chul_total -= 1
# 		min_total += 3 
# 		print("민수가 이김")

# 	if chul == 0 and min == 2 : 
# 		chul_total += 3 
# 		min_total -= 1
# 		print("철수가 이김")

# 	if chul == 1 and min == 0 : 
# 		chul_total += 3
# 		min_total -= 1 
# 		print("철수가 이김")

# 	if chul == 1 and min == 2 : 
# 		chul_total -= 1 
# 		min_total += 3
# 		print("민수가 이김")

# 	if chul == 2 and min == 0 : 
# 		chul_total -= 1
# 		min_total += 3 
# 		print("민수가 이김")

# 	if chul == 2 and min == 1 : 
# 		chul_total += 3 
# 		min_total -= 1
# 		print("철수가 이김")
	
# 	if chul_total >= 100 :
# 		print("철수가 이김")
# 		run = 0
# 	if min_total >= 100 :
# 		print("민수가 이김")
# 		run = 0 
# 	if chul_total - min_total == 10 or min_total - chul_total == 10 :
# 		print("10차이로 종료")
# 		run = 0


	# if chul > min : 
	# 	chul_total += 3 
	# 	min_total -= 2

	# if chul < min :
	# 	chul_total -= 2 
	# 	min_total += 3 
	
	# if chul_total >= 100 or min_total >= 100 or chul_total - min_total >= 10 or min_total - chul_total >= 10 :

# 		run = 0

# print(chul_total)
# print(min_total)
