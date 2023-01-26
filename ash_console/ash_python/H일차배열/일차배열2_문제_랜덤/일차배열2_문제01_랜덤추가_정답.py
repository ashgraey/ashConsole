'''
    [문제]
        랜덤 숫자(1~5)를 한 개 저장한다. 
        랜덤 숫자만큼 반복문을 돌리고, 
        저장한 랜덤 숫자를 계속 저장한다.
    [예시]
        r = 3 
        arr = [3,3,3]
    [예시]
        r = 5
        arr = [5,5,5,5,5]  
'''

import random
arr = []

r = random.randint(1, 5)
print("r =", r)

i = 0
while i < r:
    arr.append(r)
    i += 1

print(arr)


