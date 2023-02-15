"""
	[홀짝게임]		  
		[1] 1~10사이의 숫자를 랜덤으로 저장한다.
		[2] 문자로 입력을 "홀" 또는 "짝" 을 입력한다. 
		[3] 홀짝을 맞추는게임이다. 
		[4] 기본금은 3000원을 가지고시작한다. 정답을 맞추면 700원 이득을 보고,틀리면 1000원 손해를 본다.
		[5] 매게임이 끝날때마다 새로운메뉴 [1.한번더][2.종료] 를 보여준다.   
		[6] 게임종료후 남은자금을 출력하시오.
		[7] 돈이 부족하면 게임은 자동종료된다. 
 
"""
import random

money = 3000
turn = 1
while money > 0:
    print("=========", turn, "=========")
    r = random.randint(1, 10)
    print(r)
    a = input()

    if r % 2 == 0:
        result = "짝"
    else:
        result = "홀"

    if a == result:
        money += 700
    else:
        money -= 1000
        if money <= 0:
            break

    print("money : ", money)
    print("[1.한번더][2.종료]")
    b = int(input())
    if b == 2:
        break

    turn += 1

print("잔돈 : ", money)
