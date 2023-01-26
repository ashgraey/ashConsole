'''
[문제]
	랜덤으로 1 또는 7을 10번 출력한다. 
	7이 연속으로 3번 이상이면 "당첨" 아니면 "꽝"을 출력하시오.
[예시]
	1 1 1 7 7 7 1 1 7 7 
	당첨

	7 1 1 1 1 7 1 1 7 1 
	꽝
'''

import random

count = 0

result = False

# 1 1 1 7 7 7 1 1 7 7 
i = 0
while i < 10:
	r = random.randint(1, 2)
	if r == 2:
		r = 7
	print(r, end=" ")

	if r == 7:
		count += 1
	if r != 7:
		count = 0
	
	if count == 3:
		result = True

	i += 1

if result == True:
	print("당첨")
if result == False:
	print("꽝")
