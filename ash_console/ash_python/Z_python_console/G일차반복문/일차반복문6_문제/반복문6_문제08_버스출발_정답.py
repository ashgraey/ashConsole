'''
	[문제]
	  	어느 시외버스 터미널에서 대전행버스는 10분 간격으로 출발,
	  	광주행버스는 15분 간격으로 출발,
	  	부산행버스는 18분 간격으로 출발한다고 했을 때,	
	  	오전 8시에 처음 동시에 출발하고, 
		그 이후 처음으로 동시에 출발하는 시각을 구하시오. 
	[정답]
		9시 30분
'''

대전 = 10
광주 = 15
부산 = 18

시간 = 8 * 60

i = 1

run = 1
while run == 1:
    if i % 대전 == 0 and i % 광주 == 0 and i % 부산 == 0:
        시간 = 시간 + i
        run = 0
    i += 1

시 = 시간 // 60
분 = 시간 % 60
print(시, 분)
