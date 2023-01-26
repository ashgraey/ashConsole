'''
[문제]
    a 변수에 1부터 10 사이의 랜덤 숫자를 저장하고, 
    "짝수" 또는 "홀수"를 출력하시오.
'''

import random

a = random.randint(1, 10)

if a % 2 == 0:
    print("짝수")
if a % 2 == 1:
    print("홀수")


