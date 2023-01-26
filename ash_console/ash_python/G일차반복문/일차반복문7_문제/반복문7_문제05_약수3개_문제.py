'''
	[문제]
		어떤 수를 1부터 자기 숫자까지 나눠서 나눠지는 수를 약수라고 한다. 
		랜덤으로 1~100을 저장 후, 
		약수가 3개이면 "정답"을 
		아니면 "오답"을 출력하시오.
'''

import random

r = random.randint(1, 100)
print("랜덤숫자 =", r)

count = 0
i = 1 
while i <= r :
	
	if r % i == 0 :
		print(i, end = " ")
		count += 1
	i += 1 
print()
print("약수의 개수 =", count)

if count == 3 :
	print("정답")

else :
	print("오답") 

# [풀이]
# num = random.randint(1, 100)
# print(num)
# count = 0

# i = 1
# while i <= num :
# 	if num % i == 0 : 
# 		print(i, end = " ")
# 		count += 1 
# 	i += 1 

# print()
# if count == 3: 
# 	print("정답")
# else : 
# 	print("오답")