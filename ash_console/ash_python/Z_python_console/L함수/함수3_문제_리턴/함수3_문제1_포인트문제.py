
"""
  [문제]
    아래  userData는 회원번호와이름이고 , 
    pointData는 포인트와 회원번호이다.
    포인트는 여러번쌓을수있고, 전부 누적해서 합을 구한다.
    포인터 점수가 가장높은 회원의 이름과 번호를 리스트로반환하는 함수를 만드시오.
    단, 직접만든 스플릿함수를 사용하시오.
  [정답]
    이만수  1002
      
"""
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

def getMax(userList , pointList):
  maxPoint = 0
  for i in range(len(userList)): 
    user = userList[i]
    total = 0
  for j in range(len(pointList)):
    point = pointList[j]
    if user[0] == point[1]:
      total += int(point[0])
    if total > maxPoint:
      maxPoint = total 
  return user

def maxPoint(userData , pointData):
  userList = []
  token1 = mySplit(userData , ",")
  for i in range(len(token1)):
    token2 = mySplit(token1[i] , "/")
    userList.append(token2)

  pointList = []
  token1 = mySplit(pointData , ",")
  for i in range(len(token1)):
    token2 = mySplit(token1[i] , "/")
    pointList.append(token2)

  maxUser = getMax(userList, pointList)
  print(maxUser)  

userData = "1001/김철수,"
userData += "1002/이만수,"
userData += "1003/이영희"

pointData = "1/1001,"
pointData += "1/1002,"
pointData += "2/1003,"
pointData += "1/1001,"
pointData += "2/1002"

#print(userData)
#print(pointData)
maxPoint(userData , pointData)


