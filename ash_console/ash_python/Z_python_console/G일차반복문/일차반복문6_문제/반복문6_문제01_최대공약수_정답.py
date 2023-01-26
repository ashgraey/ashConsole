'''
	[문제] 
		45와 60, 75의 최대공약수를 구하시오.
	[정답]
		15
'''
answer = 0

i = 1
while i <= 45:
    if 45 % i == 0 and 60 % i == 0 and 75 % i == 0:
        answer = i
    i += 1

print(answer)
