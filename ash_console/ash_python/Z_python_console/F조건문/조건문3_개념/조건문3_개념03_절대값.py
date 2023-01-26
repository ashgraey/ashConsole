'''
랜덤 값 (1~10) 두 개를 저장한다.
앞의 숫자에서 뒤에 숫자를 뺀다. 
만약에 값이 음수라면 양수로 변환해서 출력하시오.
'''

import random 

a = random.randint(1, 10)
b = random.randint(1, 10)

c = a - b
print(a, " ", b, " ", c)


if c < 0:
    c = c * -1
print(a, " ", b, " ", c)