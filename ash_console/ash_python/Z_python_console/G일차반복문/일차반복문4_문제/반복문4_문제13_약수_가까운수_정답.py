'''
	[문제] 
		200의 약수 중에서 짝수 중 
		80에 가장 가까운 수를 구하시오.
		만약 약수 중에 80이 있을 경우, 80이 정답이다.
	[정답]
		100
'''

num = 200

first = 0
last = 0

i = 1
while i <= num:
	if num % i == 0 and i % 2 == 0 and i <= 80:
		first = i
	if num % i == 0 and i % 2 == 0 and i > 80 and last == 0:
		last = i
	i += 1

first_result = 80 - first
last_result = last - 80

if first_result < last_result:
	print(first)
if first_result >= last_result:
	print(last)




