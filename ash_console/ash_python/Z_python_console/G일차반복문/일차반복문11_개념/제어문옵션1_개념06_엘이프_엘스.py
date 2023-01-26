'''
    [elif 와 else]
        if에 추 가조건을 사용하기 위해 elif를 사용한경우 else 또한 사용가능하다. 
        단, else는 문맥상 가장 마지막에만 사용할 수 있다.
        다음 가위바위보 식을 보면 기존식에선 조건이 7개 이었는데 
        조건을5개로 줄인걸 확인할 수 있다.
'''
'''
    [가위(0) 바위(1) 보(2) 게임]
        [1] com 은 0~2 사이의 숫자를 랜덤 저장한다. 
        [2] me 는 0~2 사이의 숫자를 랜덤 저장한다. 
        [3] 가위,바위,보를 0,1,2 숫자로 대신 표현한다.
        [4] com 과 me를 비교해서 "비김" "승리" "패배" 를 출력한다.
'''
import random

com = random.randint(0, 2)
me = random.randint(0, 2)

if me == com :
    print("비겼다.")
elif me == 0 and com == 2:
    print("내가 이겼다.")
elif me == 1 and com == 0:
    print("내가 이겼다.")
elif me == 2 and com == 1:
    print("내가 이겼다.")
else:
    print("내가 졌다.")
    
# 위와같이 조건식이 길어진 경우 elif 와 else 를 활용하면 식을 효과적으로 줄일 수 있다.   

