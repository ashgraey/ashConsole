'''
	[문제]
		이번 달 1일이 수요일이라고 할 때, 
		랜덤으로 1~31을 저장하고 해당 요일을 출력하시오.

		[예]
		3일 ==> 금요일
'''
'''
    월      화      수      목      금      토      일
                    1       2       3       4       5
    6       7       8       9       10      11      12
    13      14      15      16      17      18      19
    20      21      22      23      24      25      26
    27      28      29      30      31
'''

import random

day = random.randint(1, 31)
print(day, "일")

unit = day % 7

if unit == 1:
    print("수요일")
if unit == 2:
    print("목요일")
if unit == 3:
    print("금요일")
if unit == 4:
    print("토요일")
if unit == 5:
    print("일요일")
if unit == 6:
    print("월요일")
if unit == 0:
    print("화요일")
