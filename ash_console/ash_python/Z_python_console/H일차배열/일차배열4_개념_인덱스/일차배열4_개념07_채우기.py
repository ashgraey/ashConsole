'''
	[문제]
		공간이 10개인 a리스트가 있다. 
		랜덤(0~9)숫자 한 개를 저장한다.
		랜덤 숫자의 인덱스부터 랜덤 숫자만큼 1부터 1씩 증가하면서 순차적으로 채운다.
		단, 만약에 숫자가 리스트 길이를 벗어나면 앞에서부터 채운다.
  
	[예시1]
		r = 3
		a = [0,0,0,1,2,3,0,0,0,0]  
  			- 인덱스 3부터 3개를 채운다.
	
 	[예시7]
		r = 7
		a = [4,5,6,7,0,0,0,1,2,3] 
  			- 인덱스 7부터 7개를 채운다.
  			- 리스트를 벗어나기 때문에 앞으로 이동 후 채운다.
'''

import random

a = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

r = random.randint(0, 9)
print("r =", r)

# 방법1)
value = 1
count = 0
i = r			 # 인덱스 3부터 시작해서
while count < r: # count가 3이 될때까지 반복
	# print(i, end=" ")
	a[i] = value
	value += 1
	i += 1
	count += 1
	if i >= len(a):
		i = 0
print("a =", a)

# 방법2)
value = 1
count = 0
i = r			 # 인덱스 3부터 시작해서
while count < r: # count가 3이 될때까지 반복
	a[i % len(a)] = value
	value += 1
	i += 1
	count += 1
	
print("a =", a)