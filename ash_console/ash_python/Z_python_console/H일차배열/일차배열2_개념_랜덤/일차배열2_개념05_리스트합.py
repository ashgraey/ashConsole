'''
    [문제]
        랜덤숫자(1~100)를 각각 다섯개씩 a 와 b에 저장하고,
        a 와 b 의 각 자리의 합을 total에 추가하시오.
'''
import random

a = []
b = []
total = []

for i in range(5):
    a.append(random.randint(1, 100))
    b.append(random.randint(1, 100))

print("a :", a)
print("b :", b)

for i in range(5):
    result = a[i] + b[i]
    total.append(result)
print("total :", total)

