'''
	[문제]	
		아래 리스트 a의 값을 사각형 모양으로 출력하시오.
	[예시]
		123
		456
		789
'''

a = [1, 2, 3, 4, 5, 6, 7, 8, 9]

count = 0
for i in range(len(a)):
    print(a[i] , end=" ")
    count += 1
    if count == 3:
        print()
        count =0

print()

for i in range(len(a)):
	print(a[i], end=" ")
	if i % 3 == 2:
		print()
    



