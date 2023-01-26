'''
    [문제]
        1~100 사이의 숫자를 랜덤으로 저장하고
        그 수가 짝수인지 홀수인지 출력하는 함수를 만드시오.
        위 식을 10번 반복하시오.
    [예시]
        23 : 홀수
        8 : 짝수
        48 : 짝수
        62 : 짝수
        71 : 홀수
        56 : 짝수
        100 : 짝수
        45 : 홀수
        52 : 짝수
        7 : 홀수   
'''
import random

def checkNumber(a):
    print(a, end=" : ")
    if a % 2 == 0:
        print("짝수")
    else:
        print("홀수")

for i in range(10):
    r = random.randint(1, 100)
    checkNumber(r)