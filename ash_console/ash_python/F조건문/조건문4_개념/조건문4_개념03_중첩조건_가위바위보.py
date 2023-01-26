'''
[가위(0) 바위(1) 보(2) 게임]
    [1] com은 0~2 사이의 숫자를 랜덤 저장한다. 
    [2] me는  0~2 사이의 숫자를 랜덤 저장한다. 
    [3] 가위, 바위, 보를 0, 1, 2 숫자로 대신 표현한다.
    [4] com과 me를 비교해서 "비김" "승리" "패배" 를 출력하시오.
'''
import random

me = random.randint(0, 2)
com = random.randint(0, 2)

print(me , " " , com)

# 아래 내용은 직접 채워넣어보세요.
if me == com :
    print("비겼다.")

if me == 0:             # me     가위
    if com == 1:        # com    바위
        print("내가 졌다.")
    if com == 2:        # com    보
        print("내가 이겼다.")

if me == 1:             # me    바위
    if com == 0:        # com   가위
        print("내가 이겼다.")
    if com == 2:        # com   보
        print("내가 졌다.")

if me == 2:             # me    보
    if com == 0:        # com   가위
        print("내가 졌다.")
    if com == 1:        # com   바위
        print("내가 이겼다.")
