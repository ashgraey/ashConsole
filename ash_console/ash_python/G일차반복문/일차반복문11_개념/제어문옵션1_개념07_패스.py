'''
    [제어문 옵션 pass]
        if문을 작성할 때 형태를 미리 만들어 놓기 위해 조건식만 적어놓고 내용은 천천히 적고싶을 때
        pass 옵션을 사용하면 식을 작성하기 쉽다.
        아래 가위바위보 게임을 보면 미리 조건식을 다 적어놓고 
        빈자리는 pass로 채워넣고 천천히 하나씩
        식을 채워서 코딩할 수도 있다. 
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
    pass 
elif me == 1 and com == 0:
    pass
elif me == 2 and com == 1:
    pass
else:
    pass
 

