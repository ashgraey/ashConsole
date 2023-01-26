"""
[문제]
    아래와 같은 규칙으로 출력하시오.
    랜덤으로 (3~7)사이의 랜덤숫자를 저장한다.
    랜덤숫자만큼 반복되는 패턴을 출력한다. 
    아래의 패턴을 참고하시오. 반복문을 사용하시오.
    
    <패턴1>  r = 4
    
        1 0 1 0 1
        0 1 0 1 0
        1 0 1 0 1
        0 1 0 1 0

    <패턴2> r = 3

        1 0 1 0 1
        0 1 0 1 0 
        1 0 1 0 1

    <패턴3> r = 6

        1 0 1 0 1
        0 1 0 1 0 
        1 0 1 0 1
        0 1 0 1 0 
        1 0 1 0 1
        0 1 0 1 0 
"""
import random

r = random.randint(3, 7)
# r = 3
print("r =", r)

i = 0 
turn = True
while i < r :
    
    if turn == True :
        print("1 0 1 0 1")
    if turn == False :
        print("0 1 0 1 0")

    i += 1 

    if i % 2 == 0 :
        turn = not turn
    else :
        turn = not turn

# [정답]
# import random

# r = random.randint(3, 7)
# i = 0

# a = 1
# b = 0
# print("r : " , r)
# while i < r:
#     if i % 2 == 0:
#         print(a,b,a,b,a)
#     else:
#         print(b,a,b,a,b)
    
#     i += 1