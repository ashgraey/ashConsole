'''
    [문제]
        a리스트를 각 세로 합을 total리스트에 추가하시오.
    [정답]
        total = [10, 9, 13, 3, 16]
'''

a = [
    [0,0,0,0,3],
    [0,2,0,0,3],
    [3,1,3,0,1],
    [1,4,2,0,2],
    [4,1,4,0,4],
    [2,1,4,3,3],   
]

total = []

for i in range(5):
    tot = 0
    for j in range(6):
        tot += a[j][i]
    total.append(tot)

print(total)
	