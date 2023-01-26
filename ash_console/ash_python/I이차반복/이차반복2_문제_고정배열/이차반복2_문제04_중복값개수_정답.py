'''
	[문제]
        a리스트와 b리스트를 전체 비교하여 
        a리스트 안에도 있고 b리스트 안에도 있는 값은 c리스트에 저장하시오. 
        단, b리스트에 같은 값이 두 개 있는 값만 추가하시오.
    [정답]
        [7, 3]
'''
a = [1, 2, 7, 40, 3, 6]
b = [1, 2, 7, 3, 7, 6, 2, 2, 3]
c = []

for i in range(len(a)):
    count = 0
    for j in range(len(b)):
        if a[i] == b[j]:
            count += 1
    if count == 2:
        c.append(a[i])
print(c)
