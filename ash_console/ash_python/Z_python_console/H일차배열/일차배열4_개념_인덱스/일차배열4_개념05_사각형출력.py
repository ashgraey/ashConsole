'''
	[문제]	
		아래 리스트 a의 값을 사각형 모양으로 출력하시오.
	[예시]
		1 2 3 
		4 5 6 
		7 8 9 
'''

a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
'''
0 1 2
3 4 5
6 7 8
'''

# 방법1)
count = 0
for i in range(len(a)):
	print(a[i], end=" ")
	count += 1

	if count == 3:
		print()
		count = 0
print()

# 방법2)
for i in range(len(a)):
	print(a[i], end=" ")
	if i % 3 == 2:
		print()


