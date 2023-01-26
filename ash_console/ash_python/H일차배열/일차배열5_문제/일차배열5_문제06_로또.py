'''
	[로또]	
		아래 lotto 리스트에 1~45숫자를 순차적으로 저장한다. 
		셔플후 그중 가장앞에서 6개를 출력한다. 
'''
import random

lotto = []
size = 45

for i in range(size) : 
	i += 1 
	lotto.append(i)
print(lotto)

temp = 0 

for i in range(10) :
	r1 = random.randint(0, size)
	r2 = random.randint(0, size)

	temp = lotto[r1]
	lotto[r1] = lotto[r2]
	lotto[r2] = temp
	print(r1, ",", r2, ":", lotto)
