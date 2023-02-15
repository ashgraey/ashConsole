"""
	[Up & Down 게임]
		1. com 은 랜덤으로 1~100사이를 저장한다.
		2. me 는 1~100사이를 입력한다. 	 
		3. com 과 me 를 비교해서 com 크면 "크다" , com 이작으면 "작다" 힌트제공 
		4. 정답을 맞출때까지 반복한다. 
"""

import random

com = random.randint(1, 100)
print(com)

hint = ""
while True:
    print("1 ~ 100사이를 입력해주세요 : ", end="")
    me = int(input())

    if com == me:
        print(com, " == ", me, ": 게임종료")
        break
    elif com > me:
        hint = "UP"
    elif com < me:
        hint = "DOWN"
    print(hint)
