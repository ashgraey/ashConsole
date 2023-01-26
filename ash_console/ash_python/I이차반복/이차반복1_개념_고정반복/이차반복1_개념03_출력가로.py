'''
	[문제]
		랜덤(3~6)숫자 하나를 저장하고 그 숫자만큼 아래와 같은 규칙 출력하시오.
		단, 일차 반복문과 이차 반복문으로 출력하시오.
 	[예시1]
		r = 6
	[출력1]
		1 2 3
		4 5 6
		7 8 9
	    10 11 12
        13 14 15
	    16 17 18
 	[예시2]
		r = 3
	[출력2]
		1 2 3
		4 5 6
		7 8 9	
'''
import random

sero = random.randint(3, 6)
print("sero =", sero)

# 정답
# for i in range(r):
#     a = i * 3 + 1
#     print(a + 0, a + 1 , a + 2)

# print("----")
# for i in range(r):
#     a = i * 3 + 1
#     for j in range(3):
#         print(a + j, end=" ")
#     print()

# 1123
# num = 1
# for i in range(sero) :
# 	for j in range(3) :
# 		print(num, end = " ")
# 		num += 1
# 	print()

# # 1116
# for i in range(sero) :
# 	for j in range(3) :
# 		j += 1
# 		print(i, end = "")
# 	i += 1 
# 	print()




