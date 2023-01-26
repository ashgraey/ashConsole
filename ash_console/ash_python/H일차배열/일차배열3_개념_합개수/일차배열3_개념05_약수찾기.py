'''
    [문제]
        랜덤숫자 1~10 을 다섯 개 저장한다.
        다섯 개 숫자 중에 40의 약수들을 출력하시오.
        40의 약수들의 개수와
        40의 약수들의 누적 합도 함께 출력하시오.
'''

import random

arr = []

count = 0
total = 0

for i in range(5):
    num = random.randint(1, 10)
    arr.append(num)

    if 40 % arr[i] == 0:
        count += 1
        total += arr[i]
        print(arr[i])

print(arr)
print("개수 =", count)
print("합 =", total)


