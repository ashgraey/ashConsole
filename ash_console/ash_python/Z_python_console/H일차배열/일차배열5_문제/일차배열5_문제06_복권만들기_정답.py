'''
	[문제] 
		a리스트 안에 1 또는 7을 랜덤으로 7개 추가 후 출력하시오. 
		단, 7의 개수는 3개만 추가하고, 1의 개수는 4개만 추가한다.
		위에서 만든 복권을 판정한다. 
  		7이 연속으로 3개면 "당첨"을 출력한다.
		아니면 "꽝"을 출력한다.
		
	[예]
		[ 1, 7, 7, 1, 1, 7, 1]  "꽝"
		[ 1, 1, 1, 7, 7, 7, 1]  "당첨"
'''

import random

lotto = []

count1 = 0
count7 = 0

while True:
	if count1 + count7 == 7:
		break

	r = random.randint(0, 1)

	if r == 0 and count1 < 4:
		lotto.append(1)
		count1 += 1
	elif r == 1 and count7 < 3:
		lotto.append(7)
		count7 += 1
print(lotto)

check = False
count = 0
for i in range(7):
	if lotto[i] == 7:
		count += 1

		if count == 3:
			check = True
	else:
		count = 0

if check == True:
	print("당첨")
else:
	print("꽝")