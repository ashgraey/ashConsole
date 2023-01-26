'''
[문제]
	90과 45의 최대공약수를 출력하시오.
[출력]
	45
'''
answer = 0

i = 1
while i <= 45:
	if 90 % i == 0 and 45 % i == 0:
		answer = i
		# print(i, end=" ")
	i += 1

print(answer)
