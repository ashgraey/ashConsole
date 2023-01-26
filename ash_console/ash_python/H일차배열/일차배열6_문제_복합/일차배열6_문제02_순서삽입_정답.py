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
r = 50
print("r =", r)

# 인덱스의 값부터 구한다.
index = -1
for i in range(len(a) - 1):
    if a[i] <= r and r < a[i + 1]:
        index = i + 1
print("index =", index)

# 구해진 인덱스의 값을 조건문을 통해 다시 구분
# a[0]보다 값이 작을 경우
if index == -1:
    a.append(r)
# a[0]보다 값이 클 경우
else:
    a.append(r)
    i = len(a) - 1
    while i > index:
        a[i] = a[i - 1]
        i -= 1
    a[index] = r
print(a)