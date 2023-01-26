'''
    [랜덤복권]
        철수는 복권을 제작하고있다. 
        복권은 1또는 7이 랜덤으로 총 7개 저장되어있다. 
        1은 4개 7은 3개 저장되어있다. 
        복권은 7이 연속으로 3개이면 당첨이다.
        복권제작 프로그램을 함수를 사용해서 만들어보시오.
'''
import random
def setLotto():
    while True:
        a = []
        count7 = 0
        count1 = 0
        for i in range(7):
            r = random.randint(0,1)
            if r == 0:
                a.append(7)
                count7 += 1
            if r == 1:
                a.append(1)
                count1 += 1
        # print(count7 , " " , count1)
        if count7 == 3 and count1 == 4:
            return a

def checkLotto(a):
    count = 0
    win = False
    for i in range(len(a)):
        if a[i] == 7:
            count += 1

        else:
            count = 0
        if count == 3:
            win = True
    if win == True:
        print("당첨")
    else:
        print("꽝")

a = setLotto()
print(a)
checkLotto(a)

