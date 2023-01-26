'''
    [문제]
         a 이차리스트에 랜덤(1~100) 값을 9개 저장 후
         사각형 모양으로 출력하시오.
    [예시]
        [38, 14, 54]
        [27, 29, 25]
        [39, 65, 11]
'''
import random

a = [
        [0,0,0],
        [0,0,0],
        [0,0,0]
    ]

for i in range(len(a)):
    for j in range(len(a[i])):
        a[i][j] = random.randint(1, 100)

print("a : ", a)

print("사각형출력")
for i in range(len(a)):
    print(a[i])

