"""
    [문제]
        어떤 학생의 번호 , 이름 , 국어 ,수학 , 영어점수를 딕셔너리로 표현했다.      
"""

b = {"number" : 1003 , "name" : "김철수" , "국어" : 100 , "수학" : 10 , "영어"  : 30}

# [추가] 위 b딕셔너리에 "총점" 키를 추가하시오.
b["총점"] = b["국어"] + b["수학"] + b["영어"]
for i in b.keys():
    print(i  , b[i] , end=" ")
print()

#[삭제] 위 b딕셔너리에 "총점" 키를 삭제하시오.
del(b["총점"])
for i in b.keys():
    print(i  , b[i] , end=" ")
print()


