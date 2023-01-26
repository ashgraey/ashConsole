'''
	[문제]
		a리스트의 각 값의 약수들을 전부 출력하고 
		각 약수의 개수를 count리스트에 추가한다.

		개수가 가장 많은 약수를 max리스트에 추가한다. 
		개수가 가장 많은 약수가 여러 개일 땐 전부 추가한다. 
	[예시]
		1 43 
		1 5 11 55 
		1 5 13 65 
		1 11 		
		count = [2, 4, 4, 2]
		max = [55, 65]
	[정답]
		max = [55, 65]
'''
a = [43,55,65,11]
count = []
max = []

for i in range(len(a)):
	
	cnt = 0
	for j in range(a[i]):
		if a[i] % (j + 1) == 0:
			print(j + 1, end=" ")
			cnt += 1
	count.append(cnt)
print()

print("count =", count)

maxCount = 0
maxIndex = 0
for i in range(len(count)):
	if maxCount < count[i]:
		maxCount = count[i]
		maxIndex = i
print(maxCount)

for i in range(len(count)):
	if maxCount == count[i]:
		max.append(a[i])
print(max)