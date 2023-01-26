'''
	[문제]
		[1] 랜덤숫자 1~9 다섯 개를 리스트에 추가한다.
		[2] 그 숫자 중 홀수만 하나로 모아서 숫자로 만든다. (더하기가 아니다.)
		[3] 그 숫자의 두 배를 출력한다. 
	
	[예시] 
		2 5 3 4 6 이 랜덤으로 저장되었다고 가정했을 때,
		홀수는 5, 3 이므로 합치면 53이 된다. 
		53의 두 배는 106이다. 
'''
import random

a = []
temp = []

# [1116]
# 출력은 되지만 코드가 엉망임
# for i in range(5) :
# 	a.append(random.randint(1,9))

# 	if a[i] % 2 == 1 :
# 		temp.append(a[i])

# print(a)
# print(temp)

# size = len(temp) - 1 
# idx = 0
# i = 0 
# while idx < len(temp):
# 	if i < size  :
# 		temp[idx] *= 10
# 		i += 1
# 	else :
# 		idx += 1
# 		i = 0
# 		size -= 1 

# total = 0 
# for i in range(len(temp)) :
# 	total += temp[i]

# # print(temp)
# print(total)
# print(total * 2)	

# [1차]
# for i in range(5) :
# 	r = random.randint(1, 9)
# 	a.append(r)
	
# 	if a[i] % 2 == 1 :
# 		temp.append(a[i])
	
# print(a)
# print(temp)

# size = len(temp)

# # 단위를 만드는것 
# # temp의 마지막 인덱스 값 * 10 이랑 같은거임
# multiply = 1
# for i in range(size - 1) :
# 	multiply *= 10
# # print(multiply)

# number = 0 
# for i in range(size) :
# 	number += temp[i] * multiply
# 	# 가장 큰 자리부터 몫을 구해서 구한다.
# 	# 자릿수를 나누어서 number값에 더한다.
# 	multiply //= 10 
# print(number)