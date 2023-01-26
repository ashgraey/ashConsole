'''
	[문제]
		철수의 위치는 y = 0 , x = 0 이다.
		랜덤 숫자(1~4) 를 5번 뽑는다. 
		랜덤 숫자는 방향을 뜻한다. 
		1은 북쪽 2는 동쪽 3은 남쪽 4는 서쪽을 뜻한다.
  
		방향만큼 1씩 이동하며, 
		5번 이동 후 철수의 위치를 출력하시오.
  
		[예시] 랜덤으로 1 4 3 2 1 이 나왔다고 했을 때
		1은 북이므로 y += 1
		4는 서이므로 x -= 1
		3은 남이므로 y -= 1
		2는 동이므로 x += 1
		1은 북이므로 y += 1
'''
import random
# [2차 - 1110]
# x = 0
# y = 0

# i = 0
# while i < 5 : 
# 	r = random.randint(1, 4)
# 	print(r, end = " ")

# 	if r == 1 :
# 		y += 1
# 	elif r == 2 :
# 		x += 1 
# 	elif r == 3 :
# 		y -= 1 
# 	else :
# 		x -= 1 

# 	i += 1 

# print()
# print("x =", x)
# print("y =", y)

# [1차]
# y = 0
# x = 0

# # 북 = 1 
# # 동 = 2
# # 남 = 3
# # 서 = 4 
# # total = 0
# i = 0 
# while i < 5 :
# 	r = random.randint(1, 4)
# 	# print(r, end =" ")

# 	if r == 1 : 
# 		print("북")
# 		y += 1 
# 	if r == 2 :
# 		print("동")
# 		x += 1 
# 	if r == 3 : 
# 		print("남")
# 		y -= 1
# 	if r == 4 :
# 		print("서")
# 		x -= 1
# 	i += 1 

# print(x, y)
