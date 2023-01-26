'''
    [문제]  
        a리스트가 있을 때, 리스트 사이에 값을 추가하고 
        나머지 값들은 뒤로 밀어내는 것을 삽입이라고 한다. 
        랜덤(0,5)으로 위치를 입력받고 
        a리스트 사이의 그 위치에 값 100을 삽입해 보시오.
    [예시]
        r = 3   
        a = [10,34,56,100,8,43]
'''

import random

a = [10, 34, 56, 8, 43]

# idx = random.randint(0, len(a))
idx = 5
print("idx =", idx)
value = 100

'''
idx = 3
value = 100

10, 34, 56, 8, 43
10, 34, 56, 8, 43, 100
10, 34, 56, 100, 8, 43
방      =   값
a[5]    =   a[4]
a[4]    =   a[3]
'''

if idx == len(a):
    a.append(value)
else:
    a.append(value)
    i = len(a) - 1
    while i > idx:
        a[i] = a[i - 1]
        i -= 1
    a[idx] = value
print("a =", a)

