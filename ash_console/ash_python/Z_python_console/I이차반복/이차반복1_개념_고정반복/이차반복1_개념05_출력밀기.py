'''
	[문제]
		랜덤(3~6)숫자 하나를 저장하고 그 숫자만큼 아래와 같이 출력하시오.
		단, 아래 일차 반복문과 이차 반복문으로 출력하시오.
 	[예시1]
		r = 6
	[출력1]
		1 2 3
		2 3 4
		3 4 5
		4 5 6
 	[예시2]
		r = 4
	[출력2]
		1 2 3
		2 3 4		
'''
import random

r = random.randint(3, 6)
print("r : " , r)
for i in range(r - 2) :
    a = i + 1
    print(a + 0 ,  a + 1 , a + 2)
print("===============================")

print("r : " , r)
for i in range(r - 2) :
    num = i + 1
    for j in range(3) : 
        print(num + j , end=" ")
    print()

