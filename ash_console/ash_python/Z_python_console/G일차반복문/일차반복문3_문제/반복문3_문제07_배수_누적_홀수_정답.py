'''
	[문제]
	    100 ~ 300 사이의 숫자 중에서 
     	[조건1] 9의 배수이면서 홀수인 수를 출력하고, 
      	[조건2] 그 총합을 구하시오.
        [조건3] 위 수의 개수를 구하시오.
	[정답]
		117 135 153 171 189 207 225 243 261 279 297 
		total = 2277
		count = 11	
'''

total = 0
count = 0

i = 100
while i <= 300:
	if i % 9 == 0 and i % 2 == 1:
		print(i, end=" ")
		total += i
		count += 1
	i += 1
print()
print("total =", total)
print("count =", count)