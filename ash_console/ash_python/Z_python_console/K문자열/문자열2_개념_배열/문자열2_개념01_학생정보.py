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
	[문제1] 
		여학생들 점수 총합과 남학생들의 점수 총합을 비교하고
		점수가 더 큰 쪽을 출력하시오.
	[정답1]
		333
'''
print("[문제1]")
total = [0, 0]

max = 0
i = 1
while i < len(student):
	if student[i][2] == "남":
		total[0] += student[i][3] + student[i][4]
		if max < total[0]:
			max = total[0]
	else:
		total[1] += student[i][3] + student[i][4]
		if max < total[1]:
			max = total[1]
	i += 1
print(total)
print(max)
