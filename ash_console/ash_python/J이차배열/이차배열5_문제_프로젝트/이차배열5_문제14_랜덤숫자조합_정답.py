'''
	[문제]
		철수는 게임을 만들려고 한다.
		숫자 다섯 개를 랜덤(1~9사이의 숫자)으로 저장한다.
		각각의 숫자는 중복이 되면 안된다.

		각각의 숫자로 랜덤 조합을 4가지 만들어서
		numList에 저장하고, 전체 합을 출력하시오.
		랜덤 조합 역시 중복이 되면 안된다.
		[예]
			1, 3, 5, 7, 9 라고 했을 때
			[1] 13597
			[2] 51397
			[3] 37951
			[4] 91537

			정답 : 13597 + 51397 + 37951 + 91537 = 194482
'''
import random

numList = []

i = 0
while i < 5:
	r = random.randint(1, 9)

	check = False
	j = 0
	while j < i:
		if r == numList[j]:
			check = True
			break
		j += 1
	
	if check == False:
		numList.append(r)
	else:
		i -= 1
	i += 1
print(numList)
print()

indexList = []
while True:
	for i in range(4):
		temp = [0, 0, 0, 0, 0]
		j = 0
		while j < 5:
			r = random.randint(0, 4)

			check = False
			k = 0
			while k < j:
				if r == temp[k]:
					check = True
					break
				k += 1
			
			if check == False:
				temp[j] = r
			else:
				j -= 1
			j += 1
		indexList.append(temp)
	
	check = False
	k = 0
	while k < len(indexList):
		for i in range(len(indexList)):
			if k == i:
				continue
			count = 0
			for j in range(len(indexList[i])):
				if indexList[k][j] == indexList[i][j]:
					count += 1
			if count == 5:
				check = True
				break
		k += 1

	if check == False:
		break
	else:
		indexList = []

for i in range(len(indexList)):
	print(indexList[i])
print()

totalList = []
for i in range(len(indexList)):
	print("[", (i+1), "]", end=" ")
	total = 0
	div = 10000
	for j in range(len(indexList[i])):
		print(numList[indexList[i][j]], end="")
		total += div * numList[indexList[i][j]]
		div //= 10
	print()
	totalList.append(total)
print(totalList)

total = 0
for i in range(len(totalList)):
	total += totalList[i]
print(total)
	



