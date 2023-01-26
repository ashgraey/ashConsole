'''
   [비어있는 딕셔너리 만들기]
      프로그래밍을 하다보면 빈 딕셔너리를 만들어야 될때가 있다. 
      [1] a = dict() 
      [2] b = {}

   [비어있는 리스트 만들기]
      [1] c = list()
      [2] c = []
'''
a = dict() 

a["number"] = 10001
a["name"] = "김철수"
print(a)

b = {}
b["number"] = 10002
b["name"] = "이영수"
print(b)

c = list()
c.append(10001)
c.append("김철수")
print(c)

d = []
d.append(10002)
d.append("이영수")
print(d)