'''
	[문제]
		a리스트에 value 의 값을 추가 하거나 삭제 한다. 
		order의 값이 1이면 value값을 추가한다.
		order의 값이 2이면 value값을 삭제한다.
		단, 추가할 값이 a리스트에 이미 추가되어있으면 "중복" 출력
		단, 삭제할 값이 a리스트에 없으면 "삭제 불가" 출력 
		
		order = 1 , value = 10 , a = [10]
		order = 2 , value = 20 , a = [10] , "삭제 불가"
		order = 1 , value = 30 , a = [10, 30] 
		order = 2 , value = 10 , a = [30] 
		order = 1 , value = 30 , a = [30] , "중복"
		order = 2 , value = 30 , a = [] 
'''
a = []
order = [1,2,1,2,1,2]
value = [10,20,30,10,30,30]

for i in range(len(order)):
	print("order =", order[i], "value =", value[i], end=", ")
	if order[i] == 1:
		check = False

		for j in range(len(a)):
			if value[i] == a[j]:
				check = True
				break
		if check == False:
			a.append(value[i])
			print(a)
		else:
			print(a, "중복")
	else:
		check = False

		for j in range(len(a)):
			if value[i] == a[j]:
				check = True
				break
		if check == False:
			print(a, "삭제 불가")
		else:
			a.remove(value[i])
			print(a)