'''
    [문제]
        랜덤 숫자(1~10) 다섯 개를 arr에 추가하고
        그 두 배를 total에 저장 후 출력하시오.
    [예시]
        arr   = [10, 3, 4, 2, 6]
        total = [20, 6, 8, 4, 12]
'''

import random

arr = []
total = []

i = 0
while i < 5:
    r = random.randint(1, 10)
    arr.append(r)

    total.append(r * 2)
    i += 1
print(arr)
print(total)

