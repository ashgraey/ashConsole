'''
    [문제]
        lotto리스트가 당첨인지 꽝인지 체크하는 함수를 만드시오.
        단, 7이 연속으로 3개이면 당첨이다.
    [정답]
        당첨
'''

def checkLotto(lotto):
    check = False
    count = 0
    for i in range(len(lotto)):
        if lotto[i] == 7:
            count += 1
        else:
            count = 0
        if count == 3:
            check = True
    if check == True:
        print("당첨!")
    else:
        print("꽝!")

lotto = [1, 7, 7, 1, 7, 7, 7]
checkLotto(lotto)