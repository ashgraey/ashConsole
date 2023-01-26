'''
	[문제] 
		a리스트 안에 1 또는 7을 랜덤으로 7개 추가 후 출력하시오. 
		단, 7의 개수는 3개만 추가하고, 
		1의 개수는 4개만 추가한다.
		
	[예]
		정답 [ 1, 7, 7, 1, 1, 7, 1]  # 개수가 맞다. 
		오답 [ 7, 1, 1, 7, 1, 1, 1]  # 7이 두개이다.
			
'''
# [문제] 
# a리스트 안에 1 또는 7을 랜덤으로 7개 추가 후 출력하시오. 
# 단, 7의 개수는 3개만 추가하고, 
# 1의 개수는 4개만 추가한다.
		
import random

[1115]
a = []
count1 = 0
count7 = 0

while True :
	if count1 + count7 == 7:
		break
	
	r = random.randint(1,2)

	if r == 1 and count1 < 5 :
		count1 += 1 
		a.append(1)
	elif r == 2 and count7 < 4 :
		count7 += 1 
		a.append(7)

print(a) 

# count1 = 0
# count7 = 0

# while True:
# 	# 무한반복을 종료시키는 조건
# 	if count1 + count7 == 7:
# 		break

# 	r = random.randint(0, 1)

# 	# 랜덤의 값이 0이고 count7의 값이 3이하일때 
# 	# a 리스트에 7을 추가하고 count7의 변수에 1을 증가시킨다.
# 	# count7값이 3이 초과되면 조건을 실행하지 않는다.
# 	# 7을 추가하는 조건
# 	if r == 0 and count7 <= 3:
# 		a.append(7)
# 		count7 += 1
# 	# 1을 추가하는 조건
# 	elif r == 1 and count1 <= 4:
# 		a.append(1)
# 		count1 += 1
# print(a)


    
