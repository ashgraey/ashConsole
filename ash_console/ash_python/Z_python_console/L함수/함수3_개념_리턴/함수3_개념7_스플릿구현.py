
def mySplit(str, d):
	arr = []
	
	temp = ""
	for i in range(len(str)):
		if str[i] == d :
			arr.append(temp)
			temp = ""
		else:
			temp += str[i]
	arr.append(temp)
	return arr


#기존 스플릿 함수
data = "1001,1002,1003,1004"
data = data.split(",")
print(data)

# 내가 만든 스플릿함수 (모양은 조금다르지만 동작은 똑같이 된다.)
test = "1001,1002,1003,1004"
test = mySplit(test, ",")
print(test)

