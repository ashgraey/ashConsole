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
# 0118

# 숫자 5개, 랜덤없이 리스트에 저장
for i in range(5) :
	num = []
	while True :
		
		r = random.randint(1, 9) 
		ck = False 
		
		k = 0
		while k < len(num) :
			if num[k] == r : 
				ck = True 
				break
			k += 1 
		
		if ck == False : 
			num.append(r)
		
		if len(num) == 5 : 
			break
		
	numList.append(num)

# 자릿수
div = 1
for i in range(len(numList[0]) - 1) :
	div *= 10

print(div)

# 자릿수로 합산
numTot = []
for i in range(len(numList)) :
	tempDiv = div
	tot = 0
	for j in range(len(numList[i])) :
		temp = numList[i][j]
		temp *= tempDiv
		tot += temp
		tempDiv //= 10

	numTot.append(tot)

print(numTot) 

# 출력
total = 0 
for i in range(len(numTot)) :
	total += numTot[i]

	if i == len(numTot) - 1 :
		print(numTot[i], end = " = ") 
	else :
		print(numTot[i], end = " + ")
print(total)



print()
for i in range(len(numList)) :
	print(numList[i])

# 2차
# 중복 없이 저장
# num = []
# i = 0
# while i < 5 :
# 	r = random.randint(1, 9)
# 	ck = False
# 	j = 0
# 	while j < i :
# 		if r == num[j] :
# 			ck = True
# 			break
# 		j += 1  
	
# 	if ck == False :
# 		num.append(r)
# 		i += 1 

# tempList = [0, 0, 0, 0, 0]
# while True :
# 	# 셔플 
# 	for i in range(100) :
# 		r = random.randint(0, len(num) - 1)
# 		temp = num[0]
# 		num[0] = num[r]
# 		num[r] = temp

# 	cnt = 0 
# 	ck = False
# 	for i in range(5) :
# 		if num[i] == tempList[i] :
# 			cnt += 1 

# 		if cnt == 5 :
# 			ck = True
# 			break	


# 	if ck == True :
# 		continue
# 	else :
# 		tempList = []
# 		tempList.append(num)
# 		numList.append(tempList)

# 	if len(numList) == 5 :

# 		break
# print(numList)
		
# 1차
# for i in range(4) :
# 	numList.append([0, 0, 0, 0, 0])

# # 중복되지않는 수 5개를 number 배열에 담는다
# number = []

# count = 0
# while True :
# 	check = False
# 	r = random.randint(1, 9)
# 	# print("r : ", r)

# 	for i in range(len(number)) :
# 		if(number[i] == r) :
# 			check = True
# 			break
	
# 	if check == False :
# 		number.append(r)
# 		count += 1
	
# 	if count == 5 :
# 		break

# # 
# print(number)
# # print(numList)

# # 셔플 중복 검사
# for i in range(4) :
# 	# numList.append(number)
# 	for j in range(100) :
# 		r = random.randint(0, len(number) - 1) 
# 		temp = number[0]
# 		number[0] = number[r]
# 		number[r] = temp
# 		# print(number)

# 		cnt = 0 
# 		for k in range(len(number)) :
# 			if numList[i][k] == number[k] :
# 				cnt += 1 

# 			if cnt == 5 :
# 				break
# 			else :
# 				numList[i][k] = number[k]


# # print(numList)
# print()
# for i in range(len(numList)) :
# 	print(numList[i])

# # 자릿수 찾기
# unit = 10
# for i in range(len(numList) - 1) :
# 	unit *= 10
# # print(unit) 

# # 자릿수만큼의 자리로 만들고 더하기
# for i in range(len(numList)) :
# 	tot = 0
# 	temp = unit
# 	for j in range(len(numList[i])) :
# 		pls = temp * numList[i][j]
# 		tot += pls
# 		temp //= 10
# 	numList[i] = tot

# # 총합을 구해서 numList의 마지막 index에 추가하기
# tot = 0 
# for i in range(len(numList)) :
# 	tot += numList[i]
# numList.append(tot)
# 	# print(numList[i])

# for i in range(len(numList)) :
# 	if i < len(numList) - 1 :
# 		print(i + 1, ":", numList[i])
# 	else :
# 		print("tot : ", numList[i]) 
