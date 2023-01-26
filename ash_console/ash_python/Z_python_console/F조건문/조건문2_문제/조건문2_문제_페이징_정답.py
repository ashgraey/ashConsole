''' 
    [문제]
        랜덤 1~2000 사이의 숫자를 저장하고, 다음과 같이 출력하시오.

        랜덤 숫자가
        1   ~ 10    사이 값이면, 1
        11  ~ 20    사이 값이면, 2
        21  ~ 30    사이 값이면, 3
        
        ...
        
        101 ~ 110은 사이 값이면, 11
        
        ...
        
        1001 ~ 1010 사이 값이면, 101
'''
import random

num = random.randint(1, 2000)
num = 1001
print(num)

unit = num // 10
if num % 10 != 0:
    unit = unit + 1
print(unit)