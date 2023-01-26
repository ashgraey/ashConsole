'''
	[문제]
		랜덤으로 10000 ~ 99999 사이의 랜덤숫자를 저장하고 
		다음 규칙에 따라 결과를 출력하시오.
		랜덤숫자를 두 개로 분리하는데
		한 자리씩 늘리면서 분리한다. 
		각 분리한 숫자의 합을 출력한다.
	[예시]
		r = 34567
	[결과]
		3 + 4567
		34 + 567
		345 + 67
		3456 + 7
'''
import random
# 0113
r = random.randint(10000, 99999)
print("r : ",r)

# 자릿수
tempR = r
cnt = 0 
while True :
	tempR //= 10
	cnt += 1 

	if tempR == 0 : 
		break

print("자릿수 : ", cnt)

# 끊어야 할 단위
cipher = 1
for i in range(cnt - 1) :
	cipher *= 10
print("단위 : ", cipher)

# 출력
for i in range(cnt - 1) :
	fir = r // cipher
	last = r % cipher
	total = fir + last
	print(fir, "+", last, "=", total)

	cipher //= 10


# 1213
# r = random.randint(10000, 99999)
# print("random : ", r)

# # 자릿수
# temp = r 
# cnt = 0 
# while True :
# 	temp //= 10
# 	cnt += 1 
# 	if temp == 0 :
# 		break
# # print(cnt)

# cip = 1
# for i in range(cnt - 1) :
# 	cip *= 10 

# print(cip)

	
# for i in range(cnt - 1) :
# 	temp = r
# 	total = 0
# 	for j in range(1) :
# 		share = temp // cip
# 		rest = temp % cip
# 	total = share + rest 
# 	cip //= 10

# 	print(share," + ", rest ," =", total)