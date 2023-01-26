'''
    [문제]
        a리스트와 b리스트를 비교해서 서로 겹치는 값을 0으로 변경하시오.
    [정답] 
        a = [
                [0, 0, 0],
                [0, 7, 2]
            ] 
        b = [0, 6, 0, 0, 0]
'''

a = [[1,4,3],[5,7,2]]
b = [4,6,3,1,5]

for i in range(len(b)):

    for j in range(len(a)):
        for k in range(len(a[j])):
            if b[i] == a[j][k]:
                a[j][k] = 0
                b[i] = 0
for i in range(len(a)):
    print(a[i])
print(b)