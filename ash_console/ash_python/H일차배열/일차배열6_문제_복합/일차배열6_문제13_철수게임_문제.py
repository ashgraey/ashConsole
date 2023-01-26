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
# print(len(map1))

# [1120]
# position = 0  
# total = 0 
# for i in range(4) :
# 	r1 = random.randint(1,6)
# 	r2 = random.randint(1,6)
# 	print(r1, r2)

# 	total = r1 + r2

# 	if total < len(map1) :
# 		if map1[i] == 1 :
# 			map1[i] = 0 
# 		else :
# 			map1[total] = 1
	
# 	elif total > len(map1) :
# 		position = total - len(map1)
# 		if map1[i] == 1 : 
# 			map1[i] = 0 
# 		else :
# 			map2[position] = 1 

# [1116 - 1차]
# position = 0
# total = 0
# for i in range(4) :
# 	dice1 = random.randint(1, 6)
# 	dice2 = random.randint(1, 6)
# 	print("dice1 =", dice1)
# 	print("dice2 =", dice2)

# 	position = dice1 + dice2
# 	print("position =", position)
# 	total += position  

# 	if len(map1) - 1 > total :
# 		map1[i] = 0 
# 		map1[position] = 1
# 	else :
# 		map1[i] = 0
# 		map2[total - len(map1)] = 1 

# [1차]
# position = 0
# turn = True
# size = len(map1)

# for i in range(4) :

# 	주사위1 = random.randint(1,6)
# 	주사위2 = random.randint(1,6)
# 	print("주사위1 =", 주사위1)
# 	print("주사위2 =", 주사위2)

# 	idx = 주사위1 + 주사위2

# 	if turn : 
# 		map1[position] = 0 
# 	else :
# 		map2[position] = 0 

# 	print("position =", position)
# 	if position + idx >= size :
# 		turn = not turn

# 	if turn :
# 		position += idx 
# 		position %= size 
# 		map1[position] = 1 
# 	else :
# 		position += idx
# 		position %= size
# 		map2[position] = 1
	
# 	print("map1 =", map1, turn)
# 	print("map1 =", map2, turn)