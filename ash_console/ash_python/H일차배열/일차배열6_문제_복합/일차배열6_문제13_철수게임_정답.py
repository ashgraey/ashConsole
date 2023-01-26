'''
	[문제]
		철수는 철수의 마블 게임을 개발 중이다. 
		map1과 map2는 게임 스테이지를 표현한다. 
		숫자 1은 철수의 위치이다. 
		주사위는 1~6까지 있고 주사위 2개를 던저서 그 합만큼 앞으로 이동한다. 		
		map1의 끝에 도달하면 map2로 이동해서 전진하고, 
		map2의 끝에 도달하면 다시 map1로 이동해서 전진한다. 		
		주사위를 총 4번 반복하고 철수의 위치를 출력하시오.
	[예시]
	(1)	시작
		map1 = [1,0,0,0,0,0,0,0,0,0]
		map2 = [0,0,0,0,0,0,0,0,0,0]
  
	(2)	주사위 3 , 5 : 8
		map1 = [0,0,0,0,0,0,0,0,1,0]
		map2 = [0,0,0,0,0,0,0,0,0,0]
		
	(3)	주사위 2 , 1 : 3
		map1 = [0,0,0,0,0,0,0,0,0,0]
		map2 = [0,1,0,0,0,0,0,0,0,0]
		
	(4)	주사위 6 , 1 : 7
		map1 = [0,0,0,0,0,0,0,0,0,0]
		map2 = [0,0,0,0,0,0,0,0,1,0]
		
	(5)	주사위 3 , 3 : 6
		map1 = [0,0,0,0,1,0,0,0,0,0]
		map2 = [0,0,0,0,0,0,0,0,0,0]
			
'''
import random

map1 = [1,0,0,0,0,0,0,0,0,0]
map2 = [0,0,0,0,0,0,0,0,0,0]

position = 0
turn = True
size = len(map1)
# print(size)

for i in range(4):
	dice1 = random.randint(1, 6)
	dice2 = random.randint(1, 6)
	total = dice1 + dice2
	print("주사위", dice1, dice2, "=", total)

	# position 0부터 시작
	if turn:
		map1[position] = 0
	else:
		map2[position] = 0
	print("position =", position)

	# 위치값 + 주사위합이 map의 길이보다 크면 turn 변수 값 전환
	if position + total >= size:
		turn = not turn

	# turn True : map1 list position으로 이동
	if turn:
		position += total
		# 일 단위로 변환
		position %= size
		map1[position] = 1
	
	# turn False : map2 list position으로 이동
	else:
		position += total
		position %= size
		map2[position] = 1	
	
	print("map1 =", map1, turn)
	print("map2 =", map2, turn)
	print()
	