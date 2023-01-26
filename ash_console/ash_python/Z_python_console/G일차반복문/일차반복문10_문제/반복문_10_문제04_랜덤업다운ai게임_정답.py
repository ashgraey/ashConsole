'''
    [문제]
        아래식은 랜덤 업다운 게임 식이다.
        com 이 랜덤으로 숫자를 저장하면 
        me가 com의 숫자를 맞출 때까지 반복하는 것이다.
        하지만 me는 그저 랜덤으로 아무 숫자나 막 뽑는다. 그 부분을 해결한다.
        예를 들어 com이 50이고 me가 30을 뽑았으면
        그 이후는 1~30 사이는 뽑지 않게 아래식을 수정하시오. 
        마찬지로 com이 50인데 me가 80을 뽑았다면 
        그 이후는 80~100은 뽑지 않게 바꾸면 된다. 
'''

import random

com = random.randint(1, 100)
print("com =", com)

start = 1
end = 100

run = 1
while run == 1:
    me = random.randint(start, end)
    
    if me < com:
        start = me + 1
        print(me, "Up!")
    if me > com:
        end = me - 1
        print(me, "Down!")

    if com == me:
        print(me, "정답!")
        run = 0
    