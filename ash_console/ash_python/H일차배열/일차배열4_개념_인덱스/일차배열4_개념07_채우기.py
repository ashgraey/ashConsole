'''
	[문제]
		공간이 10개인 a리스트가 있다. 
		랜덤(0~9)숫자 한개를 저장한다.
		랜덤숫자의 인덱스부터 랜덤숫자만큼 1부터 1씩증가하면서 순차적으로채운다.
		단, 만약에 숫자가 리스트 길이를 벗어나면 앞에서부터 채운다.
  
	[예시1]
		r = 3
		a = [0,0,0,1,2,3,0,0,0,0]  
  			- 인덱스 3부터 3개를채운다.
	
 	[예시7]
		r = 7
		a = [4,5,6,7,0,0,0,1,2,3] 
  			- 인덱스 7부터 7개를 채운다.
  			- 리스트를 벗어나기때문에 앞으로 이동후 채운다.
'''
import random
a = [0,0,0,0,0,0,0,0,0,0]

# [방법1]
r = random.randint(0, 9)
print("r =", r)

idx = r 
count = 0 
value = 1


while count < r :
	a[idx] = value
	idx += 1 
	value += 1  
	count += 1
	
	if idx >= len(a) :
		idx = 0
		
print(a)
print()

# [방법2]
idx = r
count = 1 
while count <= r :
	a[idx % len(a)] = count
	idx += 1 
	count += 1 
print(a)



