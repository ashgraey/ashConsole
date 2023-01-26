student = [
		["번호",  "이름", "성별", "국어", "수학"],
		[1001, 	"이만수",  "남",     10,     20],
		[1002,  "이영희",  "여",     70,     30],
		[1003,  "김민정",  "여",     64,     65],
		[1004,  "이철민",  "남",     13,     87],
		[1005,  "오만석",  "남",     49,     80],
		[1005,  "최이슬",  "여",     14,     90]
	]

'''
	[문제4] 
		1등의 번호, 이름을 출력하시오.
		만약 여러 명이면 전부 출력하시오.
	[정답4]
		1003 김민정
		1005 오만석
'''
print("[문제4]")
# 정답
# max = 0
# i = 1
# while i < len(student):
# 	total = student[i][3] + student[i][4]
# 	if max < total:
# 		max = total
# 	i += 1

# i = 1
# while i < len(student):
# 	total = student[i][3] + student[i][4]
# 	if max == total:
# 		print(student[i][0], student[i][1])
# 	i += 1

# 1214
# 1등 찾기
# max = 0 
# i = 1 
# while i < len(student) :
# 	total = student[i][-2] + student[i][-1] 
	
# 	if max < total :
# 		max = total
# 		maxIdx = i 
# 	i += 1 

# # print(student[maxIdx][0], student[maxIdx][1])

# # 중복되는 1등 찾기
# i = 1 
# while i < len(student) :
# 	total = student[i][-2] + student[i][-1]

# 	if total == max :
# 		totIdx = i
# 		print(student[totIdx][0], student[totIdx][1])
	
# 	i += 1

# 0126
# [문제4] 
# 1등의 번호, 이름을 출력하시오.
# 만약 여러 명이면 전부 출력하시오.

max = 0
for i in range(1, len(student)) :
	total = student[i][-2] + student[i][-1]
	# print(total)
	
	if max < total :
		max = total
print("max : ", max)

for i in range(1, len(student)) :
	total = student[i][-2] + student[i][-1]
	# print(total)
	
	if max == total :
		print(student[i][0], student[i][1])

	
