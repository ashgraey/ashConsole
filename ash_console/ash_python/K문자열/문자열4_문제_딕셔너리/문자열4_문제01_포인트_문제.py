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
# 0129
# user별 포인트 합산
pointTot = [0, 0, 0]
for i in range(len(pointList)) :
  point = pointList[i]
  for j in range(len(userList)) :
    user = userList[j]
    if point["userno"] == user["userno"] :
        pointTot[j] += point["point"]

print(pointTot)

# max값 찾기
max = 0 
maxIdx = 0
for i in range(len(pointTot)) :
    if max < pointTot[i] :
      max = pointTot[i]
      maxIdx = i

# 출력
print(userList[maxIdx]["username"], max)

# 1차
# # 각 번호의 total point의 값을 totpoint 리스트에 순차적으로 저장
# totpoint = [0, 0, 0]
# for i in range(len(pointList)) :
#   point = pointList[i]

#   if point["userno"] == 1001 :
#     totpoint[0] += point["point"]
  
#   elif point["userno"] == 1002 :
#     totpoint[1] += point["point"]
  
#   else :
#     totpoint[2] += point["point"]
# print(totpoint)

# # max값과 maxIdx값을 찾는다.
# max = 0 
# maxIdx = 0
# for i in range(len(totpoint)) :
#   if max < totpoint[i] :
#     max = totpoint[i]
#     maxIdx = i 

# # 출력
# user = userList[maxIdx]
# print("1등 번호 : ",user["userno"],"1등 점수 : ", max, "1등 이름 : ", user["username"])

# 정답
# max = 0
# name = ""
# for i in range(len(userList)):
#   total = 0
#   for j in range(len(pointList)):
#     if userList[i]["userno"] == pointList[j]["userno"]:
#       total += pointList[j]["point"]
#   if total > max:
#     max = total
#     name = userList[i]["username"]

# print(max , " " , name)