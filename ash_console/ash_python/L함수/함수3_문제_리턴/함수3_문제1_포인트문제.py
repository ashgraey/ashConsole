
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
def setUserSplit(user) :
  temp = ""
  userList = []
  for i in range(len(user)) :
    if user[i] == "," :
      userList.append(temp)
      temp = ""
    else :
      temp += user[i]
  userList.append(temp)

  for i in range(len(userList)) :
    userList[i] = userList[i].split("/")

  return userList

def setDataSplit(point) :
  temp = ""
  pointList = []
  for i in range(len(point)) :
    if point[i] == "," :
      pointList.append(temp)
      temp = ""
    else :
      temp += point[i]
  pointList.append(temp)

  for i in range(len(pointList)) :
    pointList[i] = pointList[i].split("/")
    
  return pointList

def getPoint(point, user) :
  pointTot = [0, 0, 0]
  for i in range(len(pointTot)) :

    for j in range(len(point)) :
      if user[i][0] == point[j][1] :
        pointTot[i] += int(point[j][0])
    
  return pointTot

def maxPoint(point, user) :
  max = 0 
  maxIdx = 0
  for i in range(len(point)) :
    if point[i] > max :
      max = point[i]
      maxIdx = i

  return maxIdx

userData = "1001/김철수,"
userData += "1002/이만수,"
userData += "1003/이영희"

pointData = "1/1001,"
pointData += "1/1002,"
pointData += "2/1003,"
pointData += "1/1001,"
pointData += "2/1002"
print(userData, pointData)

userList = setUserSplit(userData)
print(userList)
pointList = setDataSplit(pointData)
print(pointList)
a = getPoint(pointList, userList)
print(a)
maxIdx = maxPoint(a, userList)
print(userList[maxIdx])

