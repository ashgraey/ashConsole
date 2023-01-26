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
	[문제2] 
		평균이 60점 이상이면 합격이다.
		합격생들 번호, 이름, 평균점수를 출력하시오.
	[정답2]
		1003 김민정 64.5
		1005 오만석 64.5
'''
print("[문제2]")
# 정답
# i = 1
# while i < len(student):
# 	total = student[i][3] + student[i][4]
# 	avg = total / 2
# 	if avg >= 60:
# 		print(student[i][0], student[i][1], avg)
# 	i += 1

# i = 1 
# while i < len(student) :
# 	total = (student[i][-2] + student[i][-1])
# 	avg = total / 2
# 	# print(avg)
# 	if avg >= 60 : 
# 		print("번호 : ", student[i][0], "이름 : ", student[i][1], "점수 : ", avg)
	
# 	i += 1 

# 0126

for i in range(1, len(student)) :
	avg = (student[i][3] + student[i][4]) / 2
	# print(avg)
	if avg >= 60 :
		print(student[i][0], student[i][1], avg)
	
