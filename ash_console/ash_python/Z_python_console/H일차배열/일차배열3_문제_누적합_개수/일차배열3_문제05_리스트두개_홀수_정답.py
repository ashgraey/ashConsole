'''
    [문제]
        a리스트와 b리스트에 랜덤 숫자(1~100)를 다섯 개씩 저장하고,
        a리스트의 전체 합과 b리스트의 홀수의 합을 출력하시오. 
        a리스트의 홀수 합과 b리스트의 홀수 합을 비교해서 더 큰 값을 출력하시오.
        서로 같으면 둘 다 출력하시오.
    [예시]
        a = [28, 79, 47, 70, 36]
        b = [63, 4, 45, 54, 87]
        total1 = 126
        total2 = 195
        195    
'''

import random

a = []
b = []

total1 = 0
total2 = 0

for i in range(5):
    a.append(random.randint(1, 100))
    if a[i] % 2 == 1:
        total1 += a[i]

    b.append(random.randint(1, 100))
    if b[i] % 2 == 1:
        total2 += b[i]

print("a =", a)
print("b =", b)
print("total1 =", total1)
print("total2 =", total2)

if total1 > total2:
    print(total1)
elif total2 > total1:
    print(total2)
elif total1 == total2:
    print(total1, total2)