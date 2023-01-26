'''
    [문제]
        랜덤(2~100) 숫자를 저장해 그 수의 약수를 모두 리스트에 저장한다.
        위 규칙을 다섯 번 반복하여 이차원리스트를 만드시오.
    [정답]
        27 [1, 3, 9, 27]
        72 [1, 2, 3, 4, 6, 8, 9, 12, 18, 24, 36, 72]
        76 [1, 2, 4, 19, 38, 76]
        94 [1, 2, 47, 94]
        91 [1, 7, 13, 91]  
'''
import random

a = []

for i in range(5):
    r = random.randint(2, 100)
    print(r, end=" ")
    temp = []
    for j in range(r):
        if r % (j + 1) == 0:
            temp.append(j + 1)
    
    a.append(temp)
    print(a[i])
print()

