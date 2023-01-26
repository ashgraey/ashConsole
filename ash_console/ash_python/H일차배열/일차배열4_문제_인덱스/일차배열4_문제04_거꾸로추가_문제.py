'''
	[문제]
		a 리스트의 값을 b리스트에 추가한다.
		단, 값은 거꾸로 추가한다.
	[결과]
		b = [40,30,20,10]
'''

a = [10, 20, 30, 40]
b = []

'''
0 1 2 3 4 
4 3 2 1 0

'''
# [1115]
# idx = len(a) - 1
# for i in range(len(a)) :
# 	b.append(a[idx])

# 	idx -= 1
	 
# print(a) 
# print(b)

# [1차]
# temp = len(a) - 1
# for i in range(len(a)) : 
# 	# b[i] = a[temp]
# 	b.append(a[temp])
# 	temp -= 1
# print(b)
