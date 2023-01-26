'''
    [문제]
        숫자 10과 3을 각각 저장한다.
        랜덤으로 0~3 저장한다. 랜덤숫자는 연산자에 해당하고,
        각각의 숫자는 다른 연산자를 뜻한다. 
        (0 은 +, 1 은 -, 2는 *, 3은 / )
        숫자10과 3을 연산해주는 함수들과 식을 만드시오.
        위 식을 5번 반복하시오.
    [예시]
       r = 3
       3은 / 이므로 10 / 3 
'''
import random

def plus(x, y):
    result = x + y
    print(result)

def minus(x, y):
    result = x - y
    print(result)

def multiply(x, y):
    result = x * y
    print(result)

def divide(x, y):
    result = x / y
    print(result)

x = 10
y = 3

for i in range(5):
    op = random.randint(0, 3)
    print("op =", op, end=" : ")

    if op == 0:
        plus(x, y)
    elif op == 1:
        minus(x, y)
    elif op == 2:
        multiply(x, y)
    elif op == 3:
        divide(x, y)

