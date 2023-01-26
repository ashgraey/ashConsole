'''
[최대값]
    [1] 숫자 3개를 랜덤으로 저장한다. (-100 ~ 100 사이의 숫자)
    [2] 3개의 랜덤 숫자를 비교한다.
    [3] 가장 작은 수(MIN)를 출력한다.    
'''

import random

x = random.randint(-100, 100)
y = random.randint(-100, 100)
z = random.randint(-100, 100)

print(x, y, z)

min = x
if min > y:
    min = y
if min > z:
    min = z

print(min)
