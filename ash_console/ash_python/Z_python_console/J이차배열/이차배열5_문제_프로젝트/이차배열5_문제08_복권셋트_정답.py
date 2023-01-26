'''
	[문제]
		복권 1개당 7칸으로, 총 5개의 복권을 제작하려 한다.
		복권 1줄은 1 또는 7의 랜덤 숫자로 구성되어 있다.
		7이 연속으로 3개 이상이면 "당첨"이고, 그 미만은 "꽝"이다.
		5개 중에 딱 1개만 당첨 복권이고 나머지 4개는 꽝인 복권을
		랜덤으로 생성해서 출력하시오.
		
		예)
			1177117 (꽝)
			1117771 (당첨)
			7171117 (꽝)
			7711771 (꽝)
			7171717 (꽝)
'''
import random

lotto = [0, 0, 0, 0, 0]

doubleCheck = False
i = 0
while i < 5:
    temp = [0, 0, 0, 0, 0, 0, 0]

    check = False
    count = 0
    j = 0
    while j < 7:
        r = random.randint(0, 1)
        if r == 0:
            temp[j] = 7
            count += 1
        else:
            temp[j] = 1
            count = 0
        
        if count >= 3:
            check = True
        j += 1
    lotto[i] = temp

    # 당첨 복권이 안나오면
    if doubleCheck == False and check == False:
        i -= 1
    # 당첨 복권이 두 번 나왔으면
    elif doubleCheck == True and check == True:
        i -= 1
    # 당첨 복권이 나오면
    elif doubleCheck == False and check == True:
        doubleCheck = True

    i += 1

# 셔플
for i in range(10):
    r = random.randint(0, 4)

    temp = lotto[0]
    lotto[0] = lotto[r]
    lotto[r] = temp

# 출력
for i in range(len(lotto)):
    check = False
    count = 0
    for j in range(len(lotto[i])):
        if lotto[i][j] == 7:
            count += 1
        else:
            count = 0
        
        if count >= 3:
            check = True
        print(lotto[i][j], end="")
    if check:
        print(" (당첨)")
    else:
        print(" (꽝)")