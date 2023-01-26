'''
    [문제]  
        아래 a리스트는 순서대로 값이 저장되어있다.
        랜덤(1~70)숫자 하나를 저장 후,
        a리스트의 값들 사이에 저장하려고 한다. 
        저장조건은 a리스트의 바로 앞의 값 보다는 크고 
        바로 뒤의 값 보다는 이하인 위치에 삽입 후 출력하시오.
    [예시]
        r = 54
        a = [10,20,30,40,50,54,60]

'''
import random

a = [10, 20, 30, 40, 50, 60]

r = random.randint(1, 70)
print("r =", r)

index = -1
for i in range(len(a) - 1):
    if a[i] <= r and r < a[i + 1]:
        index = i + 1
print("index =", index)

# 파이썬은 index값이 -1이면, 맨 뒤를 의미한다.
# 음수 인덱스가 나올 경우, 맨 처음 값은 별도의 식이 필요하다.
if index == -1:
    if r < a[0]:
        a.append(r)
        i = len(a) - 1
        while i > 0:
            a[i] = a[i - 1]
            i -= 1
        a[0] = r
    else:
        a.append(r)
else:
    a.append(r)
    i = len(a) - 1
    while i > index:
        a[i] = a[i - 1]
        i -= 1
    a[index] = r
print(a)