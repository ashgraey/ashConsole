import random

a = []

'''
    [문제1]
        a리스트를 한 줄당 3개씩 3줄 총 9개로 이차원으로 만들고, 
        랜덤값(1~100)을 9개 저장하시오.
    [예시1]
        [56, 64, 10] 
        [100, 40, 12]
        [9, 70, 29] 
'''
print("[문제1]")
for i in range(3):
    a.append([0, 0, 0])

for i in range(len(a)):
    for j in range(len(a[i])):
        a[i][j] = random.randint(1, 100)

for i in range(len(a)):
    print(a[i])

'''         
    [문제2]
        a리스트값들 중 50이상을 전부 출력하시오.
    [예시2] 
        56 64 100 70
'''
print("[문제2]")
for i in range(len(a)):
    for j in range(len(a[i])):
        if a[i][j] >= 50:
            print(a[i][j], end=" ")
print()

'''
    [문제3]
         a리스트값들 중 4의 배수만 출력하시오.
    [예시3]
        56 64 100 40 12
'''
print("[문제3]")
for i in range(len(a)):
    for j in range(len(a[i])):
        if a[i][j] % 4 == 0:
            print(a[i][j], end=" ")
print()

'''        
    [문제4]
         a리스트값들 중 50이상인 수의 합을 출력하시오.
    [예시4]
        total = 290
'''
print("[문제4]")
total = 0
for i in range(len(a)):
    for j in range(len(a[i])):
        if a[i][j] >= 50:
            total += a[i][j]
print("total =", total)

'''
    [문제5]
         a리스트값들 중 50이상인 수의 개수를 출력하시오.
    [예시5]
        count = 4
'''
print("[문제5]")
count = 0
for i in range(len(a)):
    for j in  range(len(a[i])):
        if a[i][j] >= 50:
            count += 1
print("count =", count)

