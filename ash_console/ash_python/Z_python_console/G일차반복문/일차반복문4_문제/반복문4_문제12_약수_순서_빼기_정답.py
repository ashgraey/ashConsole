'''
	[문제] 
		100의 약수 중에서 
        5번째 약수에서 2번째 약수를 뺀 값을 구하시오.
	[정답]
		8
'''

num = 100

first = 0
last = 0

count = 0

i = 1
while i <= num:
	if num % i == 0:
		count += 1

		if count == 2:
			first = i
		if count == 5:
			last = i
	i += 1

result = last - first
print(result)