'''
[문제]
    com은 1~100 사이의 숫자를 한 개 저장한다.
    me는 com의 숫자를 모른다고 가정하고, 1~100 사이의 숫자를 제시한다.
    com과 me를 비교해서 "크다", "작다", "같다"를 출력하시오.

    com은 딱 한 번만 숫자를 정하고, 
    me는 com의 숫자를 맞출 때까지 계속 숫자를 랜덤으로 뽑는다. 
    숫자를 맞추면 게임은 종료된다.
'''
import random

com = random.randint(1, 100)
print("com =", com)

run = 1
while run == 1:
    me = random.randint(1, 100)
    
    if com < me:
        print(me, "크다")
    if com > me:
        print(me, "작다")
    if com == me:
        print(me, "같다")
        run = 0


