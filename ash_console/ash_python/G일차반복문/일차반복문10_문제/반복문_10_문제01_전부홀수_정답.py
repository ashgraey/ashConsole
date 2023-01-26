'''
   [문제]
      1 ~ 9 사이의 랜덤 값을 4개 출력한다. 
      랜덤 값이 모두 홀수이면 "당첨"을 출력,
      하나라도 홀수가 아니면 "꽝" 출력한다.
      
      [예시] 
         3 1 5 1 : "당첨"
         5 2 1 4 : "꽝"
'''

import random

count = 0

i = 0
while i < 4:
    num = random.randint(1, 9)
    print(num, end=" ")

    if num % 2 == 1:
        count += 1
    i = i + 1

print()
if count == 4:
    print("당첨")
if count != 4:
    print("꽝")