'''
	[문제] 
		철수는 편의점에서 아르바이트를 하고 있다. 
		오늘 장사가 잘돼서 라면이 많이 판매되었다.
		라면 진열장에 라면들이 전부 채워질 수 있도록 라면을 채워보자.
		
		라면 진열장은 한 칸에 최대 5개씩 진열할 수 있으며,
		재고는 6개 밖에 없고 앞에서부터 순차적으로 채워 넣는다. 
		재고를 다 채웠을 때 라면 진열장의 모습을 출력하시오.
	[정답] 
		list = [3,5,2,1,2]
		count = 6
  
		1번은 3이므로 2개를 추가해 ==> -2
		2번은 5이므로 0개를 추가해 ==> -0
		3번은 2이므로 3개를 추가해 ==> -3
		4번은 1이므로 4개를 추가해야되지만 재고가 1개밖에없어서 -1	
		최종으론 [5,5,5,2,2] 가된다. 
'''
'''
조건1 = 리스트의 값과 5를 


'''
list = [3, 5, 2, 1, 2]
count = 6
plus = 0 

# [1118]
# for i in range(len(list)) :
# 	if list[i] > 0 : 
# 		plus = 5 - list[i]
# 		# list[i] += plus
# 		# count -= plus
# 		if count > plus :
# 			list[i] += plus
# 			count -= plus
# 		else :
# 			list[i] += count
# 			count = 0 
# print(list)
# print(count)

# [1116]
# 필요개수 = 0
# for i in range(len(list)) :
# 	if count > 0 and list[i] < 5 :
# 		필요개수 = 5 - list[i]
# 		if count - 필요개수 > 0 :
# 			list[i] += 필요개수
# 			count -= 필요개수
# 		else :
# 			list[i] += count
# 			count = 0

# print(list)
# print(count)

# [1차]
# count = 6
# full = 5
# 필요개수 = 0 
# for i in range(len(list)):
# 	if list[i] <= 5 and count > 0 :
# 		필요개수 = full - list[i]
		
# 		if count - 필요개수 > 0 :
# 			list[i] += 필요개수
# 			count -= 필요개수
		
# 		else :
# 			list[i] += count
# 			count = 0 
			
# print(list)
# print(count)