'''
	  	[문제]
		 	아래 리스트를 아래와 같이 출력하시오.
		[결과]
			1
			23
			456
			7890
'''
'''
0
12
345
6789

'''
a = [1,2,3,4,5,6,7,8,9,0]

start = 0
end = 1 
for i in range(len(a)) :
	print(a[i], end = " ")
	start += 1

	if start == end :
		start = 0 
		end += 1
		print()