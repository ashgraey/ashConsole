'''
[문제]
 	변수에 숫자를 랜덤으로 저장한다(1~100)
  	해당 숫자의 값이 4의 배수이면 True
   	4의배수가 아니면 False 출력하시오.
'''

import random

num = random.randint(1, 100)
print("num =", num)

if num % 4 == 0:
	print(True)
else:
	print(False)
