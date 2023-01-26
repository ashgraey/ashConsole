'''
    [반복문 옵션 break]
        반복문 안에서 즉시 종료하고 싶을 때 사용한다.
        기존엔 변수를 사용해서 제어했는데, break를 사용하면 쉽게 종료 가능하다.
        break를 사용하면 쉽게 반복문 제어가 가능하나, 꼭 사용하지 않아도 된다. 
    
    [문제]
        무한반복문안에서 랜덤(1~10) 숫자 하나를 저장한다. 
        숫자가 5가 나오면 반복문을 종료한다.
'''
import random

# 기존방법
run = 1
while run == 1:
    r = random.randint(1, 10)
    print(r , end=" ")
    if r == 5:
        run =0
        
print()
print("-------------------")

# break 사용시
while True:
    r = random.randint(1, 10)
    print(r , end=" ")
    if r == 5:
        break