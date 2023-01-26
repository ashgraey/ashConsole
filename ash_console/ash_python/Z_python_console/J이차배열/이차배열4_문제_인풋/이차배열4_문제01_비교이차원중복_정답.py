'''
    [문제]
        a리스트와 b리스트를 비교해서 
        서로 겹치는 값을 0으로 변경하시오.
        중복되는 값은 전부 0으로 변경한다.
    [정답]
    a = [
            [0, 4, 0],
            [0, 0, 0],
            [0, 4, 0]
        ]
    b = [
            [0, 0, 0],
            [0, 0, 8],
            [6, 0, 0]
        ]
'''

a = [[1,4,3],[5,7,2],[5,4,1]]
b = [[5,3,2],[1,7,8],[6,5,1]]

for i in range(len(a)):
    for j in range(len(a[i])):

        value = 0
        for y in range(len(b)):
            for x in range(len(b[y])):
                if a[i][j] == b[y][x]:
                    value = a[i][j]
                    b[y][x] = 0
        
        for y in range(len(a)):
            for x  in range(len(a[y])):
                if value == a[y][x]:
                    a[y][x] = 0

for i in range(len(a)):
    print(a[i])
print()

for i in range(len(b)):
    print(b[i])