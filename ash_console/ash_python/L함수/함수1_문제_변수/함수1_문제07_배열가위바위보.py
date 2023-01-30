# <script>

# /*
# 	 	[테스트]
# 	 		철수와 민수는 가위바위보를 6회 하였다. 
# 	 		가위(0) , 바위(1) , 보(2) 를 뜻한다. 
# 	 		아래 배열은 각각 가위바위보를 낸 기록을 저장한것이다. 
	 		
# 	 		철수와 민수는 계단 50번째 부터 게임을 시작하였다. 
# 	 		철수와 민수는 게임을 모두 끝마치고 어디있을까?
# 	 		[규칙]
# 	 			이기면 5칸 올라간다.
# 	 			비기면 1칸 올라간다.
# 	 			지면 3칸 내려간다. 

#                  int 철수list[] = {0,1,2,2,1,0};
# 				int 민수list[] = {2,1,1,2,0,1};
# 				int 철수위치 = 50;
# 				int 민수위치 = 50;
# 	 */

# </script>

#  0 가위, 1 바위, 2 보
def rpsGame(a, b, aPosition, bPosition) : 
	print("철수위치 : ", aPosition, "민수위치 : ", bPosition)
	
	for i in range(len(a)) :
		if a[i] == b[i] :
			aPosition += 1 
			bPosition += 1
			print("비겼다")
		
		elif a[i] == 0 and b[i] == 2 :
			aPosition += 5
			bPosition -= 3
			print("철수 승")
			
		elif a[i] == 1 and b[i] == 0 :
			aPosition += 5
			bPosition -= 3
			print("철수 승")
		
		elif a[i] == 2 and b[i] == 1 :
			aPosition += 5
			bPosition -= 3
			print("철수 승")

		else :
			aPosition -= 3
			bPosition += 5
			print("민수 승")
	
	print("철수위치 : ", aPosition, "민수위치 : ", bPosition)


# 0 가위 1 바위 2 보
철수 = [0,1,2,2,1,0]
민수 = [2,1,1,2,0,1]
철수위치 = 50
민수위치 = 50
rpsGame(철수, 민수, 철수위치, 민수위치)

