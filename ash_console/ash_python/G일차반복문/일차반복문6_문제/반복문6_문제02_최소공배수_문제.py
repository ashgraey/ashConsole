'''
[문제] 
	45와 60, 75의 최소공배수를 구하시오.
[정답]
	900
'''

i = 1 
min = 0
run = 1
while run == 1 :
	if i % 45 == 0 and i % 60 == 0 and i % 75 == 0 : 
		min = i
		print(i)
		run = 0

	i += 1

print(min)

# [정답]
# answer = 0

# i = 1

# run = 1
# while run == 1:
# 	if i % 45 == 0 and i % 60 == 0 and i % 75 == 0:
# 		answer = i
# 		run = 0
# 	i += 1

# print(answer)

