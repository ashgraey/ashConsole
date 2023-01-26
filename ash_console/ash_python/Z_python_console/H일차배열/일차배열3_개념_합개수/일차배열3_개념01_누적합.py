'''
    [문제]
        [조건1] 배열에 랜덤숫자(1~10) 5개를 추가하고,
        [조건2] 위 조건의 누적합을 출력하시오.
'''
import random

a = []

for i in range(5):
    r = random.randint(1, 10)
    a.append(r)
print("a =", a)

total = 0
for i in range(len(a)):
    # total = total + a[i]
    print("total =", total, "+", a[i])
    total += a[i]
print("total =", total)
