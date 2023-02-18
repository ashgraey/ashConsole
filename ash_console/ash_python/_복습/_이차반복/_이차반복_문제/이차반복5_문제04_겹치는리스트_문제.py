'''
	[문제]
		a리스트를 순차적으로 검사한다.
		b리스트의 값들이 a리스트의 값들과 완벽히 겹치는지 검사하시오.
		겹치면 "o" , 안겹치면 "x"를 출력하시오.

	[예시1] 
		b = [6,1,8] : [1,3,3,6,5,(6,1,8),9] 완벽히 겹친다.
	[예시2]
		b =[6,3] : [1,3,3,6,5,6,1,8,9] 겹치는 부분이 없다.
	[예시3]
		b =[3,6,5,6] : [1,3,(3,6,5,6),1,8,9] 완벽히 겹친다.
'''
a = [1,3,3,6,5,6,1,8,9]
b = [6,1,8]
# b = [6,3]
# b = [3,6,5,6]

check = False
# 1124
count = 0
for i in range(len(a) - len(b) + 1) :

	for j in range(len(b)) :
		if a[j + i] == b[j] :
			count += 1 
		else : 
			count = 0

	if count == 3 :
		check = True 
		break

if check :
	print("o")
else :
	print("x")
	

# 1121
# 연속으로 겹치는가?
# 뭘 의도한걸까?
# i = 0
# while i < len(a) :
	
# 	count = 0
# 	check = False
# 	j = 0 
# 	while j < len(b) :
# 		if a[i] == b[j] :
# 			check = True 
# 			break
# 		j += 1 
	
# 	if check == True :
# 		count += 1  

# 	if count >= 2 :
# 		print("완벽히 겹친다.")

# 	i += 1 
