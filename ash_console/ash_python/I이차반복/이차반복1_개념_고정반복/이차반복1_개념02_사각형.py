'''
	[사각형그리기]
		랜덤으로 세로(3~6)을 저장하고, 각 길이에 맞게 사각형을 그려보시오. 
		단 가로는 항상 5이다.
		일차원 반복문과 이차원 반복문으로 그려보시오.
	[예시] 
		세로 : 3
  
		#####
		#####
		#####
'''

import random

# 정답
sero = random.randint(3, 6)
print("세로 :", sero)

print("--------------------")
for i in range(sero):
    print("#####")
	
print("--------------------")
for i in range(sero):
    for j in range(5):
        print("#", end="")
    print()

# [1123]
# sero = random.randint(3, 6)
# print("sero =", sero)

# for i in range(sero) :
# 	for j in range(5) :
# 		print("#", end = "")
# 	print()

# [1116]
# garo = 5
# # sero = random.randint(3, 6)
# sero = 3
# # print(sero)
# for i in range(sero) :
# 	print('#####')

# 	# if i % 5 == 0 :
# 	# 	print() 
# print()
# print("----- 이차원 반복문 ------")
# for i in range(sero) :
# 	print()
# 	for j in range(garo) :
# 		print('#', end = " ")
