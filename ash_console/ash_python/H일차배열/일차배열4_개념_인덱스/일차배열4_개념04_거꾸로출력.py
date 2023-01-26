'''
	[문제]	
		a 의 값들을 거꾸로 출력한다.
	
'''
a =[21,44,12,54,60]

# [1115]
idx = len(a) - 1
for i in range(len(a)) :
    print(a[idx], end = " ")
    idx -= 1 


