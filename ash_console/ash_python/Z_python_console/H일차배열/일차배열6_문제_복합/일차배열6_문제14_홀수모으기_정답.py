'''
	[문제]
		[1] 랜덤숫자 1~9 다섯 개를 리스트에 추가한다.
		[2] 그 숫자 중 홀수만 하나로 모아서 숫자로 만든다. (더하기가 아니다.)
		[3] 그 숫자의 두 배를 출력한다. 
	
	[예시] 
		2 5 3 4 6 이 랜덤으로 저장되었다고 가정했을 때,
		홀수는 5, 3 이므로 합치면 53이 된다. 
		53의 두 배는 106이다. 
'''

import random

a = []
temp = []

for i in range(5):
	r = random.randint(1, 9)
	a.append(r)
	
	if a[i] % 2 == 1:
		temp.append(a[i])
	
print("a =", a)
print("temp =", temp)

size = len(temp)

multiply = 1
for i in range(size - 1):
	multiply *= 10
# print(multiply)

number = 0
for i in range(size):
	number += temp[i] * multiply
	multiply //= 10
print(number)

answer = number * 2
print("정답 =", answer)
