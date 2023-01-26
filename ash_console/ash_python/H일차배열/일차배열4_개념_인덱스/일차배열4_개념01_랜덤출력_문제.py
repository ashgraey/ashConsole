'''
    [문제]
        [조건1] 리스트에 랜덤숫자(1~100) 5개를 추가하고,
        [조건2] 랜덤으로 위 값 중 한 개만 출력하시오. 
    
    [예시]
        a = [1, 43, 22, 77 ,44]
        출력 : 22
'''

import random
a = []

# [1115]
# for i in range(5) :
#     a.append(random.randint(1, 100))
# print(a)

# idx = random.randint(0, len(a) - 1)
# print("출력 =", a[idx])

# [2차]
# size = 5 
# for i in range(size) :
#     r = random.randint(1, 100)
#     a.append(r)

# print(a)
# index = random.randint(0, len(a) - 1)
# print(index)
# print("출력 =", a[index])

# [1차]
# for i in range(size) :
#     r = random.randint(1, 100)
#     a.append(r)
# print(a)

# index = random.randint(0, len(a) - 1)
# print("index =", index)
# print(a[index])


