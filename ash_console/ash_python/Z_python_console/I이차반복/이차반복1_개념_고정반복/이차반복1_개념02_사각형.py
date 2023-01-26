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