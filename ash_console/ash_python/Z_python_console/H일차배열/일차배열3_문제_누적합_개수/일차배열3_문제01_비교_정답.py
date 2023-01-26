'''
    [문제]
        [조건1] 리스트에 랜덤숫자(1~100) 5개를 추가한다.
        [조건2] 리스트의 숫자중 50보다 큰 값들만 출력하시오.
        [조건3] 위 조건의 값들의 누적 합을 출력하시오.
        [조건4] 위 조건의 개수 출력하시오.
       
    [예시]
        a = [1, 83, 22, 77 ,19]
        비교 = 50
        출력 : 83, 77
        합 : 160
        개수 : 2
'''
import random

a = []

count = 0
total = 0

for i in range(5):
    num = random.randint(1, 100)
    a.append(num)

    if a[i] > 50:
        count += 1
        total += a[i]
        print(a[i])

print(a)

print("개수 =", count)
print("합 =", total)



