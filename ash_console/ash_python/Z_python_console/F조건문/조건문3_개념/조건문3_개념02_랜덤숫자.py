'''
[문제]
    랜덤으로 숫자 1이나 7을 출력하시오.
'''
import random

a = random.randint(1, 2)

if a == 2:
    a = 7

print(a)