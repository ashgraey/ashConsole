'''
    [문제]
        [조건1] 배열에 랜덤숫자(1~10) 다섯 개를 추가한 후,  5보다 큰수만 출력하시오.
        [조건2] 위 조건의 개수를 출력하시오.
'''
import random

a = []

for i in range(5):
    r = random.randint(1, 10)
    a.append(r)
print("a :", a)

count = 0
for i in range(len(a)):
    if a[i] > 5:
        print(a[i])
        count += 1
print("count =", count)

