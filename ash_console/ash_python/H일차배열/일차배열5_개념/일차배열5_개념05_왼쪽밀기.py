'''
	[문제]
		a리스트의 값 중 0을 제외한 모든 값을 왼쪽으로 모으시오.
 	[결과]
 		a = [2,3,4,5,0,0,0,0,0,0];
'''
'''
if a[1] == 0 :
	idx += 1
print(a[idx])
'''


a = [0,0,2,0,3,0,4,0,0,5]

[1115]
idx = 0
for i in range(len(a)) :
	if a[i] != 0 :
		a[idx] = a[i]
		a[i] = 0
		idx += 1 
		
print(a)

# [2차]
# for i in range(len(a)) :
# 	# 조건정리 :
# 	# a[i]의 값이 0이 아닌걸 찾고
# 	# 값이 0이 아니라면 a[idx] == a[0] 초기값
# 	# 부터 값을 대입시킨다 
# 	# 대입이 끝난후에는 idx값을 1씩 증가시켜 다음 인덱스 위치에 또 다시 값을 넣는걸 반복한다.

# 	if a[i] != 0 :
# 		a[idx] = a[i]
# 		a[i] = 0

# 		idx += 1
# print(a)	

# [1차]
# index  = 0
# for i in range(len(a)):
# 	if a[i] != 0:
# 		a[index] = a[i]
# 		a[i] = 0

# 		index += 1

# print(a)