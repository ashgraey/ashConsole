'''
	[문제]
		숫자 5개를 랜덤으로 뽑고, 
		랜덤으로 더하기나 빼기를 한 총합을 구하려고 한다.
  
		변수 r 은 숫자를 표현하며, 변수 op는 기호를 표현한다.
		변수 r 에 랜덤숫자(1~9)를 5개를 뽑는다. 
		또 op변수는 더하기나 빼기를 뜻하는 랜덤숫자(0, 1)도 4개를 뽑는다. 
		(기호는 숫자보다 1개 적어야 한다.)
		op 변수의 0은 더하기고 1은 빼기이다. 
		
		[예시]
			r 은 3, 6, 5, 3 , 1이 나왔다고 가정하고,
			op 는 0, 1, 0, 1이 나왔다고 하면, 
	
			3 + 6 - 5 + 3 - 1 이된다. 
'''
# [3차 - 1110]
import random

# 첫번째 랜덤값을 따로 출력해서 total 변수에 저장
r = random.randint(1, 9)
# print(r)
total = r 
i = 0
# 반복의 횟수를 하나 낮추면 
# 랜덤값 하나가 출력되지 않음
# 총 출력되어야하는 랜덤값이 4개여야하기때문
while i < 5 :
    
    print(r, end = " ")
    # 반복의 횟수는 5회이지만 실질적으로 출력되는 값은 4회 조건에서 이루어짐
    if i < 4 :
        r = random.randint(1, 9)
        op = random.randint(0,1)
        # print(end =" + ")
        if op == 0 : 
            print(end = " + ")
            total += r
        else :
            print(end = " - ")
            total -= r
    i += 1 

print(" =",total)


# [2차]
# import random

# r = random.randint(1, 9)

# total = r
# i = 0
# while i < 5:
#     print(r, end=" ")

#     op = random.randint(0, 1)
#     r = random.randint(1, 9)
#     # print(op, end = " ")

#     if i < 4:
#         if op == 0:
#             print("+", end=" ")
#             total += r
#         if op == 1:
#             total -= r
#             print("-", end=" ")
#     i += 1
    
# print("=", total)

# [1차]
# r = random.randint(1, 9)
# op = 0

# i = 0 
# total = r 
# while i < 5 :
# 	print(r, end = " ")

# 	op = random.randint(0, 1)
# 	r = random.randint(1, 9)

# 	if i < 4 : 
# 		if op == 0 : 
# 			print("+", end = " ")
# 			total += r
# 		if op == 1 : 
# 			total -= r
# 			print("-", end = " ")
# 	i += 1

# print("=", total)

# while i < 4 : 
# 	op = random.randint(0, 1)
# 	print(op, end =" ")
# 	i += 1 
