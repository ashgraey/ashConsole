'''
	[문제]
		아래와 같이 출력하시오.
'''
'''
	[문제1]
		11112
		11122
		11222
		12222
'''
print("[문제1]")
# 1125
# for i in range(4) :
# 	for j in range(4 - i) :
# 		print("1", end = "")
# 	# print()
# 	for j in range(i + 1) :
# 		print("2", end = "")
# 	print()

# 1216
for i in range(4) :

	for j in range(4 - i) :
		print("1", end = "")
	# print()
	for j in range(i + 1) :
		print("2", end = "")
	print()

'''
	[문제2]
		12222
		11222
		11122
		11112
'''
print("[문제2]")
#1125
# for i in range(4) :
# 	for j in range(i + 1) :
# 		print("1", end = "")
# 	for j in range(4 - i) :
# 		print("2", end = "")
# 	print()

# 1216
# for i in range(4) :

# 	for j in range(i + 1) :
# 		print("1", end = "")
# 	# print()

# 	for j in range(4 - i) :
# 		print("2", end = "")
# 	print()

'''
	[문제3]
		11211
		12221	
		22222
'''
print("[문제3]")
# 1125
# num = 1 
# for i in range(3) :
# 	for j in range(2 - i) :
# 		print("1", end = "")
# 	for j in range(num) :
# 		print("2", end = "")
# 	for j in range(2 - i) :
# 		print("1", end = "") 
# 	print()
# 	num += 2

# 1216
# num = 1
# for i in range(3) :

# 	for j in range(2 - i) :
# 		print("1", end = "")
	
# 	for j in range(num) :
# 		print("2", end = "")
	
# 	for j in range(2 - i) :
# 		print("1", end = "")
	
# 	print()
# 	num += 2

'''
	[문제4]
		  2
		 222
		22222
'''
print("[문제4]")
# 1125
# num = 1 
# for i in range(3) :
# 	for j in range(2 - i) :
# 		print(end = " ")
# 	for j in range(num) :
# 		print("2", end = "")
# 	for j in range(2 - i) :
# 		print(end = " ") 
# 	print()
# 	num += 2

# 1216
# num = 1
# for i in range(3) :

# 	for j in range(2 - i) :
# 		print(end =" ")
# 	for j in range(num) :
# 		print("2", end = "")
# 	for j in range(2 - i) :
# 		print(end = " ")
# 	print()
# 	num += 2

'''
	[문제5]
		22222
		 222
		  2   
'''
print("[문제5]")
# 1125
# num = 5 
# for i in range(3) :
# 	for j in range(i) :
# 		print(end = " ")
# 	for j in range(num - i) :
# 		print("2", end = "")
# 	for j in range(i) :
# 		print(end = " ") 
# 	print()
# 	num -= 1

# 1216
# num = 0	 
# for i in range(3) :

# 	for j in range(i) :
# 		print(end = " ")

# 	j = 5 - num
# 	while j > 0 :
# 		print("2", end = "")
# 		j -= 1
	
# 	for j in range(i) :
# 		print(end = " ")
# 	print()
# 	num += 2
