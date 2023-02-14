"""
    [소수] 소수란 1과 자신으로만 나눠지는수 
    [소수 구하는 방법 두가지]
   
    [1] 전부 나눠보기
        소수를 구하는 숫자를 2부터 그숫자전까지 전부 나눠본다. 
        한번이라도 나눠지면 소수가 아니다.
"""


a = 15
i = 2
check = False
while i < a:
    if a % i == 0:
        check = True
        break
    i += 1

if check == True:
    print(a, "소수가아니다.")
else:
    print(a, "소수이다.")

"""
    [2] 제곱근까지 나누기 
        예를 들어 15를 1부터 15까지 전부 나눈다고햇을때, 나눠지는 때를 생각해보면

        1 , 15
        3, 5
        5, 3
        15, 1

        위와같이 아래 2번은 위와 동일하다는것을알수있다. 즉 15의 제곱근까지만 확인하면 나머지는 할필요가없다.
"""

import math

num = math.sqrt(a) # a의 제곱근을 구한다. 
i = 2
check = False
while i <= int(num): # 제곱근까지 나눠야 한다. 
    if a % i == 0:
        check = True
        break
    i += 1

if check == True:
    print(a, "소수가아니다.")
else:
    print(a, "소수이다.")
