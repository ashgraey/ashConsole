'''
	[문제]
		a리스트에 -100~100 사이의 랜덤 값 중 홀수만 5개 저장한다. 
		그중 가장 큰 수와 가장 작은 수를 출력하시오. 
		[예시]
			[37, 53, 90, -82, -17]
			90
			-82
'''

import random

a = []

max = 0
min = 100
size = 0 

[1115]
while True :
	r = random.randint(-100, 100)

	if r % 2 == 1 :
		a.append(r)
		size += 1

	if size == 5 :
		break

for i in range(len(a)) :
	if max < a[i] :
		max = a[i]
	if min > a[i] :
		min = a[i] 

print(a)
print("max =", max, "min =", min)


# [2차]
# 조건1 : a리스트에 -100, 100사이의 랜덤 값 중 홀수만 5개 저장한다.
# count = 0
# run = 1
# while run == 1 :
# 	r = random.randint(-100, 100)
# 	if r % 2 == 1 :
# 		a.append(r)
# 		count += 1
# 	if count == 5:
# 		run = 0
# print(a)

# # 조건2 : 그중에 가장 큰 수와 작은 수를 출력
# for i in range(len(a)) :
# 	if max < a[i] : 
# 		max = a[i]
# 	if min > a[i] :
# 		min = a[i]

# print("가장 큰 값 =", max)
# print("가장 작은 값 =", min)
 
# [1차]
# for i in range(5):
# 	r = random.randint(-100, 100)
# 	a.append(r)

# 	if max < a[i]:
# 		max = a[i]
# 	if min > a[i]:
# 		min = a[i]

# print(a)

# print(max)
# print(min)



