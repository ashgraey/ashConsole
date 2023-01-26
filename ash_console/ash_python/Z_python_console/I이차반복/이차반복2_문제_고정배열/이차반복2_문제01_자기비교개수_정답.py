'''
	[문제]
		a리스트의 각 값이 a리스트 전체와 비교해서 
		각 값이 몇 개 있는지 출력하시오.
	[예시]
		10 : 4
		30 : 2
		40 : 1
		10 : 4
		20 : 1
		30 : 2
		50 : 1
		10 : 4
		10 : 4
'''
a = [10,30,40,10,20,30,50,10,10]

for i in range(len(a)):
    count = 0
    for j in range(len(a)):
        if a[i] == a[j]:
            count += 1
    print(a[i], ":", count)
