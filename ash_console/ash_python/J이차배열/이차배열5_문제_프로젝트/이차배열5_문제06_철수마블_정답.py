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
import random

game = [
    [ 0,  1,  2,  3, 4],
    [15, 99, 99, 99, 5],
    [14, 99, 99, 99, 6],
    [13, 99, 99, 99, 7],
    [12, 11, 10,  9, 8]
]

pY = 0
pX = 0
position = 1

count = 0

while True:

	for i in range(len(game)):
		for j in range(len(game[i])):
			if i == pY and j == pX:
				print("옷", end=" ")
			elif game[i][j] == 99:
				print("■", end=" ")
			else:
				print("□", end=" ")
		print()
	print()

	if count == 2:
		break
	

	dice = random.randint(1, 6)
	print("dice =", dice)

	position += dice
	if position > 15:
		count += 1
	position %= 16

	for i in range(len(game)):
		for j in range(len(game[i])):
			if game[i][j] == position:
				pY = i
				pX = j
				break
	

