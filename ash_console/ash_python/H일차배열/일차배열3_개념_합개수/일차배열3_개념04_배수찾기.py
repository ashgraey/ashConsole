'''
    [문제]
        랜덤 숫자 100~200을 다섯 개 저장하고,
        다섯 개 숫자 중에 3의 배수들을 출력하시오.
        3의 배수들의 개수와
        3의 배수들의 누적 합도 출력하시오.
'''

import random

arr = []

count = 0
total = 0

for i in range(5):
    num = random.randint(100, 200)
    arr.append(num)

    if arr[i] % 3 == 0:
        total += arr[i]
        count += 1
        print(arr[i])

print(arr)

print("개수 =", count)
print("합 =", total)




