'''
    [문제]
        1~10 사이의 숫자를 랜덤으로 2개 저장하고,
        작은 숫자부터 큰 숫자까지의 합을 출력하는 함수를 만드시오.
    [예시]
        5, 3 ==> 3 + 4 + 5 = 12
        2, 6 ==> 2 + 3 + 4 + 5 + 6 = 20
'''

import random

def printTotal(x, y):
    if x > y:
        temp = x
        x = y
        y = temp
    
    total = 0
    i = x
    while i <= y:
        print(i, end="")

        if i < y:
            print(" + ", end="")
        total += i
        i += 1
    print(" =", total)

x = random.randint(1, 10)
y = random.randint(1, 10)
print(x, y, "==> ", end="")
printTotal(x, y)

