'''
    [문제]
        리스트a 와 리스트b 에 랜덤 숫자(1~10) 다섯 개씩 저장하고,
        둘 다 출력하시오.
'''
import random

a = []
b = []

for i in range(5):
    r = random.randint(1, 10)
    a.append(r)
    r = random.randint(1, 10)
    b.append(r)

print("a :", a)
print("b :", b)

