'''
	[문제1]
		a리스트의 값들을 한 칸씩 앞으로 당기고 출력하시오.
	[정답1]
		a = [10,20,30,40,50,0]
  
	[문제2]
		b리스트의 값들을 한 칸씩 뒤로 밀고 출력하시오.
	[정답2]
		b =  [0,10,20,30,40,50]
'''

# [문제1]
# 인덱스의 길이 - 1 = 리스트의 끝자리
# 리스트의 끝자리를 맨 앞으로 출력해야기 때문에
# len(a) - 1 리스트의 끝자리 -1까지 반복한다.
# i + 1 을 사용하여 0~4까지 인덱스를 하나씩 밀어준다.
# 반복문을 탈출하여 마지막 인덱스 5번에 인덱스 0번의 값인 0을 직접 넣어준다.
# 마지막으로 a를 출력하여 값을 확인한다.

# [1115]
# # [문제1]
# a = [0, 10, 20, 30, 40, 50]

# for i in range(len(a) - 1):
# 	a[i] = a[i + 1]
# a[len(a) - 1] = 0

# print(a)
# print()

# # [문제2]
# b =  [10, 20, 30, 40, 50, 0]

# index = len(b) - 1
# for i in range(len(b)):
# 	b[index] = b[index - 1]
# 	index -= 1
# b[0] = 0
# print(b)

# [2차]
# 문제1
# a = [0, 10, 20, 30, 40, 50]
# print(a)
# for i in range(len(a) - 1 ) :
# 	a[i] = a[i + 1]
# # print(a)
# a[len(a) - 1] = 0
# print(a)

# 문제2
# b =  [0,10,20,30,40,50]
# print(b)
# idx = len(b) - 1

# for i in range(len(b) - 1) :
# 	b[idx] = b[idx - 1]
# 	idx -= 1
# b[0] = 50

# print(b)

# [1차]
#[문제1]
# a = [0, 10, 20, 30, 40, 50]
# for i in range(len(a) - 1) : 
# 	# print(a[i], end = " ")
# 	a[i] = a[i + 1] 
# 	# print(a[i])

# a[len(a) - 1] = 0
# # print()
# print(a)


# [문제2]
# b =  [10, 20, 30, 40, 50, 0]
# for i in range(len(b) - 1) : 
# 	b[i] = b[i + 1]
# b[len(b) - 1] = 10
# print(b)

# b =  [10, 20, 30, 40, 50, 0]
# #
# #  b[5] = b[4] 
# #  b[4] = b[3]
# #  b[3] = b[2]
# #  b[2] = b[1]
# #  b[1] = b[0]
# #  b[0]이 비어있기 때문에 0을 직접 대입시켜준다. 
# index = len(b) - 1
# for i in range(len(b) - 1):
# 	b[index] = b[index - 1]
# 	index -= 1
# b[0] = 0
# print("b =", b)





