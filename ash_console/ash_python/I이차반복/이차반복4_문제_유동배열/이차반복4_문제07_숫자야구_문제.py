'''
	[문제]		
		[1] com리스트에 0~9사이의 랜덤 숫자 3개를 저장하되 중복 값이 없어야 한다.
		[2] me리스트에 0~9사이의 랜덤 숫자 3개를 저장하되 중복 값이 없어야 한다.
		[3] com과 me 를 비교해서 숫자가 같고 자리도 같으면 strike + 1
		[4] com과 me 를 비교해서 숫자가 같고 자리가 틀리면 ball + 1
		[5] 사용자에게 strike와 ball 개수를 출력해 보여준다.
		
		계속 반복하면서 strike가 3이 되면 종료한다.
'''
import random

com = [0, 0, 0]
me = [0, 0, 0]

# 1124
# com 중복x, 랜덤값
# i = 0 
# while i < 3 : 
# 	r = random.randint(0,9)
# 	check = False

# 	j = 0 
# 	while j < i : 
# 		if com[j] == r : 
# 			check = True
# 			# continue
# 		j += 1 

# 	if check == False :
# 		com[i] = r
# 		i += 1 
# print("com =", com)

# # me 중복x, 랜덤값
# # strike, ball 판단 
# # 무한반복 -> strike == 3이면 반복종료
# # 무한반복 동안 me의 랜덤값은 계속 바뀜
# while True :
# 	i = 0 
# 	while i < 3 : 
# 		r = random.randint(0,9)
# 		check = False

# 		j = 0 
# 		while j < i : 
# 			if me[j] == r : 
# 				check = True
# 			j += 1 

# 		if check == False :
# 			me[i] = r
# 			i += 1 
# 	print("me =", me)
	
# 	# com,me list 비교
# 	# idx와 값이 같으면 strike
# 	# 값만 같으면 ball
# 	# 3strike = out 반복 종료
# 	strike = 0
# 	ball = 0 
# 	for i in range(len(com)) :
# 		for j in range(len(me)) :
# 			if i == j and com[i] == me[j] :
# 				strike += 1
# 			elif i != j and com[i] == me[j] :
# 				ball += 1 
	
# 	print("strike =", strike)
# 	print("ball =", ball)

# 	if strike == 3 :
# 		print("Out!!!")
# 		print("com =", com)
# 		break

# 1122
# i = 0
# while True :
# 	# 문제 이해가 잘못됨
# 	# com값은 한번만 저장하고 me값만 strike가 3이 될때까지 변함
# 	# com값과 me값 모두 게임마다 변하게 만들었음
# 	r1 = random.randint(0, 9)
# 	r2 = random.randint(0, 9)
# 	check = False

# 	for j in range(len(com)) :
# 		if com[j] == r1 or me[j] == r2 : 
# 			check = True
# 			continue
	
# 	if check == False :
# 		com[i] = r1
# 		me[i] = r2
# 		i += 1 
	
# 	if i == len(com) :
# 		i = 0 
	
# 	print()
# 	print(com)
# 	print(me)
	
# 	strike = 0 
# 	ball = 0 
# 	for x in range(len(com)) :
# 		for y in range(len(me)) :
# 			if x == y and com[x] == me[y] :
# 				strike += 1 
# 			elif x != y and com[x] == me[y] :
# 				ball += 1 

# 	print("strike =", strike)
# 	print("ball =", ball)
	
# 	if strike == 3 : 
# 		break 






