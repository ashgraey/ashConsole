'''
	[문제]
		랜덤으로 리스트의 값을 교환하고, 출력하시오.  
		[예]
			교환 전  [10,20,30,40,50,60,70,80] : 30과 40을 교환
			교환 후  [10,20,40,30,50,60,70,80]
'''

import random

a =[10, 20, 30, 40, 50, 60, 70, 80]
print("교환 전 =", a)

# [1115]
# idx1 = random.randint(0, len(a) - 1)
# idx2 = random.randint(0, len(a) - 1)
# print("idx1 = ", idx1)
# print("idx2 = ", idx2)

# temp = a[idx1]
# a[idx1] = a[idx2]
# a[idx2] = temp

# print("교환 후 =", a)
# print(index)

# [1차]
# idx1 = random.randint(0, len(a) - 1)
# idx2 = random.randint(0, len(a) - 1)
# print(idx1, idx2)

# # 값을 교환하기 위해서는 temp라는 변수 안에 idx1의 값을 옮겨놓아야한다.
# temp = a[idx1]
# a[idx1] = a[idx2]
# a[idx2] = temp
# print("교환 후 =", a)
