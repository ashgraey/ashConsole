"""
    [문제]
        Up & Down 게임
        1. com은 8이다.
        2. me는 com의 숫자를 맞추는 게임이다.
        3. 다음과 같은 메세지를 출력한다.
            1) me < com   : Up!
            2) me == com  : Bingo!
            3) me > com   : Down!
"""
com = 8
me = int(input("숫자를 입력하세요 : "))
if me < com:
    print("Up!")
if me == com:
    print("Bingo!")
if me > com:
    print("Down!")