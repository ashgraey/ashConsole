'''
	[문제]	
		아래 a 리스트는 한 줄 리스트이지만 
		아래와 같이 사각형으로 놓였다고 했을 때,  
		[1] a 리스트의 가로 합은 garo 리스트에 저장하시오.
		[2] a 리스트의 세로 합은 sero 리스트에 저장하시오.
	[정답]
		garo = [10, 26, 42]
		sero = [15, 18, 21, 24]
'''	

a = [1, 2, 3, 4,
     5, 6, 7, 8,
     9, 10,11,12]

garo = [0, 0, 0]
sero = [0, 0, 0, 0]

# 가로의 합 구하는 식
garoIndex = 0
for i in range(len(a)):
	garo[garoIndex] += a[i]
	# 	garo[0] = garo[0] + a[0]
	#   garo[0] = a[0]+ a[1]
	#   garo[0] = a[0] + a[1] + a[2]
	# 	garo[0] = a[0] + a[1] + a[2] +a[3]
	# 	garo[1] = garo[1] + a[4] ...
	#  	garo[2] = garo[2] + a[7]
	if i % 4 == 3:
		garoIndex += 1
print("garo =", garo)

seroIndex = 0
for i in range(len(a)):
	sero[seroIndex] += a[i]
	# sero[0] = sero[0] + a[0]
	# sero[1] = sero[1] + a[1]
	# sero[2] = sero[2] + a[2]
	# sero[3] = sero[3] + a[3]
	# sero[0] = a[0] + a[4]...
	# sero[1] = a[1] + a[5]...
	# .....
	seroIndex += 1
	if i % 4 == 3:
		seroIndex = 0
print("sero =", sero)	