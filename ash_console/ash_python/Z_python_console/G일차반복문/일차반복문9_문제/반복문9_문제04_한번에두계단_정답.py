'''
	[문제]
		계단이 50 계단이 있다. 철수는 제일 위 계단에 서 있다. 
		철수는 한 번에 두 계단씩 내려간다. 
		철수가 왼발로 디딘 계단을 출력하시오.
		아래 조건을 참고하시오.
		[1] 철수는 한 번에 두 계단씩 내려간다.
		[2] 철수는 왼발부터 내려간다.
		[3] 5번 출력할 때마다 다른 발을 출력하시오.
		
		48 44 40 36 32 
		30 26 22 18 14
		12 8  4   0
'''

철수위치 = 50

count = 0
turn = True
while 철수위치 > 0:

    # 왼발
    철수위치 = 철수위치 - 2
    if turn == True:
        print("(좌)",철수위치, end=" ")
        count += 1

        if count % 5 == 0:
            print()
            count = 0
            turn = not turn
            print(turn)
    # 오른발
    철수위치 = 철수위치 - 2
    if turn == False:
        print("(우)",철수위치, end=" ")
        count += 1

        if count % 5 == 0:
            print()
            count = 0
            turn = not turn
            print(turn)
    
    
    
    

    