"""
[문제]
    [내마음대로 주사위게임]
        내마음대로 주사위게임 은 a와 b가 주사위를 두개를 던진다.
        두개의 주사위중 하나를 랜덤으로 선택해서 제시한다.

        아래의 특별한 게임규칙에 따라 승패가 갈린다. 
       
        a는 주사위를 2개 던진다.
        b는 주사위를 2개 던진다.

        a와 b는 두 주사위중 하나를 랜덤 선택해서 제출한다. 

        <게임규칙>
            [1] 숫자가 둘다 짝수이면 둘중 큰수가 승리 , 숫자가 같으면 비김
            [2] 숫자가 둘다 홀수이면 둘중 작은수가 승리 , 숫자가 같으면 비김
            [3] 하나는 짝수이고 하나는 홀수이면 
                주사위 숫자와 상관없이 비긴다. 

    a 와 b는 위 게임을 무한으로 반복한다. 
    둘중 한명이 연속으로 3번 승리하면 게임 종료. 
    과정을 전부 출력한다. 
"""
import random

a_count = 0 
b_count = 0 
while True :
    a1 = random.randint(1, 6)
    a2 = random.randint(1, 6)
    b1 = random.randint(1, 6)
    b2 = random.randint(1, 6)
    print("a =",a1, a2)
    print("b = ",b1, b2)

    a_ch = random.randint(0, 1) 
    b_ch = random.randint(0, 1)

    if a_ch == 0 : 
        a_ch = a1 
    else : 
        a_ch = a2

    if b_ch == 0 : 
        b_ch = b1 
    else : 
        b_ch = b2

    if a_ch % 2 == 0 and b_ch % 2 == 0 :
        if a_ch > b_ch :
            print("a의 승리")
            a_count += 1 
            b_count = 0
        else :
            print("b의 승리")
            b_count += 1 
            a_count = 0

    if a_ch % 2 == 1 and b_ch % 2 == 1 :
        if a_ch > b_ch :
            print("b의 승리")
            b_count += 1
            a_count = 0  
        else :
            print("a의 승리")
            a_count += 1 
            b_count = 0

    if (a_ch % 2 == 0 and b_ch % 2 == 1) or (a_ch % 2 == 1 and b_ch % 2 == 0) :
        print("무승부")
    
    if a_count == 3 :
        print("a의 승리 게임종료")
        break
    elif b_count == 3 :
        print("b의 승리 게임종료")
        break
    

