'''
    [문제]
      userList는 회원들의 정보이다. 
      userno 는 회원번호이다.
      username 은 회원이름이다.
      
      pointList는 회원들의 점수이다.
      userno 는 회원번호이다.
      point는 포인트 점수이다.
      
      포인트 점수가 가장높은 회원의 점수와 이름을 구하시오.
      
    [정답]
      5   김철수
'''
userList = [ 
  {"userno" : 1001 , "username" : "김철수"},
  {"userno" : 1002 , "username" : "이만수"},
  {"userno" : 1003 , "username" : "이영희"},
]

pointList = [
  {"userno" : 1001 , "point" : 1},
  {"userno" : 1002 , "point" : 3},
  {"userno" : 1001 , "point" : 4},
  {"userno" : 1003 , "point" : 2},
  {"userno" : 1003 , "point" : 1},
]

max = 0
name = ""
for i in range(len(userList)):
  total = 0
  for j in range(len(pointList)):
    if userList[i]["userno"] == pointList[j]["userno"]:
      total += pointList[j]["point"]
  if total > max:
    max = total
    name = userList[i]["username"]

print(max , " " , name)