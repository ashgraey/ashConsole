'''
[가위(0) 바위(1) 보(2) 게임]
	[1] com은 0~2 사이의 숫자를 랜덤 저장한다. 
	[2] me는  0~2 사이의 숫자를 랜덤 저장한다. 
	[3] 가위, 바위, 보를 0, 1, 2 숫자로 대신 표현한다.
	[4] com과 me를 비교해서 me를 기준으로 "비김" "승리" "패배"를 출력하시오.
'''

'''
	# 내가 이겼다.
	me 		vs		com
	가위(0)			보(2)
	바위(1)			가위(0)
	보(2)			바위(1)
'''

import random

me = random.randint(0, 2)
com = random.randint(0, 2)

print(me, " ", com)

if me == com:
	print("비겼다.")

if me == 0 and com == 2:
	print("이겼다.")
if me == 1 and com == 0:
	print("이겼다.")
if me == 2 and com == 1:
	print("이겼다.")

if me == 2 and com == 0:
	print("졌다.")
if me == 0 and com == 1:
	print("졌다.")
if me == 1 and com == 2:
	print("졌다.")

