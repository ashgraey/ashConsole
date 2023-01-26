'''
	[문제]
		a리스트에 랜덤(0~9) 사이의 랜덤 값을 4개 저장한 후 출력한다. 
		리스트 안의 값들이 모두 짝수면 True를 출력하고,
		하나라도 짝수가 아니면 False를 출력한다.
		단, 0은 짝수이다.
		[예시] 
			[4, 6, 2, 0] True
			[5, 2, 0, 4] False
'''
'''
조건1 : a리스트에 랜덤(0 ~ 9)사이의 랜덤값 4개를 저장 후 출력 
조건2 : 리스트 안의 값들이 모두 짝수면 true
조건3 : 하나라도 짝수가 아니면 false
조건4 : 0은 짝수이다.
'''
import random

a = []

# [1115]
count = 0
for i in range(4) :
	a.append(random.randint(0,9))
	# a.append(4)

	if a[i] % 2 == 0 :
		count += 1 
	else : 
		count += 0

	if count == 4 :
		result = True
	else :
		result = False
	
print(count)
print(a, result)


# [2차]
# for i in range(4) :
# 	# a.append(random.randint(0,9))
# 	a.append(2)
# print(a)

# # count변수를 활용하여 짝수일때만 카운트가 1씩 증가
# # 카운트의 값이 a배열의 길이의 값과 같다면 true
# # 그렇지않다면 false를 출력
# # true와 false를 판명하기위한 count조건
# count = 0
# for i in range(len(a)) : 
# 	if a[i] % 2 == 0 :
# 		# print("true")
# 		count += 1 

# # 반복문으 빠져나와 카운트 값을 이용하여 true와 false를 출력
# # count조건
# if count == len(a) : 
# 	print("true")
# else :
# 	print("false")

# [1차]
# for i in range(4):
# 	r = random.randint(0, 9)
# 	a.append(r)
# print(a)
    
# count = 0
# for i in range(len(a)):
#     if a[i] % 2 == 0:
#     	count += 1
		
# if count == len(a):
#     print(True)
# else:
#     print(False)
