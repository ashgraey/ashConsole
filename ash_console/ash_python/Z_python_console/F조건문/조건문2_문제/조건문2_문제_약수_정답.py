'''
  [문제]
    변수에 1부터 10 사이의 숫자를 랜덤으로 저장한다.
    저장한 숫자의 값이 300의 약수이면 "True"
    300의 약수가 아니면 "False" 출력하시오.
'''

import random

num = random.randint(1, 10)
print(num)

if 300 % num == 0:
    print(True)
if 300 % num != 0:
    print(False)