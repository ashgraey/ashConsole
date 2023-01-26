'''
	[문제]
        철수는 게임을 만들고 있다. 
        (1~6 사이의 랜덤 숫자)주사위를 던져
		해당 숫자만큼 캐릭터를 이동시킨다.
		단, 캐릭터는 외곽으로만 움직일 수 있다.
		두 바퀴를 돌고 게임을 끝내시오.
	[예시]
		옷 □ □ □ □ 
		□ ■ ■ ■ □  
		□ ■ ■ ■ □  
		□ ■ ■ ■ □  
		□ □ □ □ □  

		dice = 2   
		□ □ □ 옷 □ 
		□ ■ ■ ■ □  
		□ ■ ■ ■ □  
		□ ■ ■ ■ □  
		□ □ □ □ □  

		dice = 3   
		□ □ □ □ □  
		□ ■ ■ ■ □  
		□ ■ ■ ■ 옷 
		□ ■ ■ ■ □  
		□ □ □ □ □  

		dice = 3   
		□ □ □ □ □  
		□ ■ ■ ■ □
		□ ■ ■ ■ □
		□ ■ ■ ■ □
		□ □ □ 옷 □

		dice = 1
		□ □ □ □ □
		□ ■ ■ ■ □
		□ ■ ■ ■ □
		□ ■ ■ ■ □
		□ □ 옷 □ □

		dice = 6
		옷 □ □ □ □
		□ ■ ■ ■ □
		□ ■ ■ ■ □
		□ ■ ■ ■ □
		□ □ □ □ □

		dice = 5
		□ □ □ □ □
		□ ■ ■ ■ 옷
		□ ■ ■ ■ □
		□ ■ ■ ■ □
		□ □ □ □ □

		dice = 1
		□ □ □ □ □
		□ ■ ■ ■ □
		□ ■ ■ ■ 옷
		□ ■ ■ ■ □
		□ □ □ □ □

		dice = 4
		□ □ □ □ □
		□ ■ ■ ■ □
		□ ■ ■ ■ □
		□ ■ ■ ■ □
		□ □ 옷 □ □

		dice = 4
		□ □ □ □ □
		□ ■ ■ ■ □
		옷 ■ ■ ■ □
		□ ■ ■ ■ □
		□ □ □ □ □

		dice = 4
		□ □ 옷 □ □
		□ ■ ■ ■ □
		□ ■ ■ ■ □
		□ ■ ■ ■ □
		□ □ □ □ □

'''
'''
움직일 수 있는 공간 : 00 01 02 03 04 
					10			 14
					20			 24
					30			 34
					40 41 42 43 44 
'''
import random

block = [ 
	[0,  1,  2,  3,  4],
	[15, 99, 99, 99, 5],
	[14, 99, 99, 99, 6],
	[13, 99, 99, 99, 7],
	[12, 11, 10,  9, 8]
]

# 0113
turn = 0
position = 0
while True :
	for i in range(len(block)) :
		for j in range(len(block)) :
			if block[i][j] == position :
				print("옷", end = " ")
			elif block[i][j] == 99 :
				print("■", end = " ")
			elif block[i][j] != 99 and block[i][j] != position :
				print("□", end = " ")
		print()
	print()

	if turn >= 2 : 
		break

	dice = random.randint(1,6)
	position += dice

	if position > 15 :
		position %= 16
		turn += 1

	print("dice : ", dice, "position : ", position,"turn : ", turn)
		
# # 2차
# y = 0
# x = 0
# position = 0
# turn = 0 

# while True :
	

# 	for i in range(len(block)) :
# 		for j in range(len(block[i])) :
# 			if i == y and j == x : 
# 				print("옷", end = " ")
				
# 			elif block[i][j] == 99 :
# 				print("■", end = " ")
			
# 			else :
# 				print("□", end = " ")
# 		print()
# 	print()
	
# 	if turn == 2 :
# 		print("게임종료")
# 		break 

# 	dice = random.randint(1,6)
# 	print("dice : ", dice)

# 	position += dice
	
# 	if position > 15 :
# 		turn += 1
# 		position %= 16
	
# 	for i in range(len(block)) :
# 		for j in range(len(block[i])) :
# 			if block[i][j] == position :
# 				y = i
# 				x = j
# 				break
# 	print("turn : ", turn, "position : ", position)
	
# for i in range(len(block)) :
# 	for j in range(len(block[i])) :
# 		if i == y and j == x : 
# 			print("옷", end = " ")
			
# 		elif block[i][j] == 99 :
# 			print("■", end = " ")
		
# 		else :
# 			print("□", end = " ")
# 	print()
# print()



