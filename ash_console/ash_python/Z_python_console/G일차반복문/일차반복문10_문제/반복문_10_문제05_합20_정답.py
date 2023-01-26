'''
    [문제]
        1~10 사이의 랜덤 숫자 3개 저장하고
        그 숫자의 합이 무조건 20이 되도록 출력해보자.
'''

import random

run = 1
while run == 1:
    x = random.randint(1, 10)
    y = random.randint(1, 10)
    z = random.randint(1, 10)
    
    total = x + y + z
    if total == 20:
        run = 0
print(x, y, z)