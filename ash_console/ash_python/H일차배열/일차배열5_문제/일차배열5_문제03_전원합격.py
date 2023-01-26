'''
	[문제]
		a리스트에 랜덤(0 ~ 100) 사이의 랜덤값을 4개 저장한후 출력한다. 
		배열의 값은 학생들의 성적이다. 
		60점이상이면 합격이다. 
  		전원합격시는 "상품" 을 출력. 
		전원탈락시는 "벌칙" 를 출력.
		그외는 리스트만 출력.
		
		[예시] 
			[67, 100, 98, 97] "상품"
			[53, 25, 12, 41] "벌칙"
'''
import random
a = []
for i in range(4):
    r = random.randint(0, 100)
    a.append(r)

print(a)
c1 = 0
c2 = 0
for i in range(len(a)):
	if a[i] >= 60:
		c1 += 1
	if a[i] < 60 :
		c2 += 1
if c1 == len(a):
	print("상품")
elif c2 == len(a):
    print("벌칙")
		



