'''
	[문제]
		a리스트를 순차적으로 검사한다.
		b리스트의 값들이 a리스트의 값들과 완벽히 겹치는지 검사하시오.
		겹치면 "o" , 안겹치면 "x"를 출력하시오.

	[예시1] 
		b = [6,1,8] : [1,3,3,6,5,(6,1,8),9] 완벽히 겹친다.
	[예시2]
		b =[6,3] : [1,3,3,6,5,6,1,8,9] 겹치는 부분이 없다.
	[예시3]
		b =[3,6,5,6] : [1,3,(3,6,5,6),1,8,9] 완벽히 겹친다.
'''
a = [1,3,3,6,5,6,1,8,9]
b = [6,1,8]
# b = [6,3]
# b = [3,6,5,6]

check = False

count = 0
for i in range(len(a) - len(b) + 1):
	for j in range(len(b)):
		if a[i + j] == b[j]:
			count += 1
		else:
			count = 0
	if count == len(b):
		check = True
		break
	
if check:
	print("O")
else:
	print("X")