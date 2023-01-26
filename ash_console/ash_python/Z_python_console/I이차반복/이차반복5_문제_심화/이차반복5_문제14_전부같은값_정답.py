'''
	[문제]
		a리스트와 b리스트의 값들이 각각 값과 개수가 똑같은지 확인한다.
		똑같으면 "같음", 아니면 "다름"을 출력하시오.
		위치는 상관없이 각각의 숫자의 개수가 일치하면 "같음"이다. 
	[정답]
'''
a = [10, 20, 30, 10, 20, 30]
b = [30, 20, 10, 20, 30, 10]

temp = []
i = 0
while i < len(a):
	check = False
	j = 0
	while j < i:
		if a[i] == temp[j]:
			check = True
			break
		j += 1
	
	if check == False:
		temp.append(a[i])
	
	i += 1
print(temp)

check = False
for i in range(len(temp)):

	cnt1 = 0
	for j in range(len(a)):
		if temp[i] == a[j]:
			cnt1 += 1
	
	cnt2 = 0
	for j in range(len(b)):
		if temp[i] == b[j]:
			cnt2 += 1
		
	print(cnt1, cnt2)
	if cnt1 == cnt2:
		check = True
	else:
		check = False

if check:
	print("같음")
else:
	print("다름")