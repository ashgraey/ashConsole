'''
    [문제]
        랜덤 숫자 100~200을 다섯 개 저장하고,
        다섯 개 숫자 중에 3의 배수들을 출력하시오.
        3의 배수들의 개수와
        3의 배수들의 누적 합도 출력하시오.
'''
import random

arr = []

for i in range(5):
    r = random.randint(100, 200)
    arr.append(r)
print("arr =", arr)

count = 0
total = 0
for i in range(len(arr)):
    if arr[i] % 3 == 0:
        print(arr[i])
        total += arr[i]
        count += 1

print("3의 배수의 개수 =", count)
print("3의 배수의 합 =", total)




