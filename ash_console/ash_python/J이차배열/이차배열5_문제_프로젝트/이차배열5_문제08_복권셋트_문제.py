'''
	[문제]
		복권 1개당 7칸으로, 총 5개의 복권을 제작하려 한다.
		복권 1줄은 1 또는 7의 랜덤 숫자로 구성되어 있다.
		7이 연속으로 3개 이상이면 "당첨"이고, 그 미만은 "꽝"이다.
		5개 중에 딱 1개만 당첨 복권이고 나머지 4개는 꽝인 복권을
		랜덤으로 생성해서 출력하시오.
		
		예)
			1177117 (꽝)
			1117771 (당첨)
			7171117 (꽝)
			7711771 (꽝)
			7171717 (꽝)
'''
import random
# 0113
# 7칸 5개
# lottoList = []
# win = 0
# while True :
	
# 	lotto = []
# 	for i in range(7) :
# 		r = random.randint(0, 1) 
		
# 		if r == 0 :
# 			r = 1
# 		elif r == 1 :
# 			r = 7
		
# 		lotto.append(r)
	
# 	# 당첨확인 검사
# 	ck = False 
# 	cnt = 0
# 	for i in range(7) :
# 		if lotto[i] == 7 :
# 			cnt += 1 
# 			if cnt >= 3 :
# 				ck = True
# 				break 
		
# 		elif lotto[i] == 1 :
# 			cnt = 0
	
# 	# 당첨복권 하나만 lottoList에 추가
# 	if ck == True and win == 0 : 
# 		lottoList.append(lotto)
# 		win += 1
		
# 	elif ck == False and win == 1 : 
# 		lottoList.append(lotto)

# 	# 종료식
# 	if win == 1 and len(lottoList) == 5 :
# 		break

# # 셔플
# for i in range(100) :
# 	idx = random.randint(1, len(lottoList) - 1)
# 	temp = lottoList[0]
# 	lottoList[0] = lottoList[idx]
# 	lottoList[idx] = temp

# # 당첨여부 확인 & 출력
# for i in range(len(lottoList)) :
# 	cnt = 0
# 	ck = False
# 	for j in range(len(lottoList[i])) :
# 		if lottoList[i][j] == 7 :
# 			cnt += 1 
# 			if cnt >= 3 :
# 				ck = True
# 				break
# 		elif lottoList[i][j] == 1 :
# 			cnt = 0

# 	if ck == False :
# 		print(lottoList[i], "꽝")
# 	else :
# 		print(lottoList[i], "당첨")
		
# 1219
# lotto = []
# # 총 5개, 리스트의 길이 7
# cnt = 0 
# while True :

# 	ck = False
# 	temp = []

# 	# 7칸의 랜덤 복권 제작
# 	while True :
# 		r = random.randint(0,1)
# 		# print("r : ", r)

# 		if r == 0 :
# 			r = 1
# 			temp.append(r)
		
# 		elif r == 1 :
# 			r = 7
# 			temp.append(r)
			
# 		if len(temp) == 7 :
# 			break

# 	# 당첨복권 확인
# 	cnt7 = 0
# 	for j in range(len(temp)) :
# 		if temp[j] == 7 :
# 			cnt7 += 1
# 		else :
# 			cnt7 = 0 
	
# 		if cnt7 >= 3 :
# 			ck = True
# 			break		
	
# 	# 첫번째에 당첨 복권 777을 저장
# 	# 두번째부터는 꽝을 넣는다.
# 	if ck == True and cnt == 0 :
# 		lotto.append(temp)
# 		# print(temp, "당첨")
# 		cnt += 1
# 	elif ck == False and cnt != 0 :
# 		lotto.append(temp)
# 		# print(temp, "꽝")
# 		cnt += 1 

# 	if cnt == 5 : 
# 		break 

# # 셔플
# for i in range(100) :
# 	r = random.randint(0, len(lotto) - 1)
# 	temp = lotto[0]
# 	lotto[0] = lotto[r]
# 	lotto[r] = temp

# # 출력 및 당첨, 꽝 확인
# for i in range(len(lotto)) :
# 	cnt = 0
# 	ck = False
# 	for j in range(len(lotto[i])) :
# 		if lotto[i][j] == 7 :
# 			cnt += 1 
# 		else :
# 			cnt = 0
		
# 		if cnt >= 3 :
# 			ck = True
# 			break
	

# 	if ck == True :
# 		result = "당첨"
# 	else :
# 		result = "꽝"

# 	print(lotto[i], result)
	
	

		
		

		
	


		

		


		






















# 1213
# 7이 연속으로 3개인 당첨이 하나이고, 꽝이 4개인 lotto리스트 만들기
# size = 0 
# while True :
# 	lt = []
# 	cnt = 0 
# 	check = False
# 	for i in range(7) : 
# 		n = random.randint(0, 1) 

# 		if n == 0 :
# 			n = 1 
# 			cnt = 0
# 		elif n == 1 :
# 			n = 7 
# 			cnt += 1 
		
# 		if cnt >= 3 :
# 			check = True

# 		lt.append(n)
	
# 	# 첫번째에 당첨인 로또 리스트를 저장한다.
# 	if check == True and size == 0 :
# 		lotto.append(lt)
# 		size += 1 

# 	# 첫번째 이후부터는 꽝인 리스트를 저장한다.
# 	elif size > 0 and check == False :
# 		lotto.append(lt)
# 		size += 1 
	
# 	if size == 5 :
# 		break

# # 셔플
# for i in range(10) :
# 	temp = []
# 	r = random.randint(0,4)
# 	temp.append(lotto[r])
# 	lotto[r] = lotto[0]
# 	lotto[0] = temp[0]

# # 출력
# for i in range(len(lotto)) :
# 	count = 0 
# 	result = "꽝"
# 	for j in range(len(lotto[i])) :
# 		if lotto[i][j] == 7 :
# 			count += 1 
# 		else :
# 			count = 0
		
# 		if count == 3 :
# 			result = "당첨"

# 	print(lotto[i], result)
	
# 1차 시도
# for i in range(len(lotto)) :
# 	lotto2.append(lotto)
# # print(lotto2)

# cnt = 0
# while True : 

# 	for i in range(len(lotto)) :
# 		for j in range(len(lotto)) :
# 			l = random.randint(0, 1) 
# 			if l == 0 :
# 				l = 1
		
# 			elif l == 1 :
# 				l = 7

# 			lotto2[i][j] = l
# 	cnt += 1

# 	if cnt == 5 :
# 		break		

# print(lotto2)

# for i in range(len(lotto2)) :
# 	for j in range(len(lotto2[i])) :	
# 		print(lotto2[i][j], end = " ")
# 	print()
# print()

# for i in range(len(lotto)) :s

# 1차 결과
# while True : 
# # 7개의 로또 번호를 추첨
# 	lotto = [0, 0, 0, 0, 0]

# 	for i in range(len(lotto)) :
# 		temp = []
# 		for j in range(7) :
# 			r = random.randint(0, 1)

# 			if r == 0 :
# 				r = 1
# 			elif r == 1 :
# 				r = 7
			
# 			temp.append(r)
# 		# print(temp)
# 		lotto[i] = temp

# #  당첨여부 확인
# 	win = 0 
# 	for i in range(len(lotto)) :
# 		cnt = 0
# 		for j in range(len(lotto[i])) :
# 			if lotto[i][j] == 7 :
# 				cnt += 1
# 			else :
# 				cnt = 0
		
# 			if cnt == 3 :
# 				win += 1 

# 	# print(win)
# 	if win == 1 :
# 		print("당첨")
# 		for i in range(len(lotto)) :
# 			for j in range(len(lotto[i])) :
# 				print(lotto[i][j], end = " ")
# 			print()
# 		print()
# 		break
		


	
		
		
		


