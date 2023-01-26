'''
[문제]
	[1] 1~99 사이의 랜덤 숫자를 저장한다.
	
	랜덤 숫자 중에서 3이나 6이나 9의 개수가
	[2-1] 2개이면, 짝짝을 출력한다.
	[2-2] 1개이면, 짝을 출력한다.
	[2-3] 0개이면, 해당 숫자를 출력하시오.
	
	[예]
		33	==> 짝짝
		16	==> 짝
		 7	==> 7
'''

import random

num = random.randint(1, 99)
print(num)

x = num // 10
y = num % 10

count = 0
if x == 3 or x == 6 or x == 9:
    count = count + 1
if y == 3 or y == 6 or y == 9:
    count = count + 1

if count == 2:
    print("짝짝")
if count == 1:
    print("짝")
if count == 0:
    print(num)