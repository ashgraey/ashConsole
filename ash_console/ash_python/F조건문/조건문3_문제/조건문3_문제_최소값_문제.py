'''
[최대값]
    [1] 숫자 3개를 랜덤으로 저장한다. (-100 ~ 100 사이의 숫자)
    [2] 3개의 랜덤 숫자를 비교한다.
    [3] 가장 작은 수(MIN)를 출력한다.    
'''
import random

r1 = random.randint(-100, 100)
r2 = random.randint(-100, 100)
r3 = random.randint(-100, 100)
print("r1 =", r1)
print("r2 =", r2)
print("r3 =", r3)

# 양수변환
# if r1 < 0 :
#     r1 = -r1
#     print(r1)
# if r2 < 0 :
#     r2 = -r2
#     print(r2)
# if r3 < 0 :
#     r3 = -r3
#     print(r3)

min = r1 
if min > r2 :
    min = r2
if min > r3 :
    min = r3
print("가장 작은 수 =", min)