"""
   [클래스와 리스트]
        [1] 클래스는 딕셔너리와 활용이 거의 비슷하며, 좀더 직관적으로 사용할수있다. 
"""

# 학생성적관리 프로그램 : 1단계(1차원 리스트)
a = ["1001", "1002", "1003"]
b = [87, 11, 42]
 
# 학생성적관리 프로그램 : 2단계(2차원 리스트)
c = [
        ["1001", 87],
        ["1002", 11],
        ["1003", 42]   ]
 
# 학생성적관리 프로그램 : 3단계(딕셔너리 와 리스트)
c = [
        {"number" : 1001, "score" : 87},
        {"number" : 1002, "score" : 11},
        {"number" : 1003, "score" : 42},  ]

 
# 학생성적관리 프로그램 : 4단계(클래스 와 리스트)
class Student:
    number = 0
    score = 0

d = Student()
d.number = 1001
d.score = 87

e = Student()
e.number = 1002
e.score = 10

stlist = [d , e]
for i in range(len(stlist)):
    print(stlist[i].number , " " , stlist[i].score)
