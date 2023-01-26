'''
	[문제]		
		[1] com리스트에 0~9사이의 랜덤 숫자 3개를 저장하되 중복 값이 없어야 한다.
		[2] me리스트에 0~9사이의 랜덤 숫자 3개를 저장하되 중복 값이 없어야 한다.
		[3] com과 me 를 비교해서 숫자가 같고 자리도 같으면 strike + 1
		[4] com과 me 를 비교해서 숫자가 같고 자리가 틀리면 ball + 1
		[5] 사용자에게 strike와 ball 개수를 출력해 보여준다.
		
		계속 반복하면서 strike가 3이 되면 종료한다.
'''
import random

com = [0, 0, 0]
me = [0, 0, 0]

# 중복값 없이 랜덤 com저장
# com값은 한번만 저장
i = 0
while i < 3:
	r = random.randint(0, 9)

	# 중복값 검사
	check = False
	j = 0
	while j < i:
		if r == com[j]:
			check = True
		j += 1
	
	# check값이 변함이 없는것이 중복이 없는것
	# com 인덱스 안에 r저장
	if check == False:
		com[i] = r
		i += 1
	
print("com =", com)


# me값은 strike가 3이 될때까지 계속 바뀐다.
while True:
	i = 0
	# me에 중복없는 값을 저장
	while i < 3:
		r = random.randint(0, 9)

		check = False
		j = 0
		while j < i:
			if r == me[j]:
				check = True
			j += 1
		
		if check == False:
			me[i] = r
			i += 1
	print("me =", me)

	ball = 0
	strike = 0

	# strike와 ball 검사
	for i in range(3):
		for j in range(3):
			if com[i] == me[j]:
				if i == j:
					strike += 1
				else:
					ball += 1
	print("ball =", ball)
	print("strike =", strike)

	if strike == 3:
		print("com =", com)
		break