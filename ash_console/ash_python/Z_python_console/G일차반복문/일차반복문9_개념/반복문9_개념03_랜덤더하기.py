'''
[문제]
	2~5 사이의 숫자를 랜덤으로 저장하고,
	랜덤 숫자의 개수만큼 숫자를 더하는 문제와 답을 만들어 출력하시오.
	단, 더하기 할 숫자들은 1~9사이의 랜덤 숫자이어야 한다. 
	아래 [출력] 뒤에 나오는 모양과 똑같은 모양으로 출력한다. 
	(단, 숫자는 랜덤이므로 숫자는 다르게 나올 수 있다.)
		
	[예시1]		  		
		랜덤 ==> 3
		[출력] 5 + 3 + 2 = 10
		
	[예시2]
		랜덤 ==> 5
		[출력] 6 + 5 + 2 + 7 + 8 = 28
'''
import random

count = random.randint(2, 5)
print("반복 횟수 =", count)

total = 0

i = 0
while i < count:
	r = random.randint(1, 9)
	total += r
	print(r, end="")

	if i < count - 1:
		print(end=" + ")
	i += 1

print(" =", total)