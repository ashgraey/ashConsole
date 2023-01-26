'''
    [문제]
        랜덤숫자 1~10 을 다섯 개 저장한다.
        다섯 개 숫자 중에 40의 약수들을 출력하시오.
        40의 약수들의 개수와
        40의 약수들의 누적 합도 함께 출력하시오.
    * 배수
        예) 3의 배수 = 3x1, 3x2, 3x3, ...
                        n % 3 == 0
    * 약수  
        예) 40의 약수 = 1부터 자기 자신까지(=40) 나눴을 때 0으로 딱 떨어지는 수
                        1, 2, 4, 5, ...., 40
                        40 % n == 0
'''

import random

arr = []

for i in range(5):
    num = random.randint(1, 10)
    arr.append(num)
print("arr =", arr)

count = 0
total = 0
for i in range(len(arr)):
    if 40 % arr[i] == 0:
        print(arr[i])
        count += 1
        total += arr[i]

print("40의 약수의 개수 =", count)
print("40의 약수의 합 =", total)


