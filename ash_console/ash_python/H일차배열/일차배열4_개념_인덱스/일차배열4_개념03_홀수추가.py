'''

	[문제] 다음 리스트를 이용해서 a 의 값중 홀수만 b 에 저장
		
	[예]   
 		b = [ 49, 51, 17 ]
'''
a = [49,2,51,22,17]

b = []

for i in range(len(a)) :
	if a[i] % 2 == 1 :
		b.append(a[i])

print("b =", b)