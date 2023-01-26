'''
	[문제] 
		다음 리스트를 이용해서 a의 값 중 
		홀수만 b에 저장하고 출력하시오.
	[예]   
 		b = [ 49, 51, 17 ]
'''
a = [49, 2, 51, 22, 17]
b = []

for i in range(len(a)):
	if a[i] % 2 == 1:
		# print(a[i])
		b.append(a[i])
print("b =", b)
