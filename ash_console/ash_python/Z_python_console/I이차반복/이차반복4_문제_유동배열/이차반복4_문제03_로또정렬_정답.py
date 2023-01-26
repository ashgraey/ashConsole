'''
	[문제] 
		1~45사이의 랜덤값 6개를 lotto에 저장하려 한다.
		단, 중복되는 숫자는 없어야 하며,
		내림차순 정렬 후 출력하시오.
	[예시]
        [40, 38, 27, 26, 18, 5]
'''
import random

lotto = []

i = 0
while i < 6:
	r = random.randint(1, 45)

	check = False

	j = 0
	while j < i:
		if r == lotto[j]:
			check = True
			break
		j += 1
	
	if check == False:
		lotto.append(r)
		i += 1
	
i = 0
while i < len(lotto):

    max = lotto[i]
    maxIndex = i

    j = i
    while j < len(lotto):
        if max < lotto[j]:
            max = lotto[j]
            maxIndex = j
        j += 1
    
    temp = lotto[i]
    lotto[i] = lotto[maxIndex]
    lotto[maxIndex] = temp

    i += 1

print(lotto)



