'''
	[문제]
		철수는 수학 시험을 보았다. 
		철수는 실수로 답을 한 칸씩 밀려 적었다. 
		철수가 원래대로 마킹했더라면 몇 점인지 구하시오.
		한 문제당 20점이다. 

		정답 = [ 1,4,3,3,2 ]		
		철수가 제출한 답안지 =  [0,1,4,3,2]
		원래 제출하고 싶었던 답안지 = [1,4,3,2,0]
	[정답]
		60점		
'''
'''
밀린답 = 밀어넣기


'''

정답 = [1,4,3,3,2]
밀린답 = [0,1,4,3,2]
점수 = 20

# [1118]
# temp = 밀린답[0]
# idx = 1 
# for i in range(len(밀린답) - 1) :

# 	밀린답[i] = 밀린답[idx]

# 	if idx == len(밀린답) - 1 :
# 		밀린답[idx] = temp
	
# 	idx += 1 
# print(밀린답)

# total = 0 
# count = 0 
# for i in range(len(정답)) :
# 	if 정답[i] == 밀린답[i] :
# 		count += 1 
	
# total = count * 20
# print("total =", total)

# [1116]
# idx = 1 
# for i in range(len(밀린답) - 1) :
# 	밀린답[i] = 밀린답[idx]
# 	idx += 1 

# 밀린답[len(밀린답) - 1] = 0 

# print(밀린답)

# count = 0
# for i in range(len(정답)) :
# 	if 정답[i] == 밀린답[i] :
# 		count += 1
# 점수 = count * 20
# print(점수) 

# [1차]
# idx = 1 
# temp = 밀린답[0]
# for i in range(len(밀린답) - 1) :
# 	밀린답[i] = 밀린답[idx]
# 	# print(밀린답)
# 	idx += 1 
# 밀린답[(len(밀린답) - 1)] = temp
# print(밀린답)

# count = 0 
# for i in range(len(정답) - 1) :
# 	if 정답[i] == 밀린답[i] :
# 		count += 1 
# 		# print(count)

# total = count * 점수
# print(total)