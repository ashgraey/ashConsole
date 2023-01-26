'''
	[문제]
		철수는 게임을 개발하고 있다.
		game리스트를 아래와 같이 사각형으로 출력한다.

		숫자8 은 현재 플레이어가 있는 자리이다.
		숫자0 은 플레이어가 이동할 수 있는 자리이다.
		숫자1 은 플레이어가 이동할 수 없는 벽이다.

		order리스트는 플레이어를 움직이기 위한 명령어들이다.
		숫자 1~4로 표현하고 북(1)동(2)남(3)서(4)를 뜻한다.

		order의 내용대로 플레이어가 이동하는 경로를 전부 출력하시오.
		벽 때문에 이동할 수 없을 때는 "이동 불가"를 출력하시오.
'''
game = [1,1,1,1,1,
	    1,0,0,0,1,
	    1,0,8,0,1,
	    1,0,0,0,1,
	    1,1,1,1,1]

order = [1,2,3,3,3,1,4,1]

# 1216
# review : 좌표값으로 생각하지못함 y,x으로 생각하여 풀어보자
# 숫자 0 : 이동할수 있는자리 idx : 6 7 8 / 11 12 13 / 16 17 18 
# 숫자 1 : 벽 idx : 0 1 2 3 4 5 9 10 14 15 19 20 21 22 23 24 25 
# print(game)
for i in range(len(game)) :
	print(game[i], end = " ")
	# print(i, end = " ")
	if i % 5 == 4 :
		print()

for i in range(len(game)) :
	if game[i] == 8 :
		position = i 
print("위치 : ", position)
# game[position] = 0

# 1 북, 2 동, 3 남, 4 서
for j in range(len(order)) :
	print()

	ck = False
	if order[j] == 1 :
		if 6 <= position - 5 <= 8 or 11 <= position - 5 <= 13 or 16 <= position - 5 <= 18 :
			game[position] = 0
			position -= 5
			game[position] = 8
			ck = True

	elif order[j] == 2 :
		if 6 <= position + 1  <= 8 or 11 <= position + 1 <= 13 or 16 <= position + 1 <= 18 :
			game[position] = 0
			position += 1
			game[position] = 8
			ck = True
	
	elif order[j] == 3 :
		if 6 <= position + 5 <= 8 or 11 <= position + 5 <= 13 or 16 <= position + 5 <= 18 :
			game[position] = 0
			position += 5
			game[position] = 8
			ck = True

	elif order[j] == 4 :
		if 6 <= position - 1 <= 8 or 11 <= position - 1 <= 13 or 16 <= position - 1 <= 18 :
			game[position] = 0
			position -= 1
			game[position] = 8
			ck = True


	if ck == True :
		for i in range(len(game)) :
			print(game[i], end = " ")
			if i % 5 == 4 :
				print()
	else :
		for i in range(len(game)) :
			print(game[i], end = " ")
			if i % 5 == 4 :
				print()
		print("이동불가")
		
	print("위치 : ", position, "order : ", order[j])

# 1차
# position
# for i in range(len(game)) :
# 	for j in range(len(game[i])) :
# 		if game[i][j] == 8 :
# 			tempY = i
# 			tempX = j
# 			position = game[i][j]

# print(tempX, tempY, position)












# 문제 이해가 잘 안됨
# 북(1), 동(2), 남(3), 서(4)
# 1125
# position = 0 
# for i in range(len(game)) :
# 	if game[i] == 8 :
# 		position = i 
# print(position)

# for i in range(len(order)) :
# 	if order[i] == 1 :
# 		position %= 5
# 	elif order[i] == 2 :
# 		position += 1
# 	elif order[i] == 3 :
# 		position += 5
# 	else :
# 		position -= 1
# print(position)

# for i in range(len(game)) :
# 	if i % 5 == 0 :
# 		print()
# 	print(game[i], end = "")

