'''
	[문제]
		랜덤으로 2~5 를 저장하고, 
		랜덤숫자의 개수만큼 숫자를 더하는 문제와 답을 만들어 출력하시오..
		단 더하기 할 숫자들은 1~9사이의 홀수인 랜덤숫자여야 한다. 
		
		아래 [출력] 뒤에 나오는 모양과 똑같은 모양으로 출력한다. 
		(단, 숫자는 랜덤이므로 숫자는 다르게 나올 수 있다.)
			
		[예시1]		  		
			랜덤 ==> 3
			[출력] 5 + 3 + 1 = 9
			
		[예시2]
			랜덤 ==> 5
			[출력] 1 + 5 + 3 + 7 + 1 = 17
'''

import random

count = random.randint(2, 5)
print("문제 개수 =", count)

total = 0

i = 0
while i < count:
    num = random.randint(1, 9)
    if num % 2 == 1:
        total += num
        print(num, end="")

        if i < count - 1:
            print(end=" + ")

        i += 1
print(" =", total)

    
    