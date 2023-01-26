'''
    [문제]
         1~10 사이의 숫자를 랜덤으로 저장하고,  
         1 ~ 랜덤숫자까지의 합을 출력하는 함수를 만드시오.
    [예시]
        1
        3
        6
        10
        15
        1부터 5 까지의 합 : 15    
'''
import random

def numberTotal(a):
    total = 0
    for i in range(a):
        total += (i + 1)
        print(total)
    print("1부터", a, "까지의 합 :", total)

r = random.randint(1, 10)
numberTotal(r)