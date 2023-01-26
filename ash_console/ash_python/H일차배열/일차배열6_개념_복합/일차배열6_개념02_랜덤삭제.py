'''
    [문제]
        [조건1] 리스트에 랜덤숫자(1~100) 5개를 추가한다.
        [조건2] 랜덤으로 위 값 중 한 개만 삭제 후 출력하시오. 
    
    [예시]
        a = [1, 43, 22, 77 ,44]
        r = 3
        a = [1, 43, 22, 44]
'''

import random

a = []

for i in range(5):
    num = random.randint(1, 100)
    a.append(num)
print(a)

r = random.randint(0, len(a))
print(r)

a.remove(a[r])
print(a)



