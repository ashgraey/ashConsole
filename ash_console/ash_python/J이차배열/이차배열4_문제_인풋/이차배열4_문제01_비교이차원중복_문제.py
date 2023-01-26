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

for i in range(len(a)) :
    for j in range(len(a[i])) :

        for x in range(len(b)) :
            for y in range(len(b[x])) :
                if(a[i][j] == b[x][y]) :
                    a[i][j] = 0
                    b[x][y] = 0

print("a =")
for i in range(len(a)) :
    print(a[i])
print("b =")
for i in range(len(a)) :
    print(b[i])

    