'''
    [문제]
        a리스트와 b리스트를 비교해서 서로 겹치는 값을 0으로 변경하시오.
    [정답] 
    a = [
            [0, 4, 0],
            [0, 0, 0]
        ]
    b = [
            [0, 0, 0],
            [0, 0, 8]    
        ]
'''

a = [[1,4,3],[5,7,2]]
b = [[5,3,2],[1,7,8]]

for i in range(len(a)):
    for j in range(len(a[i])):

        for y in range(len(b)):
            for x in range(len(b[y])):
                if a[i][j] == b[y][x]:
                    a[i][j] = 0
                    b[y][x] = 0

for i in range(len(a)):
    print(a[i])
print()

for i in range(len(b)):
    print(b[i])