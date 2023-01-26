'''
	[문제]
		아래 배열은 철수와 민수의 가위바위보 데이터이다. 
		왼쪽이 철수의 데이터이고 오른쪽이 민수의 데이터이다.
		
		가위, 바위, 보
		
		민수와 철수는 계단 50번째에서 게임을 시작했으며, 
		아래의 규칙을따른다.
		철수는 게임 종료 후 몇번째 계단에 있을지 구하시오.
	[규칙]
		이기면 계단 5증가
		비기면 계단 1증가
		지면 계단 3감소 			
	[정답]
		56
'''
arr = [
		["바위","가위"],
		["바위",  "보"],
		["보",  "가위"],
		["가위","가위"],
		["바위","바위"],
		["보",  "바위"]
	]
pos = 50
# 정답
# for i in range(len(arr)):
# 	if arr[i][0] == arr[i][1]:
# 		pos += 1
# 		print("비겼다!")
# 	elif arr[i][0] == "가위" and arr[i][1] == "보":
# 		pos += 5
# 		print("철수가 이겼다!")
# 	elif arr[i][0] == "바위" and arr[i][1] == "가위":
# 		pos += 5
# 		print("철수가 이겼다!")
# 	elif arr[i][0] == "보" and arr[i][1] == "바위":
# 		pos += 5
# 		print("철수가 이겼다!")
# 	else:
# 		pos -= 3
# 		print("철수가 졌다!")

# print("철수의 현재 위치 =", pos)

# 1214
for i in range(len(arr)) :
	if arr[i][0] == arr[i][1] :
		print("비겼다")
		pos += 1 
	
	elif arr[i][0] == "가위" and arr[i][1] == "보" :
		print("이겼다")
		pos += 5
	
	elif arr[i][0] == "바위" and arr[i][1] == "가위" :
		print("이겼다")
		pos += 5
	
	elif arr[i][0] == "보" and arr[i][1] == "바위" :
		print("이겼다")
		pos += 5
	
	else :
		print("졌다")
		pos -= 3

	print(pos)
	

