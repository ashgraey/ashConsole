"""	
	[베스킨라빈스31]
		베스킨라빈스 게임이란, 플레이어 2명이 번갈아가면서
		1~3사이의 숫자를 선택할수있고, 그숫자들을 계속 더해서 
		그누적합이 31에 먼저도달한쪽이 지는게임이다.
	 
	[조건]
		1) 각 플레이어는 번갈아가면서 1~3을 선택한다.
		2) 만약에 이상한숫자를 입력하면 1~3을 입력할때까지 계속본인 차례이다.
		3) 각 플레이어가 선택한숫자는  total  변수에 계속 누적해서 더한다.
		4) total 이 31이상에 도달하면 승리자를 출력한다.
"""

total = 0
while True:

    p1 = int(input())
    if 1 < p1 and p1 > 3:
        print("p1 : ")
        continue

    p2 = int(input())
    if 1 < p2 and p2 > 3:
        print("p2 : ")
        continue

    total += p1
    if total >= 31:
        print("p2 승")
        break

    total += p2
    if total >= 31:
        print("p1 승")
        break

    print(total)
