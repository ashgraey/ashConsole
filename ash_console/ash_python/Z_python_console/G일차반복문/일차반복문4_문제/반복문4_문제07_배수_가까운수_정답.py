'''
	[문제] 
  		6의 배수를 순차적으로 검사한다. 
  		그중 100에 가장 가까운 수를 출력하시오. 
 	[정답]
		102
'''

i = 1

first = 0

while i < 100:
	if i % 6 == 0:
		first = i
	i += 1
print(first)

last = first + 6
print(last)

first_result = 100 - first

last_result = last - 100
if last_result < 0:
	last_result = -last_result

if first_result < last_result:
	print(first)
if first_result >= last_result:
	print(last)
