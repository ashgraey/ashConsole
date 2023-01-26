'''
	[문제]
		a리스트는 학생 번호와 점수 한 세트를 이루고 있다.		
		0 ~ 7 사이의 랜덤 숫자를 저장하고,
		해당 위치의 학생 번호와 그 점수를 삭제하시오.
	[예시]
		
'''
'''
조건1 = 랜덤숫자(0~7)을 생성 
조건2 : 점수 위치값, 번호 위치값(점수 위치값 - 1)


'''
import random

a = [1001, 40, 1002, 60, 1003, 65, 1004, 70]

# [1118]
# idx = random.randint(0, 7)
# print("r =", idx)

# if idx % 2 == 0 :
# 	del(a[idx])
# 	del(a[idx])
# else :
# 	del(a[idx])
# 	del(a[idx - 1])
# print(a)

# [1116]
# r = random.randint(0, 7)
# # r = 1 
# print("r =", r)

# if r % 2 == 1 :
# 	a.remove(a[r])	
# 	a.remove(a[r - 1])
# else :
# 	a.remove(a[r])
# 	a.remove(a[r])

# print(a)

# [1차]
# idx = random.randint(0, len(a) - 1)
# print("idx =", idx )

# if idx % 2 == 0:
# 	a.remove(a[idx])
# 	a.remove(a[idx])

# else : 
# 	a.remove(a[idx])
# 	a.remove(a[idx - 1])

# print(a)