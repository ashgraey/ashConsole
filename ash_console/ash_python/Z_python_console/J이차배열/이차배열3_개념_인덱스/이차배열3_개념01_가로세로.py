'''
    [문제]
        a리스트의 가로 합을 garo리스트에 추가하시오.
        a리스트의 세로 합을 sero리스트에 추가하시오.
    [정답]
        garo = [410, 710, 1210]
        sero = [503, 606, 609, 612]
'''
a = [
    [101, 102, 103, 104],
    [101, 202, 203, 204],
    [301, 302, 303, 304],
     ]

garo =[]
sero =[]

for i in range(3):
    total = 0
    for j in range(4):
        total += a[i][j]
    garo.append(total)
print("garo =", garo)

for i in range(4):
    total  = 0
    for j in range(3):
        total += a[j][i]
    sero.append(total)
print("sero =", sero)
