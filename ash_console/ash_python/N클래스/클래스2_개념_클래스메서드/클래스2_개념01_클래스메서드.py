# 클래스의 구성요소
# 1) 변수
# 2) 메서드(함수)
 
# 기존 함수와의 차이점(메서드 특징)
# 1) 매개변수(parameter) 자리에 항상 self를 추가해야 함.
# 2) 메서드 밖에서 선언한 변수 사용시, 변수명 앞에 self.을 붙여야한다.


# 함수 의 예제
def func():
    print("함수 호출!")
func()
# --------------------------------
# 클래스 예제
class Test:
    num = 0         # 클래스 변수 : 클래스 영역
 
    def func(self):
        self.num = 10
        tot = 0     # 인스턴스 변수 : 함수 영역
        print("메서드 호출!")  
        
t = Test()
t.num = 100
print(t.num)
t.func()
print(t.num)