'''
    [문제]
        [1] a이차리스트에 랜덤 값(1~100)을 9개 저장 후 출력하시오.
        [2] 랜덤으로 값 두 개를 선택 후 두 개의 위치를 교환 후 출력하시오.
    [예시]
    값 교체 전 >>>
    [46, 62, 75]
    [36, 18, 100]
    [26, 11, 39]

    r1 = 11
    r2 = 36
    
    값 교체 후 >>>
    [46, 62, 75]
    [11, 18, 100]
    [26, 36, 39]
'''
import random

a = [[0,0,0], [0,0,0], [0,0,0]]

for i in range(len(a)):
    for j in range(len(a[i])):
        a[i][j] = random.randint(1, 100)
print("값 교체 전 >>>")
for i in range(len(a)):
    print(a[i])

rY1 = random.randint(0, len(a) - 1)
rX1 = random.randint(0, len(a) - 1)
print("r1 =", a[rY1][rX1])

rY2 = random.randint(0, len(a) - 1)
rX2 = random.randint(0, len(a) - 1)
print("r2 =", a[rY2][rX2])

temp = a[rY1][rX1]
a[rY1][rX1] = a[rY2][rX2]
a[rY2][rX2] = temp

print("값 교체 후 >>>")
for i in range(len(a)):
    print(a[i])