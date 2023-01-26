'''
	[문제]
		랜덤으로 (1~4)를 저장하고
		아래와 같은 경우로 리스트에 저장하시오.
	[예]
		[1 번 선택시] 
		123
		654
		789
		
		[2 번 선택시]
		761
		852
		943
		
		[3번 선택시]		
		987
		456
		321
		
		[4번 선택시]	
		349
		258
		167
'''
import random

snake = []

r = random.randint(1, 4)
r = 4
print("r =", r)

for i in range(3):
	snake.append([0, 0, 0])

if r == 1:
	turn = True
	num = 1
	for i in range(3):
		for j in range(3):
			if turn == True:
				snake[i][j] = num
			elif turn == False:
				snake[i][2-j] = num
			num += 1
		turn = not turn
elif r == 2:

	turn = True
	num = 1
	for i in range(3):
		for j in range(3):
			if turn == True:
				snake[j][2 - i] = num
			elif turn == False:
				snake[2 - j][2 - i] = num
			num += 1
		turn = not turn
elif r == 3:
	num = 1
	turn = True
	for i in range(3):
		for j in range(3):
			if turn == True:
				snake[2 - i][2 - j] = num
			elif turn == False:
				snake[2 - i][j] = num
			num += 1
		turn = not turn
elif r == 4:
	num = 1
	turn = True
	for i in range(3):
		for j in range(3):
			if turn == True:
				snake[2 - j][i] = num
			elif turn == False:
				snake[j][i] = num
			num += 1
		turn = not turn

for i in range(len(snake)):
	print(snake[i])
