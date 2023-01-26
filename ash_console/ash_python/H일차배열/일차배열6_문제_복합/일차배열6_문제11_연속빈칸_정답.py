'''
	[문제]
		철수네 공장의 창고를 아래 a리스트로 표현하였다.
		1은 물건이 차 있는 상황이고 0은 비어있는 상황이다.
		랜덤(1~5)으로 물건 크기를 입력받고 창고에 저장 후 출력하시오.
		저장할 수 없으면 "창고 부족"이라고 출력하시오.
		단, 물건은 앞에서부터 채워나간다.
	[예]
		r = 3
  		[0,1,0,0,0,1,0,0] : [0,1,1,1,1,1,0,0]
    
		r = 4
		[0,1,0,0,0,1,0,0]  : "창고부족"
'''
import random

a = [0,1,0,0,0,1,0,0]

size = random.randint(1, 5)
print("size =", size)

start = 0
end = 0
for i in range(len(a)):
	if a[i] == 1:
		if start == 0:
			start = i
		else:
			end = i
print("start =", start)
print("end =", end)
count = end - start - 1
print("빈 공간 =", count)

if count >= size:
	temp = size
	i = start + 1
	while temp != 0:
		a[i] = 1
		i += 1
		temp -= 1
	print(a)
else:
	print("창고 부족")
