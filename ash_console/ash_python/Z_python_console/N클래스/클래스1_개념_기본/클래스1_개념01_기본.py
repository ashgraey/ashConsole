"""
    # 클래스
        [1] 클래스 정의
            1) 키워드 : class
            2) 이름   : Student:
            3) 변수   : 들여쓰기를 하며 변수생성을한다. 
        
        [2] 클래스 선언(생성)
            변수 = 클래스이름()
        
        [3] 클래스 사용
            변수.내부변수 
"""
class Student:
    name = ""
    hakbun = 0
    score = 0
 
# 생성
d = Student()
d.name = "홍길동"
d.hakbun = "1001"
d.score = 87

