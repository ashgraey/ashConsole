'''
[문제]
    1~9 사이의 랜덤 숫자 2개를 저장하고
    그 숫자의 합이 무조건 10이 되도록 출력하시오.
[예시]
    x = 9
    y = 1
'''

import random

x = 0
y = 0

run = 1
while run == 1:
    x = random.randint(1, 9)
    y = random.randint(1, 9)

    total = x + y
    if total == 10:
        run = 0
print("x =", x)
print("y =", y)


