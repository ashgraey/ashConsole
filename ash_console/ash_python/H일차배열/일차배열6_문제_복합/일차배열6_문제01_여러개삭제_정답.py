'''
    [문제]  
        아래 a리스트는 순서대로 값이 저장되어있다.
        랜덤(1~100)숫자 하나를 저장 후,
        랜덤 값보다 작은 값은 전부 a리스트에서 삭제하시오.
    [정답]

'''
import random

a = [10, 20, 30, 40, 50, 60]

r = random.randint(1, 100)
print("r =", r)

i = 0
while True:
    if i == len(a):
        break

    if a[i] < r:
        a.remove(a[i])
        i -= 1
    i += 1
print(a)